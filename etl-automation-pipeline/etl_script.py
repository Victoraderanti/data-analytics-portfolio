import pandas as pd
import yaml

def extract(path):
    return pd.read_csv(path)

def transform(df):
    # Example transformations
    df = df.dropna()
    if 'OrderDate' in df.columns:
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    return df

def load(df, path):
    df.to_csv(path, index=False)

if __name__ == '__main__':
    config_path = 'etl-automation-pipeline/config/example_config.yaml'
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    src = cfg['source']['path']
    dst = cfg['destination']['path']

    df = extract(src)
    df = transform(df)
    load(df, dst)
    print('ETL job completed successfully')
