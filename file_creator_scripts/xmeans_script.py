import helpers.helper as helper
import helpers.tsne_helper as tsne_helper
import helpers.matrix_helper as matrix_helper
import helpers.xmeans_helper as xmeans_helper
import  pandas as pd

def map_cluster(cluster, df, cluster_name):
    results = []

    for index in cluster:
        row = df[index]
        line = [row[0], row[1], row[2], cluster_name]
        results.append(line)

    return results

def convert_string_to_number(string):
    return int(string[1:-1])

def create_xmeans_no_tsne():
    results = helper.read_csv_from_args(None, 0)
    temp = results.loc[len(results) - 2]
    screen_dimentions = [temp[0], temp[1], temp[2], temp[3]]

    last_line = len(results) - 3
    gallery_names = []
    for name in results.iloc[:, 0][0:last_line - 1].drop_duplicates():
        gallery_names.append(name[1:len(name) - 1])

    galleries = {}


    for gallery_name in gallery_names:
        galleries[gallery_name] = []

    for index in range(0, last_line):
        new_line = []
        new_line.append(results.loc[index][1].replace("\"", ""))
        new_line.append(convert_string_to_number(results.loc[index][2]))
        new_line.append(convert_string_to_number(results.loc[index][3]))
        name = results.loc[index][0]
        galleries[results.loc[index][0][1:len(name) - 1]].append(new_line)

    for gallery in galleries:
        df = galleries[gallery]
        data = []

        for i in range(0, len(df) - 1):
            row = df[i]
            x = row[1]
            y = row[2]
            line = [x, y]

            data.append(line)

        clusters = xmeans_helper.get_clusters(data)

        mapped_clusters = [["file name", "x", "y", "cluster"]]

        for cluster_index in range(len(clusters)):
            temp = map_cluster(clusters[cluster_index], df, str(cluster_index + 1))
            mapped_clusters.extend(temp)

        mapped_clusters.append(screen_dimentions)
        pd.DataFrame(mapped_clusters).to_csv("cluster_" + gallery + ".csv", index=False, index_label=False, header=False)

def create_xmeans_tsne():
    results = helper.read_csv_from_args(None, 0)
    galleries = matrix_helper.getMatrices(results)

    for gallery_name in galleries:
        df = galleries[gallery_name]

        fashion_tsne = tsne_helper.get_fashion_tsne(df)

        cluster = xmeans_helper.get_clusters(fashion_tsne)

        print(cluster)
