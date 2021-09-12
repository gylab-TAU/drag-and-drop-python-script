from math import sqrt, pow

def convert_string_to_number(string):
    return float(string[1:-1])


def distance(r1, r2):
    # gets 2 rows: ["img",xpos, ypos] and calculates distance
    dis = pow(r1[1] - r2[1], 2) + pow(r1[2] - r2[2], 2)

    return round(sqrt(dis),3)

def getMatrixCellValue(rows, i, j):
    if j == -1:
        return rows[i][0]
    else:
        return distance(rows[i], rows[j])

def getAdjMatrix(rows):
    titleRow = [None] + [row[0] for row in rows]

    adjMatrix = [titleRow if i == 0 else [getMatrixCellValue(rows, i - 1, j - 1) for j in range(len(rows) + 1)] for i in
                 range(len(rows) + 1)]

    return adjMatrix


def makeMatrixes(galleries):
    matrices = {galleryName: getAdjMatrix(rows) for galleryName, rows in galleries.items()}

    return matrices

def getMatrices(results):
    # read results csv
    #$results = helper.read_csv_from_args(None, 0)
    last_line = len(results) - 4
    temp = results.loc[0:last_line]

    temp.sort_values(by=['"Image Name"'], inplace=True, ignore_index=True)
    results.loc[0:last_line - 3] = temp

    # create empty galleries
    gallery_names = [name[1:len(name) - 1] for name in results.iloc[:, 0][0:last_line].drop_duplicates()]

    galleries = {gallery_name: [] for gallery_name in gallery_names}

    index = 0
    while index < last_line:
        new_line = []
        new_line.append(results.loc[index][1].replace("\"", ""))
        new_line.append(convert_string_to_number(results.loc[index][2]))
        new_line.append(convert_string_to_number(results.loc[index][3]))
        name = results.loc[index][0]
        galleries[results.loc[index][0][1:len(name) - 1]].append(new_line)
        index += 1

    matrices = makeMatrixes(galleries)

    return matrices
