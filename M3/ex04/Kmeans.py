#!/usr/bin/env python

from sys import argv
from typing import Tuple, Optional
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import rcParams


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4, graph=False):
        # ... parameters control...
        self.graph=graph
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

    def __graph_init(self, X):
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')
        self.ax.set_title('3d Scatter plot')
        self.YC=np.linspace(0, 255, num=self.n_cluster, endpoint=True)

    def __graph_iterate(self, X):
        plt.cla()
        Y = self.centroids
        lst = np.argmin(self.__compute_distance(X, self.centroids), axis=1)
        XC=[self.YC[i] for i in lst]
        self.ax.scatter(X[..., 1], X[..., 2], X[..., 0], c= XC, alpha=0.3)
        self.ax.scatter(Y[..., 1], Y[..., 2], Y[..., 0], c= self.YC, alpha=1.0, s=(rcParams['lines.markersize']*1.5) ** 2, marker='X')
        self.fig.canvas.draw()
        plt.pause(0.2)

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
        if self.graph:
            self.__graph_init(X)
        self.centroids = X[np.random.permutation(X.shape[0])[:self.n_cluster]]
        for i in range(self.max_iter):
            old_centroids = self.centroids
            if self.graph:
                self.__graph_iterate(X)
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

def __parse_arg() -> Optional[Tuple[str, int, int, bool]]:
    if len(argv) > 5:
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
    graph: bool = False
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
        elif elem[0] == 'graph':
            if elem[1] == 'true':
                graph = True
        else:
            print("unknown argument: " + elem[0])
            return None
    return filepath, ncentroid, max_iter, graph

def __fit_loop(arg, X):
    kmean = KmeansClustering(arg[2], arg[1], arg[3])
    kmean.fit(X)
    lst = kmean.predict(X)
    if arg[1] != 4:
        return lst
    while True:
        h_rank = []
        w_rank = []
        d_rank = []
        for i in range(4):
            h_rank.append([i, np.mean(X[..., 0][lst == i])])
            w_rank.append([i, np.mean(X[..., 1][lst == i])])
            d_rank.append([i, np.mean(X[..., 2][lst == i])])
        h_rank = np.array(h_rank)
        w_rank = np.array(w_rank)
        d_rank = np.array(d_rank)
        h_rank = h_rank[h_rank[:,1].argsort()]
        d_rank = d_rank[d_rank[:,1].argsort()[::-1]]
        if h_rank[3][0] != d_rank[3][0] and h_rank[2][0] != d_rank[2][0]:
            print("Bad run")
            kmean.fit(X)
            lst = kmean.predict(X)
        else:
            print("Good run")
            d_rank = d_rank[d_rank[:,0].argsort()]
            i = int(h_rank[3][0])
            print("\nAsteroids' Belt colonies  : {:3}".format(np.count_nonzero(lst == i)))
            print("H:{:7.2f}, W:{:6.2f}, B:{:5.2f}".format(h_rank[3][1], w_rank[i][1], d_rank[i][1]))
            i = int(h_rank[2][0])
            print("\nMars Republic             : {:3}".format(np.count_nonzero(lst == i)))
            print("H:{:7.2f}, W:{:6.2f}, B:{:5.2f}".format(h_rank[2][1], w_rank[i][1], d_rank[i][1]))
            i = max(int(h_rank[3][0]), int(h_rank[2][0]))
            j = min(int(h_rank[3][0]), int(h_rank[2][0]))
            w_rank = np.delete(w_rank, i, axis = 0)
            w_rank = np.delete(w_rank, j, axis = 0)
            w_rank = w_rank[w_rank[:,1].argsort()]
            h_rank = h_rank[h_rank[:,0].argsort()]
            i = int(w_rank[0][0])
            print("\nThe flying cities of Venus: {:3}".format(np.count_nonzero(lst == w_rank[0][0])))
            print("H:{:7.2f}, W:{:6.2f}, B:{:5.2f}".format(h_rank[i][1], w_rank[0][1], d_rank[i][1]))
            i = int(w_rank[1][0])
            print("\nUnited Nations of Earth   : {:3}".format(np.count_nonzero(lst == w_rank[1][0])))
            print("H:{:7.2f}, W:{:6.2f}, B:{:5.2f}".format(h_rank[i][1], w_rank[1][1], d_rank[i][1]))
            if kmean.graph:
                plt.show()
            break
    return lst



def __my_main() -> int:
    arg = __parse_arg()
    if arg is None:
        return -1
    X = np.array([str(x).rstrip().split(',')[1:] for x in open(arg[0])][1:], dtype=float)
    lst = __fit_loop(arg, X)
    for i in range(arg[1]):
        print("{}: {}".format(i, np.count_nonzero(lst == i)))
    return 0
    kmean = KmeansClustering(arg[2], arg[1], arg[3])
    kmean.fit(X)
    lst = kmean.predict(X)
    if (arg[1] == 4):
        h_rank = []
        w_rank = []
        d_rank = []
        for i in range(4):
            h_rank.append([i, np.mean(X[..., 0][lst == i])])
            w_rank.append([i, np.mean(X[..., 1][lst == i])])
            d_rank.append([i, np.mean(X[..., 2][lst == i])])
            print("{}: {}".format(i, np.count_nonzero(lst == i)))
        h_rank = np.array(h_rank)
        w_rank = np.array(w_rank)
        d_rank = np.array(d_rank)
        h_rank = h_rank[h_rank[:,1].argsort()]
        d_rank = d_rank[d_rank[:,1].argsort()[::-1]]
        if h_rank[3][0] == d_rank[3][0]:
            i = max(int(h_rank[3][0]), int(h_rank[2][0]))
            j = min(int(h_rank[3][0]), int(h_rank[2][0]))
            w_rank = np.delete(w_rank, i, axis = 0)
            w_rank = np.delete(w_rank, j, axis = 0)
            w_rank = w_rank[w_rank[:,1].argsort()[::-1]]
            print("Asteroids' Belt colonies  : {}".format(np.count_nonzero(lst == h_rank[3][0])))
            print("Mars Republic             : {}".format(np.count_nonzero(lst == h_rank[2][0])))
            print("The flying cities of Venus: {}".format(np.count_nonzero(lst == w_rank[0][0])))
            print("United Nations of Earth   : {}".format(np.count_nonzero(lst == w_rank[1][0])))
        else:
            print("Bad run")


if __name__== "__main__":
    __my_main()