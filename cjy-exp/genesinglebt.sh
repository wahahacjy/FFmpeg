#!/bin/bash
#用于生成单个比特率的特征

folder="/media/cjy/mi/MBStatistic-xvid-gop10-cbr";
for((i=100;i<=900;i+=100))
do
python generatefeature-cbr.py -data ${folder}/data.txt -bstart ${i} -bend ${i} > ${folder}/xvid-b${i}k-${i}k-gop10-cbr-svm.txt
done
