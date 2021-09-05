import csv
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List

import gspread

logger = logging.getLogger(__name__)


def fetch_worksheet(keyfile: str, sheet: str):
    gc = gspread.service_account(filename=keyfile)
    worksheet = gc.open_by_key(sheet).get_worksheet(0)

    return worksheet


def run():
    path_to_config = Path('config') / 'base.json'
    with path_to_config.open() as f:
        config = json.load(f)

    path_to_keyfile = Path('config') / config['keyfile']

    for sheet in config['sheets']:
        name = sheet['name']
        key = sheet['key']
        ws = fetch_worksheet(path_to_keyfile, key)
        rows = ws.get_all_values()
        logger.info(f' {name} has {len(rows)} rows')

        now = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        filename = f'{name}_{now}.csv'

        datafile = Path('data') / 'sheets' / filename

        with datafile.open(mode='w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger(__name__).setLevel(level=logging.INFO)
    run()
