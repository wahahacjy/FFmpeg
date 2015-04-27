#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/mi/MBStatistic-mp4native-gop10-cbr"
#result_folder="/media/cjy/Exp/MBStatistic-gop10"
yuv_folder="~/Desktop/YUV"
run_folder="/home/cjy/cuda-workspace/ffmpeg/cjy-exp"
svm_txt="native-g10-cbr-svm.txt"
gop=10
compress_number=8
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=500;i<=1500;i+=100))
    do
        python ${run_folder}/enc-dec-cbr.py -v $video -n $compress_number -gop $gop -r $result_folder -b:v ${i}k -yuv $yuv_folder
        python ${run_folder}/mbdiff-cbr.py -v $video -root $result_folder -b:v ${i}k
        rm -f ${result_folder}/${video}_b${i}k/*.yuv;
        rm -rf ${result_folder}/${video}_b${i}k/*_enc;
        rm -rf ${result_folder}/${video}_b${i}k/*_yuv;
    done
    for((i=2000;i<=9000;i+=1000))
    do
        python ${run_folder}/enc-dec-cbr.py -v $video -n $compress_number -gop $gop -r $result_folder -b:v ${i}k -yuv $yuv_folder
        python ${run_folder}/mbdiff-cbr.py -v $video -root $result_folder -b:v ${i}k
        rm -f ${result_folder}/${video}_b${i}k/*.yuv;
        rm -rf ${result_folder}/${video}_b${i}k/*_enc;
        rm -rf ${result_folder}/${video}_b${i}k/*_yuv;
    done

done
python ${run_folder}/calresult-cbr.py -root $result_folder > $result_folder/data.txt
python ${run_folder}/generatefeature-cbr.py -data $result_folder/data.txt -all  > $result_folder/$svm_txt
