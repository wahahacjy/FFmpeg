#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/Exp/MBStatistic"
allvideos=`ls ~/Desktop/YUV/ | cut -d _ -f 1`;
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=1;i<=10;i++))
    do
        python /home/cjy/cuda-workspace/ffmpeg/cjy_xvid.py -v $video -n 10 -r $result_folder -q $i
        python /home/cjy/cuda-workspace/ffmpeg/mbdiff.py -v $video -root $result_folder -q $i
        rm -f ${result_folder}/${video}_q${i}/*.yuv;
        rm -rf ${result_folder}/${video}_q${i}/*_enc;
        rm -rf ${result_folder}/${video}_q${i}/*_yuv;
    done
done
