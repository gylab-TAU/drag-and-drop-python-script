import argparse
import numpy as np
import pandas as pd
import math
import csv

def distance(r1, r2):
    # gets 2 rows: ["img",xpos, ypos] and calculates distance
    dis = 0
    dis += math.pow(r1[1] - r2[1], 2)
    dis += math.pow(r1[2] - r2[2], 2)
    return round(math.sqrt(dis),3)

def makeMatrixes(galleries):
    matrixes = {}
    for galleryName, rows in galleries.items():
        adjMatrix = []
        titleRow  = [None] + [row[0] for row in rows]
        adjMatrix.append(titleRow)

        for row in rows:
            adjRow = [row[0]]
            for r in rows:
                adjRow.append(distance(row,r))
            adjMatrix.append(adjRow)
        matrixes[galleryName] = adjMatrix

    return matrixes

def makeFiles(data, matrixes):
    for galleryName, rows in matrixes.items():
        fileName = data + "_" + galleryName
        with open(fileName + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def convert_string_to_number(string):
    return float(string[1:-1])

def format_string(string):
    string.replace("\"", "")
    print(string)
    return string

# define args variables
parser = argparse.ArgumentParser()
parser.add_argument("file", help="results file to parse in a csv format")
args = parser.parse_args()

# read results csv
results = pd.read_csv(args.file)
last_line = len(results) - 1
temp = results.loc[0:last_line - 2]
temp.sort_values(by=['"Image Name"'], inplace=True, ignore_index=True)
results.loc[0:last_line - 2] = temp

# get subject and experiment info
subject_info = results.loc[last_line - 1]
experiment_info = results.loc[last_line]

# create empty galleries
gallery_names =[]
for name in results.iloc[:,0][0:last_line - 1].drop_duplicates():
    gallery_names.append(name[1:len(name) - 1])

galleries = {}

for gallery_name in gallery_names:
    galleries[gallery_name] = []

for index in range(0, last_line - 1):
    new_line = []
    new_line.append(results.loc[index][1].replace("\"", ""))
    new_line.append(convert_string_to_number(results.loc[index][2]))
    new_line.append(convert_string_to_number(results.loc[index][3]))
    name = results.loc[index][0]
    galleries[results.loc[index][0][1:len(name) - 1]].append(new_line)

matrixes = makeMatrixes(galleries)
subject_id = experiment_info[3]+"1"
makeFiles(subject_id, matrixes)