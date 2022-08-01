
/* скрипты характерных выборок */

USE vk;

SELECT * FROM messages;
SELECT * FROM profiles;

SELECT * FROM storehouses_products
  ORDER by value desc;
  
 SELECT 
    weekday(date_format(birthday, '2022-%m-%d')) AS 'day_number',
    COUNT(*) AS 'birthdays_amount'
FROM PROFILES
GROUP BY weekday(date_format(birthday, '2022-%m-%d'))
ORDER BY day_number; 

SELECT m.from_user_id, m.to_user_id, COUNT(*) AS amount FROM messages AS m
	JOIN users AS u ON u.id = m.to_user_id
	WHERE u.email = 'kornilov@mail.ru'
GROUP BY from_user_id;

SELECT like_type, COUNT(*) AS likes FROM posts_likes AS pl 
	JOIN profiles AS p ON pl.user_id = p.user_id  
WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) < 10 AND like_type = 1;

SELECT * FROM users
WHERE EXISTS (SELECT * FROM friends WHERE user_id = users.id)
LIMIT 1;

/* представления */ 

-- 1 представление (выводим взрослых пользователей)

CREATE VIEW Adults AS
	SELECT user_id, gender
FROM profiles AS p
WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) > 18;

SELECT * FROM Adults;

-- 2 представление (выводим всю продукцию с необходимой информацией) 

CREATE VIEW CountProducts AS
	SELECT id, product_id, value 
FROM storehouses_products AS sp;
    
    SELECT * FROM CountProducts;
    
/* триггер (верифицируем дату рождения при ее обновлении) */

DELIMITER //

CREATE TRIGGER check_birthday_before_update BEFORE UPDATE ON profiles 
FOR EACH ROW
BEGIN 
	IF NEW.birthday >= NOW() THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Birthday must be in the past!';
	END IF;
END//

DELIMITER ;

/* процедура (выводим рекомендации пользователю на основе города и сообществ) */

DROP PROCEDURE IF EXISTS sp_friendship_recommendations;

DELIMITER //

CREATE PROCEDURE sp_friendship_recommendations(IN for_user_id BIGINT UNSIGNED)
BEGIN
	SELECT p2.user_id FROM profiles p1
    JOIN profiles p2 ON p1.city = p2.city
	WHERE p1.user_id = for_user_id
    AND p2.user_id != for_user_id
		UNION
	SELECT cu2.user_id FROM communities_users cu1
    JOIN communities_users cu2 ON cu1.community_id = cu2.community_id
    WHERE cu1.user_id = for_user_id
    AND cu2.user_id != for_user_id
    ORDER BY RAND()
    LIMIT 5;
END //

DELIMITER ;

CALL sp_friendship_recommendations(1);

/* функция (выводим популярность пользователя) */

DELIMITER //

CREATE FUNCTION func_user_popularity(for_user_id BIGINT UNSIGNED)
RETURNS FLOAT READS SQL DATA
BEGIN
	DECLARE cnt_to_user INT;
	DECLARE cnt_from_user INT;
	SET cnt_to_user = (SELECT COUNT(*) FROM friend_requests WHERE to_user_id = for_user_id);
    SET cnt_from_user = (SELECT COUNT(*) FROM friend_requests WHERE from_user_id = for_user_id);
    IF cnt_from_user = 0
	THEN 
		RETURN cnt_to_user;
	ELSE
		RETURN cnt_to_user / cnt_from_user;
	END IF;
END//

DELIMITER ;

SELECT func_user_popularity(2);

SELECT func_user_popularity(10);
