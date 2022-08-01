import csv
from typing import List

# with open("1_may.csv", encoding='utf-8') as r_file:
#     file_reader = csv.DictReader(r_file, delimiter=";")
#     count = 0
#     data = list()
#     for row in file_reader:
#         data.append((int(row["id_tov_cl"]), float(row["BaseSum"]), row["order_type"]))
#         count += 1
#         #if count >= 50:
#             #break
#     print(f'Всего в файле {count + 1} строк.')
#     data.sort()
#
#     with open("2_may.csv", "w", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         for item in data:
#             writer.writerow(item)



with open("Location.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Название столбцов: {", ".join(row)}')
        print(f'ID МАГАЗИНА {row["id_tt"]} - ШИРОТА {row["Shirota"]}- ДОЛГОТА {row["Dolgota"]}',
              end=',')
        print(f'ФОРМАТ МАГАЗИНА: {row["format"]}')
        count += 1
    count = 0
    print(f'Всего в файле {count + 1} строк.')