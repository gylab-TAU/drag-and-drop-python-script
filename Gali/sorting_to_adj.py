# usage: from the dir run in cmd the following command: py sorting_to_matrices.py test.csv
# the input is a file where:
# first line is title
# all others are gallery name, image, xpos and ypos.

import argparse
import csv
import math


def convertToIntIfPossible(str):
    try:
        num = float(str[1:-1]) # trim edges
        return num;
    except ValueError:
        return str.replace("\"", "");


def parseData(subjectInfo, expInfo):
    # this func returns a string with information to be used in the output
    # files names
    data = [];
    data.append(expInfo[2]);  # name of exp
    data.append(expInfo[0]);  # date
    data.append(expInfo[3]);  # subject id
    data.append(subjectInfo[0]);  # age
    data.append(subjectInfo[1]);  # gender
    data.append(subjectInfo[2]);  # handedness

    # what this func returns will be concated to the name of the
    # output files. right now it only returns sunject id
    return expInfo[3];

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
        fileName = data + "_" + galleryName;
        with open(fileName + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def Main():
    # CONSTS AND VARS
    subjectInfoDelimiter = "\"age: ";
    galleries = {};

    # define args variables
    parser = argparse.ArgumentParser();
    parser.add_argument("file", help="results file to parse in a csv format");
    args = parser.parse_args();

    # READ RESULTS FILE
    with open(args.file, 'r') as file:
        reader = csv.reader(file)
        next(reader) # skipping the first row which is titles
        for row in reader:
            # if first line
            # subject info row
            if subjectInfoDelimiter in row[0]:
                subjectInfo = list(map(convertToIntIfPossible, row));
            # experiment info row
            elif (row[0][0] != '"'):
                expInfo = row;
            # all other rows
            else:
                # a row looks like: ["galleryName", "imageName", "xPos", "yPos"]
                fixedRow = list(map(convertToIntIfPossible, row));
                currGallery = fixedRow[0]
                if galleries.get(currGallery) is None:
                    galleries[currGallery] = []
                galleries[currGallery].append(fixedRow[1:]);

        matrixes = makeMatrixes(galleries)
        data = parseData(subjectInfo, expInfo)
        makeFiles(data, matrixes)

    exit(0);


if __name__ == '__main__':
    Main()