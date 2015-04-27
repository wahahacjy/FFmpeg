#!/bin/bash
#用于复制视频

src_folder="/media/cjy/mi/MBStatistic-mp4native-gop10"
qs=10
dst_folder="/home/cjy/Desktop/YUV-q${qs}"
mkdir $dst_folder
#修改这里的yuv文件夹！！
allvideos=`ls ~/Desktop/YUV/ | grep .yuv | cut -d _ -f 1`;
echo $allvideos
videos=($allvideos);
for video in ${videos[@]}
do
    echo video = $video;
    cp ${src_folder}/${video}_q${qs}/${video}_q${qs}_1.m4v ${dst_folder}/
    ffmpeg -i ${dst_folder}/${video}_q${qs}_1.m4v ${dst_folder}/${video}_cif.yuv
done
rm ${dst_folder}/*.m4v
