import pandas as pd


def ingestion_init_data(path_file_csv, sep, engine, table_name):
    df = pd.read_csv(path_file_csv, sep=sep)
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
