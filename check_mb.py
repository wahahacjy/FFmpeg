import os
import os.path
import sys


def check_mb_diff(root, video, folder1, folder2):
    folder = root + video + "/";
    for parent, dirnames, filenames in os.walk(folder + folder1):
        filenames.sort();
        for i in range(0, len(filenames)):
            print filenames[i];
            input1 = open(folder + folder1 + filenames[i], "r");
            input2 = open(folder + folder2 + filenames[i], "r");
            for line1 in input1:
                line2 = input2.readline();
                if line1.startswith("MB"):
                    if line1 != line2:
                        print line1.strip('\n');
                        print line2;
            input1.close();
            input2.close();

if(len(sys.argv) > 2):
    num1 = sys.argv[1];
    num2 = sys.argv[2];
else:
    exit(0);
root = "/home/cjy/Desktop/";
video = "akiyo";
folder1 = video + "_q5_" + num1 + "_dec/";
folder2 = video + "_q5_" + num2 + "_dec/";
check_mb_diff(root, video, folder1, folder2);
