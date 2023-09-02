
import csv

# with open('playgrounds.csv', encoding='utf-8') as file:
#     data = file.read()
#
#     for line in data.splitlines():
#         print(line.split(';'))


with open('playgrounds.csv', encoding='utf-8') as file:
    data = csv.reader(file)

    for line in data:
        print(line)