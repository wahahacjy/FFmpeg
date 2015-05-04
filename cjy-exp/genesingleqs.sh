#!/bin/bash
#用于生成单个量化因子的特征

folder="/media/cjy/mi/MBStatistic-mp2-gop10";
for((i=1;i<=15;i++))
do
python generatefeature.py -data ${folder}/data.txt -qstart ${i} -qend ${i} > ${folder}/mp2-q${i}-q${i}-gop10-f100-svm.txt
done
