#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/mi/MBStatistic-xvid-gop10-cbr"
#result_folder="/media/cjy/Exp/MBStatistic-gop10"
yuv_folder="~/Desktop/YUV"
run_folder="/home/cjy/cuda-workspace/ffmpeg/cjy-exp"
svm_txt="xvid-g10-cbr-f100-svm.txt"
gop=10
compress_number=8
frame_number=100
p_frame=$((${frame_number}-${frame_number}/${gop}))
echo ${p_frame}
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=1000;i<=9000;i+=1000))
    do
        python ${run_folder}/enc-dec-cbr.py -v $video -n $compress_number -gop $gop -r $result_folder -b:v ${i}k -yuv $yuv_folder
        python ${run_folder}/mbdiff-cbr.py -v $video -root $result_folder -b:v ${i}k -f ${frame_number}
        rm -f ${result_folder}/${video}_b${i}k/*.yuv;
        rm -rf ${result_folder}/${video}_b${i}k/*_enc;
        rm -rf ${result_folder}/${video}_b${i}k/*_yuv;
        rm -rf ${result_folder}/${video}_b${i}k/*_[2-9].avi;
    done

done
python ${run_folder}/calresult-cbr.py -root $result_folder -pf ${p_frame} > $result_folder/data.txt
python ${run_folder}/generatefeature-cbr.py -data $result_folder/data.txt -all  > $result_folder/$svm_txt
