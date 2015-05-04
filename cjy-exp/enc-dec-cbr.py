import sys
import subprocess
import os

FFMPEG = "/home/cjy/cuda-workspace/ffmpeg/ffmpeg_g" + " ";
#flags = " -flags +mv4"
flags = "";


def encode_xvid_cbr(src, save_folder, dst, bitrate, gop, is_yuvout, yuv_folder):
    if is_yuvout > 1:
        enccmd = FFMPEG + "-only_mb -cjy_folder " + save_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v libxvid -g " + gop + " -mpeg_quant 1 -b:v " + bitrate + flags + " -threads 1 -y " + dst + " 2>/dev/null";
    else:
        enccmd = FFMPEG + "-only_mb -cjy_folder " + save_folder + " -cjy_yuvout " + yuv_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v libxvid -g " + gop + " -mpeg_quant 1 -b:v " + bitrate + flags + " -threads 1 -y " + dst + " 2>/dev/null";
    print enccmd;
    subprocess.call(enccmd, shell=True)

def decode(src, save_folder, dst):
    deccmd = FFMPEG + "-only_mb -cjy_folder " + save_folder + " -threads 1 -i " + src + " -y " + dst + " 2>/dev/null";
    print deccmd;
    subprocess.call(deccmd, shell=True);

def encode_mpeg4native_cbr(src, save_folder, dst, bitrate, gop, is_yuvout, yuv_folder):
    if is_yuvout > 1:
        enccmd = FFMPEG + "-threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg4 -g " + gop + " -b:v " + bitrate + flags + " -threads 1 " + dst + " >/dev/null 2>&1";
    else:
        enccmd = FFMPEG + "-cjy_yuvout " + yuv_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg4 -g " + gop + " -b:v " + bitrate + flags + " -threads 1 " + dst + " >/dev/null 2>&1";
    print enccmd;
    subprocess.call(enccmd, shell=True)

def encode_mpeg2video_cbr(src, save_folder, dst, bitrate, gop, is_yuvout, yuv_folder):
    if is_yuvout > 1:
        enccmd = FFMPEG + "-threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg2video -g " + gop + " -b:v " + bitrate + flags + " -threads 1 " + dst + " >/dev/null 2>&1";
    else:
        enccmd = FFMPEG + "-cjy_yuvout " + yuv_folder + " -threads 1 -s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg2video -g " + gop + " -b:v " + bitrate + flags + " -threads 1 " + dst + " >/dev/null 2>&1";
    print enccmd;
    subprocess.call(enccmd, shell=True)


result_folder = "/home/cjy/Desktop/MBStatistic" + "/";
yuv_folder = "/home/cjy/Desktop/YUV" + "/";
video = "akiyo";
bitrate = "1000k";
num = 11;
gop = "5";
if(len(sys.argv) > 1):
    i = 1;
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-v"):
            video = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-b:v"):
            bitrate = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-r"):
            result_folder = sys.argv[i + 1];
            result_folder += "/";
            i += 2;
        elif(sys.argv[i] == "-n"):
            num = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-yuv"):
            yuv_folder = sys.argv[i + 1] + "/";
            i += 2;
        elif(sys.argv[i] == "-gop"):
            gop = sys.argv[i + 1];
            i += 2;
        else:
            print "Wrong para";
            exit(-1);

src = yuv_folder + video + "_cif.yuv";
origin = 1;
yuv_save_folder = result_folder + video + "_b" + bitrate + "/" + video + "_yuv";
#checkpath
if not os.path.exists(yuv_save_folder):
    os.makedirs(yuv_save_folder);
for i in range (1,num):
    folder = result_folder + video + "_b" + bitrate;
    save_folder = folder + "/" + video + "_b" + bitrate + "_" + str(i) + "_enc";
    dst = folder + "/" + video + "_b" + bitrate + "_" + str(i) + ".avi";

    if(i > 1 and origin == 1):
        src = folder + "/" + video + "_b" + bitrate + "_" + str(i - 1) + ".yuv";
    origin = 0;
#checkpath
    if not os.path.exists(save_folder):
        os.makedirs(save_folder);
    
#encode
    #encode_mpeg2video_cbr(src, save_folder, dst, bitrate, gop, i, yuv_save_folder);
    #encode_mpeg4native_cbr(src, save_folder, dst, bitrate, gop, i, yuv_save_folder);
    encode_xvid_cbr(src, save_folder, dst, bitrate, gop, i, yuv_save_folder);

#decode
    save_folder = folder + "/" + video + "_b" + bitrate + "_" + str(i) + "_dec";
#checkpath
    if not os.path.exists(save_folder):
        os.makedirs(save_folder);
    src = dst;
    dst = folder + "/" + video + "_b" + bitrate + "_" + str(i) + ".yuv";
    decode(src, save_folder, dst);

#src
    src = dst;






