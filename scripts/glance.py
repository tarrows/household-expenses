import json
from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    path_to_config = Path('config') / 'base.json'
    with path_to_config.open() as f:
        config = json.load(f)

    df = pd.read_csv(Path('data') / 'sheets' / config['csv'][0])
    print(df.head())
