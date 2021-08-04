import argparse
import pandas as pd

def read_csv_from_args(index_col, header):
    # define args variables
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="results file to parse in a csv format")
    args = parser.parse_args()

    return pd.read_csv(args.file, index_col=index_col, header=header)

def get_filename_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="results file to parse in a csv format")
    args = parser.parse_args()

    return args.file