import sys
import subprocess
import os

check_mb = "/home/cjy/cuda-workspace/ffmpeg/cjy-exp/check_mb.py";
video = "akiyo";
root = "/home/cjy/Desktop/MBStatistic+mv4/";
i = 1;
qs = '0';
frames = 100;
while(i < len(sys.argv) - 1):
    if(sys.argv[i] == "-v"):
        i = i + 1;
        video = sys.argv[i];
        i = i + 1;
    elif(sys.argv[i] == "-root"):
        i = i + 1;
        root = sys.argv[i];
        i = i + 1;
    elif(sys.argv[i] == "-q"):
        i = i + 1;
        qs = sys.argv[i];
        i = i + 1;
    elif(sys.argv[i] == "-f"):
        i = i + 1;
        frames = int(sys.argv[i]);
        i = i + 1;
    else:
        print "Wrong para";
if(int(qs) > 0):
    result_folder = root + "/" + video + "_q" + qs + "/mbdiff";
else:
    result_folder = root + "/" + video + "/mbdiff";
#checkpath
if not os.path.exists(result_folder):
    os.makedirs(result_folder);

#determine num
num = 1;
while(os.path.exists(root+ "/" + video + "_q" + qs + "/" + video + "_q" + qs + "_" + str(num) + "_dec")):
    num += 1;
num -= 1;
print "num = " + str(num);
for i in range (1, num):
    if(int(qs) > 0):
        check_cmd = "python " + check_mb + " " + str(i) + " " + str(i + 1) + " -v " + video + " -r " + root + " -q " + qs + " -f " + str(frames) + " > " + result_folder + "/" + str(i) + "_" + str(i + 1) + ".txt 2>>" + result_folder + "/diff.txt" ;
        print check_cmd;
        subprocess.call(check_cmd, shell=True);
