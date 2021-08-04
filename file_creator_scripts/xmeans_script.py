import helpers.helper as helper
import helpers.tsne_helper as tsne_helper
import helpers.matrix_helper as matrix_helper
import helpers.xmeans_helper as xmeans_helper

def convert_string_to_number(string):
    return int(string[1:-1])

def create_xmeans_no_tsne():
    results = helper.read_csv_from_args(None, 0)

    last_line = len(results) - 1
    gallery_names = []
    for name in results.iloc[:, 0][0:last_line - 1].drop_duplicates():
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

    for gallery in galleries:
        df = galleries[gallery]
        data = []

        for i in range(1, len(df) - 2):
            row = results.loc[i]
            x = int(row[2].replace("'", "").replace('"', ""))
            y = int(row[3].replace("'", "").replace('"', ""))
            line = [x, y]

            data.append(line)

        cluster = xmeans_helper.get_clusters(data)

        print(cluster)


def create_xmeans_tsne():
    results = helper.read_csv_from_args(None, 0)
    galleries = matrix_helper.getMatrices(results)

    for gallery_name in galleries:
        df = galleries[gallery_name]

        fashion_tsne = tsne_helper.get_fashion_tsne(df)

        cluster = xmeans_helper.get_clusters(fashion_tsne)

        print(cluster)
