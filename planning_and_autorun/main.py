import schedule
import requests


def greeting():
    todos_dict = {
        '08:00': 'Drink coffe',
        '11:00': 'Work meting',
        '23:59': 'Hack))'
    }
    print("Day's task")
    for k, v in todos_dict.items():
        print(f'{k} - {v}')

    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    bts_price = f"BTC {round(data.get('btc_usd').get('last'), 2)}$"
    print(bts_price)


def main():
    # greeting()
    # schedule.every(4).seconds.do(greeting)
    schedule.every().day.at('21:51').do(greeting)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()
