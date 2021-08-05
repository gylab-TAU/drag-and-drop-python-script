from helpers import helper, matrix_helper
import csv


def makeFiles(data, matrixes):
    for galleryName, rows in matrixes.items():
        fileName = data + "_" + galleryName
        with open(fileName + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)



def format_string(string):
    string.replace("\"", "")
    return string

# get subject and experiment info
results = helper.read_csv_from_args(None, None)
last_line = len(results) - 2
subject_info = results.loc[last_line - 1]
experiment_info = results.loc[last_line]

matrixes = matrix_helper.getMatrices()
subject_id = experiment_info[3]+"1"
makeFiles(subject_id, matrixes)