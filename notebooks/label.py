# This file will be responsible for loading the data from step 1, and then asking the user to label the data
import os
import dotenv
import pandas as pd
import datetime


# Log def

def log(message: str):
    print(f"[{datetime.datetime.now()}] {message}")


# Load dotenv & constants
dotenv.load_dotenv()

TEST_PATH = os.getenv("TEST_PATH")
TRAIN_PATH = os.getenv("TRAIN_PATH")

TEST_PATH_RAW, TRAIN_PATH_RAW = (os.path.join(p, "raw") for p in (TEST_PATH, TRAIN_PATH))
TEST_PATH_PROCESSED, TRAIN_PATH_PROCESSED = (os.path.join(p, "processed") for p in (TEST_PATH, TRAIN_PATH))

# Assume step 1 filename
STEP1 = "step1.csv"
STEP2 = "step2.csv"

TEST_STEP1, TRAIN_STEP1 = (os.path.join(p, STEP1) for p in (TEST_PATH_PROCESSED, TRAIN_PATH_PROCESSED))

# Load the dataframes

test_data = pd.read_csv(TEST_STEP1)
train_data = pd.read_csv(TRAIN_STEP1)

# Display some info
log(f"Test data: {len(test_data.index)}, "
    f"Train data: {len(train_data.index)}")


def generate_code(row):
    return f"{row['font']}_{row['size']}_{row['color']}_{row['length']}"


# Start going over the dataframes
for df, filepath, name in zip(
        [test_data, train_data],
        [os.path.join(p, STEP2) for p in (TEST_PATH_PROCESSED, TRAIN_PATH_PROCESSED)],
        ["test", "train"]
):
    log(
        f"Starting dataframe: {name}"
    )
    # Add the code
    df["code"] = df.apply(generate_code, axis=1)
    log(f"Added code: {len(df['code'].unique())} distinct values")

    #
