# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def main():
    """Plot f1-scores for Labels"""
    N = 15
    names = ['PN', 'PQ', 'UR', 'EX', 'EV', 'XY', 'PE', 'PO', 'EW', 'AC', 'MC', 'PS', 'PS', 'VS', 'QL']
    scores = [0.1, 0.2, 0.3, 0.4, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1.0]

    width = 0.2
    ind = np.arange(N)
    p = plt.bar(ind, scores, color="purple")
    plt.ylabel('F1 Score')
    plt.xlabel('Labels')
    plt.title('F1 Score per Label')
    plt.xticks(ind + width / 2., names)

    plt.show()

if __name__ == '__main__':
    main()
