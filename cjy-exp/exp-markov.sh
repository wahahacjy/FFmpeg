#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/000F3F760003FDF7/error_feature/xvid-error/"
#result_folder="/media/cjy/Exp/MBStatistic-gop5"
yuv_folder="~/Desktop/YUV"
run_folder="/home/cjy/cuda-workspace/ffmpeg/cjy-exp"
gop=10
compress_number=4
frame_number=100
encoder="xvid"
p_frame=$((${frame_number}-${frame_number}/${gop}))
echo ${p_frame}
#修改这里的yuv文件夹！！
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=1;i<=15;i++))
    do
#记得修改enc-dec.py中的编码
        python ${run_folder}/enc-dec.py -c:v ${encoder} -v $video -n $compress_number -gop $gop -r $result_folder -q $i -yuv $yuv_folder
        rm -f ${result_folder}/${video}_q${i}/*.yuv;
        rm -rf ${result_folder}/${video}_q${i}/*_enc;
        rm -rf ${result_folder}/${video}_q${i}/*_yuv;
        rm -rf ${result_folder}/${video}_q${i}/*.avi;
    done
done
