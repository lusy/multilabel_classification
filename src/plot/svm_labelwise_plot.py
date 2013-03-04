#!/usr/bin/env python
# encoding: utf-8

import argparse

import numpy as np
import matplotlib.pyplot as plt


def read_labelwise(eval_file):
    ll = {}
    with open(eval_file) as f:
        for l in f:
            k, v = l.strip().split(' ')
            ll[k] = float(v)

    return ll

def get_topics_evaluation(labelcombs=True):
    if labelcombs:
        path = '../../eval/topic_svm/eval_%d_topics_labels_labelcombs.txt'
    else:
        path = '../../eval/topic_svm/eval_%d_topics_labels_ovr.txt'

    eval_dict = {}
    for i in range(10, 200, 30):
        data = read_labelwise(path % i)
        key = "%d topics" % i
        eval_dict[key] = data

    return eval_dict


def plot_eval(eval_dict):
    for title, l in eval_dict.items():
        N = len(l.keys())
        ind = np.arange(N)
        plt.plot(ind, l.values(), label=title)

    plt.xticks(ind, l.keys())
    plt.xlabel('Klassen')
    plt.ylabel('F1 Score')
    plt.legend()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topics', action='store_true', default=False)
    args = parser.parse_args()

    # Create the figure (A4 format)
    plt.figure(num=None, figsize=(4.13, 5.85), dpi=100)

    if args.topics:
        eval_dict = get_topics_evaluation()
        eval_dict2 = get_topics_evaluation(labelcombs=False)

        plt.subplot(211)
        plot_eval(eval_dict)

        plt.subplot(212)
        plot_eval(eval_dict2)

    else:
        ll = read_labelwise('../../eval/text_svm/eval_svm_labels_labelcombs.txt')
        lo = read_labelwise('../../eval/text_svm/eval_svm_labels_ovr.txt')

        eval_dict = {'Labelkombinationen': ll,
                     'One-Vs-Rest': lo}

        plot_eval(eval_dict)

    plt.show()

if __name__ == '__main__':
    main()
