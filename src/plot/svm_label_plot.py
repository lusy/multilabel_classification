# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def main():
    """Plot f1-scores for Labels"""
    N = 14
    names = ['PN', 'PQ', 'UR', 'EX', 'EV', 'XY', 'PE', 'PO', 'EW', 'AC', 'MC', 'PS', 'VS', 'QL']
    ovr_scores = [0.56, 0.77, 0.62, 0.52, 0.38, 0.63, 0.49, 0.32, 0.33, 0.52, 0.50, 0.52, 0.57, 0.02]
    comb_scores = [0.54, 0.74, 0.62, 0.52, 0.42, 0.64, 0.51, 0.33, 0.37, 0.54, 0.50, 0.49, 0.57, 0.02]

    width = 0.2
    ind = np.arange(N)
    p1 = plt.bar(ind, comb_scores, color="orange")
    p2 = plt.bar(ind, ovr_scores, color="purple")
    plt.ylabel('F1 Score')
    plt.xlabel('Labels')
    plt.title('F1 Score per Label')
    plt.xticks(ind + width / 2., names)
    plt.yticks(np.arange(0,1.1,0.1))
    plt.legend( (p1[0], p2[0]), ('Labelkombinationen', 'OvR') )

    plt.show()

if __name__ == '__main__':
    main()
