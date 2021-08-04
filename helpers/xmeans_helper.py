from pyclustering.cluster.xmeans import xmeans

def get_clusters(coordinates):
    xmeans_instance = xmeans(coordinates)
    xmeans_instance.process()

    clusters = xmeans_instance.get_clusters()

    return clusters