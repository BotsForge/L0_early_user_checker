# pyinstaller -n "L0_early_user_checker" -F -i "../BF.ico" --add-data "../BF.ico;." main.py

import sys
import ctypes
from time import sleep
import traceback

from loguru import logger

from utils import LOGO


logger.remove(0)
logger.add(sys.stderr, level='DEBUG', colorize=True, format="{time:HH:mm:ss}<level> | {level: <7} | {message}</level>",)


from time import time, sleep

import requests
from loguru import logger


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Priority': 'u=1, i',
    'Referer': 'https://dune.com/',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site'
}
# session = CloudScraper()
session = requests.Session()
session.headers.update(headers)
session.get('https://dune.com/0xtoshi/layerzero-early-and-druable-user-fees-spent')


def get_my_wallets():
    with open('wallets.txt') as file:
        wallets = [i.strip().lower() for i in file.readlines() if i.strip()]
    return wallets


def check_wallet(wallet):
    url = 'https://core-api.dune.com/public/execution'
    json_ = {
        "execution_id": "01J0GDYM9BPVKPC6FZ81BYSRKQ",
        "query_id": 3833505,
        "parameters": [],
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "filters": {
            "where_clause": (
                f"\"user\" ILIKE '%{wallet}%'"
            )
        }
    }
    r = session.post(url, json=json_)

    data = r.json()['execution_succeeded']['data']
    if data:
        data = data[0]
        data['early_user'] = data['early_user'] == "✅ "
        data['durable_user'] = data['durable_user'] == "✅ "

        if data['early_user'] and data['durable_user']:
            logger.success(data)
        elif data['early_user']:
            logger.warning(data)
        elif data['durable_user']:
            logger.debug(data)
        else:
            logger.error(data)
    else:
        logger.critical(wallet)


def main():
    wallets = get_my_wallets()
    for wallet in wallets:
        check_wallet(wallet)
        sleep(0.1)


if __name__ == '__main__':
    ctypes.windll.kernel32.SetConsoleTitleW('L0_early_user_checker')
    print(LOGO)
    try:
        main()
    except Exception as er:
        logger.warning(er)
        logger.debug(traceback.format_exc())
    finally:
        input('Press <Enter> to close...')
