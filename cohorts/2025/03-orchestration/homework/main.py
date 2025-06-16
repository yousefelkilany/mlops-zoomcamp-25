import pandas as pd
from sklearn.feature_extraction import DictVectorizer


def read_dataframe(filename: str):
    df = pd.read_parquet(filename)
    print(f"{df.shape = }")

    df["duration"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
    df["duration"] = df.duration.apply(lambda td: td.total_seconds() / 60)
    df = df[(df.duration >= 1) & (df.duration <= 60)]

    categorical = ["PULocationID", "DOLocationID"]
    df[categorical] = df[categorical].astype(str, copy=False)  # type: ignore

    return df


def preprocess(df: pd.DataFrame, dv: DictVectorizer, fit_dv: bool = False):
    df["PU_DO"] = df["PULocationID"] + "_" + df["DOLocationID"]
    categorical = ["PU_DO"]
    numerical = ["trip_distance"]
    dicts = df[categorical + numerical].to_dict(orient="records")  # type: ignore

    if fit_dv:
        X = dv.fit_transform(dicts)
    else:
        X = dv.transform(dicts)
    return X, dv


path = "../../../../data/yellow_tripdata_2023-03.parquet"

df = read_dataframe(path)
print(f"{df.shape = }")
