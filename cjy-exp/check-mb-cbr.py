import os
import os.path
import sys

diff_mb_num_I = [];
diff_mb_num_P = [];
diff_total = [];
def check_mb_diff(folder1, folder2, frames):
    global diff_mb_num_P, diff_mb_num_I, diff_total;
    for parent, dirnames, filenames in os.walk(folder1):
        filenames.sort();
        index = 0;
        tmp_P = 0;
        tmp_I = 0;
        tmp_total = 0;
        for i in range(0, len(filenames)):
            print filenames[i];
            input1 = open(folder1 + "/" + filenames[i], "r");
            input2 = open(folder2 + "/" + filenames[i], "r");
            for line1 in input1:
                if(not line1.startswith("MB")):
                    continue;
                line2 = input2.readline();
                while(not line2.startswith("MB")):
                    line2 = input2.readline();
                pos = line1.index("MB_TYPE");
                if line1[pos:] != line2[pos:]:
                    tmp_total += 1;
                    if("I" in filenames[i]):
                        tmp_I += 1;
                    elif("P" in filenames[i]):
                        tmp_P += 1;
                    print line1.strip('\n');
                    print line2;
            j = (i + 1) / frames;
            if(j > index):
                index = j;
                diff_mb_num_P.append(tmp_P);
                diff_mb_num_I.append(tmp_I);
                diff_total.append(tmp_total);
                tmp_P = tmp_I = tmp_total = 0;
            input1.close();
            input2.close();

root = "/home/cjy/Desktop/MBStatistic+mv4/";
video = "foreman";
#qs = "2";
bitrate = "600k"
frames = 300;
if(len(sys.argv) > 2):
    num1 = int(sys.argv[1]);
    num2 = int(sys.argv[2]);
    for i in range (3, len(sys.argv)):
        if(sys.argv[i] == "-v"):
            i = i + 1;
            video = sys.argv[i];
        if(sys.argv[i] == "-r"):
            i = i + 1;
            root = sys.argv[i] + "/";
        if(sys.argv[i] == "-b:v"):
            i = i + 1;
            bitrate = sys.argv[i];
        if(sys.argv[i] == "-f"):
            i = i + 1;
            frames = int(sys.argv[i]);
else:
    exit(-1);
if(num1 > num2):
    num1 = num1 + num2;
    num2 = num1 - num2;
    num1 = num1 - num2;
folder1 = root + video + "_b" + bitrate + "/" + video + "_b" + bitrate + "_" + str(num1) + "_dec";
folder2 = root + video + "_b" + bitrate + "/" + video + "_b" + bitrate + "_" + str(num2) + "_dec";
print "folder1 = " + folder1;
print "folder2 = " + folder2;
check_mb_diff(folder1, folder2, frames);
sys.stderr.write("I-mb diff = " + str(diff_mb_num_I)[1:-1] + "\n");
sys.stderr.write("P-mb diff = " + str(diff_mb_num_P)[1:-1] + "\n");
sys.stderr.write("Total diff = " + str(diff_total)[1:-1] + "\n\n");
