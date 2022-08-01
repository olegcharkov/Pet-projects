#import csv

#with open('маты.csv', 'r', newline='', encoding='utf-8') as csvfile:
   #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
   #for row in spamreader:
      #print(', '.join(row))

#read_file = open("token.ini", "r")
#content = read_file.read()
#CP866

import csv

with open("March_SQL.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=",")
    count = 0
    data = list()
    for row in file_reader:
        count += 1
        data.append((int(row["id_tov_cl"]), str(row["BaseSum"]), row["name_gr2"], row["ABC"], row["XYZ"]))
        #data.append((int(row["id_tt"]), row["Shirota"], row["Dolgota"], row["format"]))
        # if count >= 50:
        #     break
    print(f'Всего в файле {count + 1} строк.')
    data.sort()

    with open("check.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=",")
        count = 0
        for item in data:
            writer.writerow(item)
            count += 1
        print(f'Всего в файле {count + 1} строк.')