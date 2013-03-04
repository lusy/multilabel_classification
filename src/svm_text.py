# -*- coding: utf-8 -*-

import os.path
import argparse

import numpy as np

import matplotlib.mlab as mlab

from sklearn import svm

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.multiclass import OneVsRestClassifier


def read_dataset(path, labelcomb=True):
    data = mlab.csv2rec(path, names=['id', 'labels', 'abstracts'], delimiter='\t')

    X = data['abstracts']

    if labelcomb:
        Y = data['labels']
    else:
        Y = [labels.split(',') for labels in data['labels']]

    return X, Y


def write_prediction(prediction, output_file, labelcomb=False):
    with open(output_file, 'w') as f:
        for p in prediction:
            if labelcomb:
                line = p.replace(',', ' ')
            else:
                line = ' '.join(p)
            f.write(line + '\n')

def print_evaluation(Y_predict, Y_test, labelcomb):
    if labelcomb:
        print 'Precision', precision_score(Y_predict, Y_test)
        print 'Recall', recall_score(Y_predict, Y_test)
        print 'F1-Score', f1_score(Y_predict, Y_test)
    else:
        labels = Y_test + Y_predict
        classes = set([c for l in labels for c in l])
        for c in classes:
            eval_Y = [1 if c in l else 0 for l in Y_predict]
            test_Y = [1 if c in l else 0 for l in Y_test]
            print c, 'F1-Score', f1_score(eval_Y, test_Y)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_gram', '-n', action="store", dest="n_gram", default=1, type=int)
    parser.add_argument('--labelcomb', action="store_true", dest="labelcomb", default=False)
    parser.add_argument('--tfidf', action="store_true", dest="tfidf", default=False)
    parser.add_argument('-o', '--output', action="store", dest="output", default='')
    parser.add_argument('-C', action="store", dest="C", default=0.01)
    parser.add_argument('train_file', action="store")

    parser.add_argument('test_file', action="store", nargs='?')

    args = parser.parse_args()

    if not args.test_file:
        args.test_file = args.train_file

    assert os.path.exists(args.train_file), "training_file not found."
    assert os.path.exists(args.test_file), "testing_file not found."

    print "loading data..."
    X_train, Y_train = read_dataset(args.train_file, args.labelcomb)
    X_test, Y_test = read_dataset(args.test_file, args.labelcomb)

    print "transform data..."
    if args.tfidf:
        vec = TfidfVectorizer(ngram_range=(1, args.n_gram), stop_words='english')
    else:
        vec = CountVectorizer(ngram_range=(1, args.n_gram), stop_words='english')

    X_train_vec = vec.fit_transform(X_train)
    X_test_vec = vec.transform(X_test)

    del X_train, X_test

    if args.labelcomb:
        svc = svm.LinearSVC(C=args.C, random_state=0)
    else:
        svc = OneVsRestClassifier(svm.LinearSVC(C=args.C, random_state=0))

    print 'training...'
    svc.fit(X_train_vec, Y_train)

    print 'predict...'
    Y_test_predict = svc.predict(X_test_vec)

    print 'output...'
    if args.output:
        write_prediction(Y_test_predict, args.output, args.labelcomb)
    else:
        print_evaluation(Y_test_predict, Y_test, args.labelcomb)

if __name__ == '__main__':
    main()
