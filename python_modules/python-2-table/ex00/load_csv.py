import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load csv file and convert to a Dataset/Dataframe"""
    df = pd.read_csv(path)
    shape = df.shape
    print(f"Loading dataset of dimensions {shape}")
    return df.head(1)


def main():
    arr = load("landscape.jpg")
    print(arr)


if __name__ == "__main__":
    main()
