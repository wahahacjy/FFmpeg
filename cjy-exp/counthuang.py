import os
import sys

i = 1;
root_folder = "";
while(i < len(sys.argv)):
    if(sys.argv[i] == "-root"):
       root_folder = sys.argv[i + 1];
       i += 2;
    else:
        print "Wrong para";
        exit(-1);

parent, dirnames, filenames = os.walk(root_folder).next();
dirnames.sort();
total = [0, 0, 0, 0, 0, 0, 0, 0, 0];
tp = [0, 0, 0, 0, 0, 0, 0, 0, 0];
tn = [0, 0, 0, 0, 0, 0, 0, 0, 0];
for dirname in dirnames:
    filename = parent + dirname + "/b_" + dirname[dirname.rindex('b') + 1:] + ".txt";
    b = int(dirname[dirname.rindex('b') + 1: dirname.rindex('b') + 2]) - 1;
    print filename;
    inputfile = open(filename, 'r');
    single = inputfile.readline();
    double = inputfile.readline();
    single_D = single[1:single.index(']')].split(',');
    single_DD = single[single.rindex('[') + 1: -2].split(',');
    double_D = double[1:double.index(']')].split(',');
    double_DD = double[double.rindex('[') + 1: -1].split(',');
    for i in range(0, len(single_D)):
        total[b] += 2;
        if(int(single_D[i]) >= int(single_DD[i])):
            tp[b] += 1;
        if(int(double_D[i]) < int(double_DD[i])):
            tn[b] += 1;

    inputfile.close();
    print total;
    print tp;
    print tn;
print total;
print tp;
print tn;
