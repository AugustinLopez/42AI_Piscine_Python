#!/usr/bin/env python

from sys import argv
from typing import Tuple, Optional
import numpy as np

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        # ... parameters control...
        self.n_cluster = ncentroid # number of clusters
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def __compute_distance(self, X, centroids):
        distance = np.zeros((X.shape[0], self.n_cluster))
        for k in range(self.n_cluster):
            distance[:,k] = abs(X - centroids[k, :]).sum(axis=1)
        return distance

    def __compute_centroids(self, X, distance):
        closest = np.argmin(distance, axis=1)
        centroids = np.zeros((self.n_cluster, X.shape[1]))
        for k in range(self.n_cluster):
            centroids[k,:] = np.mean(X[closest == k, :], axis = 0)
        return centroids


    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        self.centroids = X[np.random.permutation(X.shape[0])[:self.n_cluster]]
        for i in range(self.max_iter):
            old_centroids = self.centroids
            distance = self.__compute_distance(X, old_centroids)
            self.centroids = self.__compute_centroids(X, distance)
            if np.all(old_centroids == self.centroids):
                break

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        return np.argmin(self.__compute_distance(X, self.centroids), axis=1)

def __parse_arg() -> Optional[Tuple[str, int, int]]:
    if len(argv) > 4:
        print("too many argument")
        return None
    elif len(argv) < 1:
        print("not enough argument")
        return None
    lst = [x.split('=', 1) for x in argv[1:]]
    try:
        lst = [[x.strip(), y.strip()] for x, y in lst]
    except ValueError:
        print("at least one '=' is required by argument")
        return None
    filepath: str = None
    ncentroid: int = 4
    max_iter: int = 20
    for elem in lst:
        if elem[0] == 'filepath':
            filepath = elem[1]
        elif elem[0] == 'ncentroid':
            try:
                ncentroid = int(elem[1])
            except ValueError:
                print("cannot convert to int: ", elem[1])
                return None
        elif elem[0] == 'max_iter':
            try:
                max_iter = int(elem[1])
            except ValueError:
                print("cannot convert to int: ", elem[1])
                return None
        else:
            print("unknown argument: " + elem[0])
            return None
    return filepath, ncentroid, max_iter

def __my_main() -> int:
    arg = __parse_arg()
    if arg is None:
        return -1
    X = np.array([str(x).rstrip().split(',')[1:] for x in open(arg[0])][1:], dtype=float)
    kmean = KmeansClustering(arg[2], arg[1])
    kmean.fit(X)
    lst = kmean.predict(X)
    if (arg[1] == 4):
        res = []
        h_rank = []
        w_rank = []
        d_rank = []
        for i in range(4):
            h_rank.append([i, np.mean(X[..., 0][lst == i])])
            w_rank.append([i, np.mean(X[..., 1][lst == i])])
            d_rank.append([i, np.mean(X[..., 1][lst == i])])
            print("{}: {}".format(i, np.count_nonzero(lst == i)))
        h_rank = np.array(h_rank)
        w_rank = np.array(w_rank)
        d_rank = np.array(d_rank)
        h_rank = h_rank[h_rank[:,1].argsort()]
        d_rank = d_rank[d_rank[:,1].argsort()[::-1]]
        if h_rank[3][0] == d_rank[3][0]:
            print("Good run")
        else:
            print("Bad run")
        print("Asteroids' Belt colonies: {}".format(np.count_nonzero(lst == h_rank[3][0])))
        w_rank = np.array(w_rank)
        w_rank = np.delete(w_rank, int(h_rank[3][0]), axis = 0)
        w_rank = w_rank[w_rank[:,1].argsort()]
        h_rank = np.delete(h_rank, 3, axis = 0)
        venus = (w_rank[0][0],w_rank[1][0])
        martian = (h_rank[2][0], h_rank[1][0])
        earth1 = (w_rank[2][0], w_rank[1][0])
        earth2 = (h_rank[0][0], h_rank[1][0])
        print(venus)
        print(martian)
        print(earth1)
        print(earth2)






if __name__== "__main__":
    __my_main()