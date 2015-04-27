#!/bin/bash
#用于生成单个量化因子的特征

folder="/media/cjy/mi/MBStatistic-mp4native-gop20";
for((i=1;i<=15;i++))
do
python generatefeature.py -data ${folder}/data.txt -qstart ${i} -qend ${i} > ${folder}/native-q${i}-q${i}-gop20-svm.txt
done
