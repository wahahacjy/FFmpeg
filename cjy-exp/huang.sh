#!/bin/bash
#用于生成huang实验数据

result_folder="/home/cjy/Desktop/MBStatistic-mp4native-gop10-all-huang"
#result_folder="/media/cjy/Exp/MBStatistic-gop10"
yuv_folder="~/Desktop/YUV"
run_folder="/home/cjy/cuda-workspace/ffmpeg/cjy-exp"
gop=10
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=200;i<=900;i+=100))
    do
        let b2=i-10;
        python ${run_folder}/huang.py -v $video -gop $gop -r $result_folder -b:v ${i} -b:v2 ${b2} -yuv $yuv_folder
        rm -f ${result_folder}/${video}_b${i}k/*.yuv
        rm -f ${result_folder}/${video}_b${i}k/*.avi
    done

done
