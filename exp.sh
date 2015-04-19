#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/mi/MBStatistic-gop20"
#result_folder="/media/cjy/Exp/MBStatistic-gop10"
yuv_folder="~/Desktop/YUV"
gop=20
compress_number=8
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=1;i<=15;i++))
    do
        python /home/cjy/cuda-workspace/ffmpeg/cjy_xvid.py -v $video -n $compress_number -gop $gop -r $result_folder -q $i -yuv $yuv_folder
        python /home/cjy/cuda-workspace/ffmpeg/mbdiff.py -v $video -root $result_folder -q $i
        rm -f ${result_folder}/${video}_q${i}/*.yuv;
        rm -rf ${result_folder}/${video}_q${i}/*_enc;
        rm -rf ${result_folder}/${video}_q${i}/*_yuv;
done
done
python /home/cjy/cuda-workspace/ffmpeg/calresult.py -root $result_folder > $result_folder/data.txt
python /home/cjy/cuda-workspace/ffmpeg/generatefeature.py -data $result_folder/data.txt -qend 15  > $result_folder/xvid-q1-q15-svm.txt
