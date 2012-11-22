# -*- coding: utf-8 -*-

import sys


def chunks(l, n):
    # From http://stackoverflow.com/a/1751478
    return [l[i:i + n] for i in range(0, len(l), n)]


def main(args):
    """docstring for main"""
    labels = []
    for l in sys.stdin.readlines():
        line_split = l.strip().split('\t')
        doc_labels = line_split[1].split(',')
        label_index = []

        for label in doc_labels:
            if label not in labels:
                labels.append(label)

            label_index.append(str(labels.index(label)))

        label_str = ','.join(label_index)
        feat = line_split[2:]
        chunk_feat = [(int(t) + 1, float(p)) for t, p in chunks(feat, 2)]
        chunk_feat.sort()
        feat_str = ' '.join(["%d:%f" % c for c in chunk_feat])
        output = label_str + " " + feat_str + " # " + line_split[0] + "\n"

        try:
            sys.stdout.write(output)
            sys.stdout.flush()
        except:
            break

    with open("label_map.txt", "w") as f:
        for i, label in enumerate(labels):
            f.write("%d\t%s\n" % (i, label))

if __name__ == '__main__':
    main(sys.argv[1:])
