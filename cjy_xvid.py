import sys
import subprocess
import os

FFMPEG = "/home/cjy/cuda-workspace/ffmpeg/ffmpeg_g ";
#flags = " -flags +mv4"
flags = "";

def encode(src, save_folder, dst, qs, is_yuvout, yuv_folder):
    if is_yuvout > 1:
        enccmd = FFMPEG + "-cjy_folder " + save_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v libxvid -g 5 -mpeg_quant 1 -q " + qs + flags + " -threads 1 " + dst + " 2>/dev/null";
    else:
        enccmd = FFMPEG + "-cjy_folder " + save_folder + " -cjy_yuvout " + yuv_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v libxvid -g 5 -mpeg_quant 1 -q " + qs + flags + " -threads 1 " + dst + " 2>/dev/null";
    print enccmd;
    subprocess.call(enccmd, shell=True)

def decode(src, save_foder, dst):
    deccmd = FFMPEG + "-cjy_folder " + save_foder + " -threads 1 -i " + src + " " + dst + " 2>/dev/null";
    print deccmd;
    subprocess.call(deccmd, shell=True);

def encode_noxvid(src, save_folder, dst, qs, is_yuvout, yuv_folder):
    if is_yuvout > 1:
        enccmd = FFMPEG + "-cjy_folder " + save_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg4 -g 5 -mpeg_quant 1 -q " + qs + flags + " -threads 1 " + dst + " 2>/dev/null";
    else:
        enccmd = FFMPEG + "-cjy_folder " + save_folder + " -cjy_yuvout " + yuv_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg4 -g 5 -mpeg_quant 1 -q " + qs + flags + " -threads 1 " + dst + " 2>/dev/null";
    print enccmd;
    subprocess.call(enccmd, shell=True)


result_folder = "/home/cjy/Desktop/MBStatistic" + "/";
yuv_folder = "/home/cjy/Desktop/YUV" + "/";
if(len(sys.argv) > 1):
    video = sys.argv[1];
else:
    video = "akiyo";
print video;
qs = "5";
src = yuv_folder + video + "_cif.yuv";
origin = 1;
yuv_save_folder = result_folder + video + "_q" + qs + "/" + video + "_yuv";
#checkpath
if not os.path.exists(yuv_save_folder):
    os.makedirs(yuv_save_folder);
for i in range (1,11):
    folder = result_folder + video + "_q" + qs;
    save_folder = folder + "/" + video + "_q" + qs + "_" + str(i) + "_enc";
    dst = folder + "/" + video + "_q" + qs + "_" + str(i) + ".m4v";

    if(i > 1 and origin == 1):
        src = folder + "/" + video + "_q" + qs + "_" + str(i - 1) + ".yuv";
    origin = 0;
#checkpath
    if not os.path.exists(save_folder):
        os.makedirs(save_folder);
    
#encode
    encode(src, save_folder, dst, qs, i, yuv_save_folder);
    
#decode
    save_folder = folder + "/" + video + "_q" + qs + "_" + str(i) + "_dec";
#checkpath
    if not os.path.exists(save_folder):
        os.makedirs(save_folder);
    src = dst;
    dst = folder + "/" + video + "_q" + qs + "_" + str(i) + ".yuv";
    decode(src, save_folder, dst);

#src
    src = dst;






