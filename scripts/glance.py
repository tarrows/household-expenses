import json
import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    path_to_config = Path('config') / 'base.json'
    with path_to_config.open() as f:
        config = json.load(f)

    df = pd.read_csv(Path('data') / 'sheets' / config['csv'])
    print(df.head())
