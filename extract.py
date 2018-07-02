#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=utf-8 autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

# Readme:
# 将lineages文件中tax_id, 界门纲目科属种的信息抽取出来，去除其他信息
# 一些背景知识：
# 'Bacteria', # 细菌
# 'Archaea', # 古菌
# 'Fungi', # 真菌

import argparse

def clean(field):
    return field.replace('"','').replace("'",'').replace(" ","_")

def main():

    parser = argparse.ArgumentParser(description="Extract the fields only we need.")
    parser.add_argument('--file', type=str, required=True, help='the taxon file path')
    args = parser.parse_args()

    count = 0
    lineages = args.file
    extractedLineages = 'extract.'+lineages
    lineages_fp = open(lineages)
    extractedLineages_fp = open(extractedLineages, 'w')

    for line in lineages_fp:
        segment = line.split(',')

        # fields define
        Tax_id = segment[0]
        Superkindom = segment[1]
        Phylum = segment[2]
        Class = segment[3]
        Order = segment[4]
        Family = segment[5]
        Genus = segment[6]
        Species = segment[7]
        Kindom = segment[12]

        # 因为分类学的混乱，而我们认为真菌界是一个独立的超界，所以，当一个物种
        # 属于Fungi这个kindom时，我们将其superkindom也改成Fungi
        if Kindom == 'Fungi': Superkindom = 'Fungi'
        # 我们未来是通过Species来查询其分类树的，所以，如果此行中Species为空，那么
        # 这行数据对我们来说就无意义，我们将其过滤掉
        if len(Species.strip()) == 0: continue

        # 组织并且写入数据
        data = (
                clean(Tax_id),
                clean(Superkindom),
                clean(Phylum),
                clean(Class),
                clean(Order),
                clean(Family),
                clean(Genus),
                clean(Species)
                )
        extractedLineages_fp.write(','.join(data)+"\n")

    extractedLineages_fp.close()
    lineages_fp.close()

if __name__ == '__main__':
    main()


