import sys
import subprocess
import os

FFMPEG = "/home/cjy/cuda-workspace/ffmpeg/ffmpeg_g" + " ";
flags ="";

def encode_mpeg4native_cbr(src, dst, bitrate, gop):
    enccmd = FFMPEG + "-s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg4 -g " + gop + " -b:v " + bitrate + " -maxrate " + bitrate + " -minrate " + bitrate + flags + " " + dst + " >/dev/null 2>&1";
    print enccmd;
    subprocess.call(enccmd, shell=True)

def encode_mp2_cbr(src, dst, bitrate, gop):
    enccmd = FFMPEG + "-s cif -pix_fmt yuv420p -i " + src + " -c:v mpeg2video -g " + gop + " -b:v " + bitrate + " -minrate " + bitrate + " -maxrate " + bitrate + flags + " -bufsize 200k " + dst + " >/dev/null 2>&1";
    print enccmd;
    subprocess.call(enccmd, shell=True)

def encode_xvid_cbr(src, dst, bitrate, gop):
    enccmd = FFMPEG + "-s cif -pix_fmt yuv420p -i " + src + " -c:v libxvid -g " + gop + " -b:v " + bitrate + flags + " " + dst + " >/dev/null 2>&1";
    print enccmd;
    subprocess.call(enccmd, shell=True)

def decode(src, save_folder, dst):
#checkpath
    if not os.path.exists(save_folder):
        os.makedirs(save_folder);
    deccmd = FFMPEG + "-markov -cjy_folder " + save_folder + " -threads 1 -i " + src + " -y " + dst + " >/dev/null 2>&1";
    print deccmd;
    subprocess.call(deccmd, shell=True);

def cal_D(folder1, folder2):
    result = list();
    for parent, dirnames, filenames in os.walk(folder1):
        i = 0;
        count = 0;
        filenames.sort();
        for filename in filenames:
            if("I" in filename):
                i += 1;
                file1 = open(folder1 + "/" + filename, "r");
                file2 = open(folder2 + "/" + filename, "r");
                line1 = file1.readline();
                line2 = file2.readline();
                while(line1 != ''):
                    if(not ("Quantized") in line1):
                        line1 = file1.readline();
                        continue;
                    while(not ("Quantized") in line2):
                        line2 = file2.readline();
                    for j in range(0, 8):
                        tmp1 = file1.readline();
                        tmp2 = file2.readline();
                        if(tmp1 != tmp2):
                            array1 = tmp1[0:-2].split();
                            array2 = tmp2[0:-2].split();
                            for k in range(0, len(array1)):
                                if(array1[k] != array2[k]):
                                    count +=1;

                    line1 = file1.readline();
                    line2 = file2.readline();
                file1.close();
                file2.close();
                if(i % 10 == 0):
                    result.append(count);
                    count = 0;
    return result;


result_folder = "/home/cjy/Desktop/MBStatistic" + "/";
yuv_folder = "/home/cjy/Desktop/YUV" + "/";
video = "akiyo";
bitrate = "1000";
bitrate2 = "950";
num = 11;
gop = "5";
encode = encode_mpeg4native_cbr;
if(len(sys.argv) > 1):
    i = 1;
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-v"):
            video = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-b:v"):
            bitrate = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-b:v2"):
            bitrate2 = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-r"):
            result_folder = sys.argv[i + 1];
            result_folder += "/";
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
save_folder = result_folder + video + "_b" + bitrate + "k/";
#checkpath
if not os.path.exists(save_folder):
    os.makedirs(save_folder);

file_name = save_folder + "b_" + bitrate + "k.txt";
output_file = open(file_name, "w");

dst = save_folder + video + "_b" + bitrate + "k_1.avi";
encode(src, dst, bitrate + "k", gop);

dct_folder1 = save_folder + video + "_b" + bitrate + "k_1";
out_yuv = save_folder + video + "_b" + bitrate + "k_1.yuv";
src1 = out_yuv;
decode(dst, dct_folder1, out_yuv);
dst = save_folder + video + "_b" + bitrate + "k_2.avi";
encode(out_yuv, dst, bitrate + "k", gop);
out_yuv = save_folder + video + "_b" + bitrate + "k_2.yuv";
dct_folder2 = save_folder + video + "_b" + bitrate + "k_2";
decode(dst, dct_folder2, out_yuv);
src2 = out_yuv;

#

dst = save_folder + video + "_b" + bitrate + "k_3.avi";
encode(out_yuv, dst, bitrate + "k", gop);
out_yuv = save_folder + video + "_b" + bitrate + "k_3.yuv";
dct_folder3 = save_folder + video + "_b" + bitrate + "k_3";
decode(dst, dct_folder3, out_yuv);


dst = save_folder + video + "_b" + bitrate2 + "k_1.avi";
encode(src1, dst, bitrate2 + "k", gop);
dct_folder_1_2 = save_folder + video + "_b" + bitrate2 + "k_1";
out_yuv = save_folder + "tmp.yuv";
decode(dst, dct_folder_1_2, out_yuv);


dst = save_folder + video + "_b" + bitrate2 + "k_2.avi";
encode(src2, dst, bitrate2 + "k", gop);
dct_folder_2_2 = save_folder + video + "_b" + bitrate2 + "k_2";
out_yuv = save_folder + "tmp.yuv";
decode(dst, dct_folder_2_2, out_yuv);

#count D'
output_file.write(str(cal_D(dct_folder1, dct_folder2)));
output_file.write(str(cal_D(dct_folder1, dct_folder_1_2))+'\n');
output_file.write(str(cal_D(dct_folder2, dct_folder3)));
output_file.write(str(cal_D(dct_folder2, dct_folder_2_2)));

output_file.close();
