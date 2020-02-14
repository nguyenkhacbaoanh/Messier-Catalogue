import pandas as pd
from functools import wraps
from flask import request
import os

def ingestion_init_data(path_file_csv, sep, engine, table_name):
    df = pd.read_csv(path_file_csv, sep=sep)
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "X-API-KEY" in request.headers:
            token = request.headers["X-API-KEY"]

        if not token:
            return {"message": "Token is missing !!!"}, 401
        if token != os.getenv("TOKEN"):
            return {"message": "Token is wrongs !!!"}, 401

        return f(*args, **kwargs)
    return decorated