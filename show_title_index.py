#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=utf-8 autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import argparse


def main():
    parser = argparse.ArgumentParser(description="show title and it's index.")
    parser.add_argument('--file', type=str, required=True, help='the taxon file path')
    args = parser.parse_args()

    count = 0
    lineages = args.file
    with open(lineages, "r") as fp:
        for line in fp:
            segment = line.strip().split(',')
            for index, item in enumerate(segment):
                print([index,item])
            count += 1
            if count == 1:
                exit(0)

if __name__ == '__main__':
    main()
