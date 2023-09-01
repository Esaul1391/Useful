import csv
import json

# name_1 = "Anna"
# name_2 = "Victor"
# data_names = [name_1, name_2]

# with open("data.csv", 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         # data_names
#         ('user_name', 'user_address')
#     )

# user_data = [
#     ['user1', 'address1'],
#     ['user2', 'address2'],
#     ['user3', 'address3']
# ]
# user_data = [
# ('user_name', 'user_address'),
#     ['user1', 'address1'],
#     ['user2', 'address2'],
#     ['user3', 'address3']
# ]


# for user in user_data:
#     with open('data.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             user
#         )

# with open('data.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(
#         user_data
#     )




# with open('data1.csv', 'w', encoding='cp1251', newline='') as file: # for Windows
with open('data1.csv', 'w') as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(
        (
            "Цена",
            "Количество",
            "Итог"
        )
    )

with open('data.txt') as file:
    src = json.load(file)

asks = src['data']['next']['next']['asks']

for a in asks:
    price = a[0]
    coin_count = a[1]
    amount = price * coin_count

    with open('data.csv', 'a') as file:
        writer.writerow(
            (
            price,
            coin_count,
            amount
            )
        )