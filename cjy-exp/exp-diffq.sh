#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/mi/MBStatistic-mp4native-gop10-q10"
#result_folder="/media/cjy/Exp/MBStatistic-gop10"
yuv_folder="~/Desktop/YUV-q10"
svm_txt="native-q1-q10-g10-q10-svm.txt"
run_folder="/home/cjy/cuda-workspace/ffmpeg/cjy-exp"
gop=10
compress_number=8
#修改这里的yuv文件夹！！
allvideos=`ls ~/Desktop/YUV-q10/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=1;i<=10;i++))
    do
#记得修改enc-dec.py中的编码
        python ${run_folder}/enc-dec.py -v $video -n $compress_number -gop $gop -r $result_folder -q $i -yuv $yuv_folder
        python ${run_folder}/mbdiff.py -v $video -root $result_folder -q $i
        rm -f ${result_folder}/${video}_q${i}/*.yuv;
        rm -rf ${result_folder}/${video}_q${i}/*_enc;
        rm -rf ${result_folder}/${video}_q${i}/*_yuv;
done
done
python ${run_folder}/calresult.py -root $result_folder > $result_folder/data.txt
python ${run_folder}/generatefeature-diffq.py -data $result_folder/data.txt -qend 10  > $result_folder/$svm_txt
