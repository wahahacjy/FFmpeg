#!/bin/bash
#用于生成单个量化因子的特征

folder="/media/cjy/mi/MBStatistic-mp4native-gop10";
for((i=1;i<=15;i++))
do
python generatefeature.py -data ${folder}/data-score.txt -qstart ${i} -qend ${i} > ${folder}/native-q${i}-q${i}-f100-svm-score.txt
done
