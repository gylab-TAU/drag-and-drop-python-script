import helpers.helper as helper
import helpers.tsne_helper as tsne_helper
import helpers.matrix_helper as matrix_helper

def create_tsne():
    results = helper.read_csv_from_args(None, 0)
    galleries = matrix_helper.getMatrices(results)

    for gallery_name in galleries:
        df = galleries[gallery_name]

        tsne = tsne_helper.get_tsne(df)

        tsne.to_csv(gallery_name + "_tsne" + ".csv", index=False)
