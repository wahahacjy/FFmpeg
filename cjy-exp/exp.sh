#!/bin/bash
#用于生成各种实验数据

result_folder="/media/cjy/mi/MBStatistic-mp2-gop10"
#result_folder="/media/cjy/Exp/MBStatistic-gop10"
yuv_folder="~/Desktop/YUV"
svm_txt="mp2-q1-q10-g10-f100-svm.txt"
run_folder="/home/cjy/cuda-workspace/ffmpeg/cjy-exp"
gop=10
compress_number=8
frame_number=100
p_frame=$((${frame_number}-${frame_number}/${gop}))
echo ${p_frame}
#修改这里的yuv文件夹！！
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    for((i=1;i<=10;i++))
    do
#记得修改enc-dec.py中的编码
#python ${run_folder}/enc-dec.py -v $video -n $compress_number -gop $gop -r $result_folder -q $i -yuv $yuv_folder
        rm -rf ${result_folder}/${video}_q${i}/mbdiff;
        python ${run_folder}/mbdiff.py -v $video -root $result_folder -q $i -f ${frame_number}
        rm -f ${result_folder}/${video}_q${i}/*.yuv;
        rm -rf ${result_folder}/${video}_q${i}/*_enc;
        rm -rf ${result_folder}/${video}_q${i}/*_yuv;
        rm -f ${result_folder}/${video}_q${i}/*_[2-9].avi;
done
done
python ${run_folder}/calresult.py -root $result_folder -pf ${p_frame}> $result_folder/data.txt
python ${run_folder}/generatefeature.py -data $result_folder/data.txt -qend 10  > $result_folder/$svm_txt
