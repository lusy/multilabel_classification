# -*- coding: utf-8 -*-

import csv
import os.path
import argparse

#import numpy as np

from sklearn import svm

from sklearn.multiclass import OneVsRestClassifier

from svm_text import print_evaluation, write_prediction


def parse_row(row):
    """docstring for parse_row"""
    feat = row[2:]
    topics = [(int(i), float(t)) for i, t in zip(feat[0:-1:2], feat[1::2])]
    topics.sort()
    topic_props = [t for i, t in topics]
    label = row[1]

    return topic_props, label


def read_file(path):
    """docstring for read_file"""
    X, Y = [], []
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter="\t")
        for row in csv_reader:
            x, y = parse_row(row)
            X.append(x)
            Y.append(y.split(','))

    return X, Y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--labelcomb', action="store_true", dest="labelcomb", default=False)
    parser.add_argument('-o', '--output', action="store", dest="output", default='')
    parser.add_argument('-C', action="store", dest="C", default=1.0)
    parser.add_argument('train_file', action="store")
    parser.add_argument('test_file', action="store")

    args = parser.parse_args()

    assert os.path.exists(args.train_file), "training_file not found."
    assert os.path.exists(args.test_file), "testing_file not found."

    print 'read files...'
    X_train, Y_train = read_file(args.train_file)
    X_test, Y_test = read_file(args.test_file)

    if args.labelcomb:
        Y_train = [' '.join(l) for l in Y_train]
        Y_test = [' '.join(l) for l in Y_test]

    print len(X_train), len(X_test)

    print 'learn...'
    if args.labelcomb:
        svc = svm.LinearSVC(C=args.C, random_state=0)
    else:
        svc = OneVsRestClassifier(svm.LinearSVC(C=args.C, random_state=0))

    svc.fit(X_train, Y_train)

    print 'predict...'
    pred = svc.predict(X_test)

    print 'output...'
    if args.output:
        write_prediction(pred, args.output, args.labelcomb)
    else:
        if args.labelcomb:
            print_evaluation(pred, Y_test, args.labelcomb)
        else:
            Y_pred = [list(l) for l in pred]
            print_evaluation(Y_pred, Y_test, args.labelcomb)

if __name__ == '__main__':
    main()
