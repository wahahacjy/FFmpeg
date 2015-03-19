import os
import os.path
import sys

diff_mb_num_I = 0;
diff_mb_num_P = 0;
diff_total = 0;
def check_mb_diff(root, video, folder1, folder2, qs):
    global diff_mb_num_P, diff_mb_num_I, diff_total;
    folder = root + video + "_q" + qs + "/";
    for parent, dirnames, filenames in os.walk(folder + folder1):
        filenames.sort();
        for i in range(0, len(filenames)):
            print filenames[i];
            input1 = open(folder + folder1 + filenames[i], "r");
            input2 = open(folder + folder2 + filenames[i], "r");
            for line1 in input1:
                if(not line1.startswith("MB")):
                    continue;
                line2 = input2.readline();
                while(not line2.startswith("MB")):
                    line2 = input2.readline();
                if line1 != line2:
                    diff_total += 1;
                    if("I" in filenames[i]):
                        diff_mb_num_I += 1;
                    elif("P" in filenames[i]):
                        diff_mb_num_P += 1;
                    print line1.strip('\n');
                    print line2;
            input1.close();
            input2.close();

root = "/home/cjy/Desktop/MBStatistic+mv4/";
video = "foreman";
qs = "2";
if(len(sys.argv) > 2):
    num1 = int(sys.argv[1]);
    num2 = int(sys.argv[2]);
    for i in range (3, len(sys.argv)):
        if(sys.argv[i] == "-v"):
            i = i + 1;
            video = sys.argv[i];
        if(sys.argv[i] == "-r"):
            i = i + 1;
            root = sys.argv[i];
        if(sys.argv[i] == "-q"):
            i = i + 1;
            qs = sys.argv[i];
else:
    exit(-1);
if(num1 > num2):
    num1 = num1 + num2;
    num2 = num1 - num2;
    num1 = num1 - num2;
folder1 = video + "_q" + qs + "_" + str(num1) + "_dec/";
folder2 = video + "_q" + qs + "_" + str(num2) + "_dec/";
print "folder1 = " + root + video + "_q" + qs + "/" + folder1;
print "folder2 = " + root + video + "_q" + qs + "/" + folder2;
check_mb_diff(root, video, folder1, folder2, qs);
sys.stderr.write("I-mb diff = " + str(diff_mb_num_I) + "\n");
sys.stderr.write("P-mb diff = " + str(diff_mb_num_P) + "\n");
sys.stderr.write("Total diff = " + str(diff_total) + "\n\n");
