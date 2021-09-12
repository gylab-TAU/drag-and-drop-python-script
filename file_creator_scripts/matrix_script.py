import numpy as np
import pandas as pd
from helpers import helper, matrix_helper
import csv


def makeFiles(data, matrixes):
    for galleryName, rows in matrixes.items():
        fileName = data + "_" + galleryName
        with open(fileName + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)



def format_string(string):
    if isinstance(string, str):
        string.replace("\"", "")
    return string

# get subject and experiment info
def create_matricex():
    results = helper.read_csv_from_args(None, 0)
    last_line = len(results) - 2
    subject_info = results.loc[last_line - 1]
    experiment_info = results.loc[last_line]
    matrixes = matrix_helper.getMatrices(pd.DataFrame(results,None, results.columns))
    subject_id = str(experiment_info[3])
    makeFiles(subject_id, matrixes)