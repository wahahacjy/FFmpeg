#!/bin/bash
#用于生成单个量化因子的特征

folder="/media/cjy/Exp/MBStatistic-xvid-gop10-mv4-qpel";
for((i=1;i<=15;i++))
do
python generatefeature.py -data ${folder}/data.txt -qstart ${i} -qend ${i} > ${folder}/xvid-q${i}-q${i}-gop10-mv4-qpel-f100-svm.txt
done
