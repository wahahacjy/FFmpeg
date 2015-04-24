import sys
import os

def generate(inputfile, bt, feature_num):
    for i in bt:
        line = inputfile.readline().strip('\n')[1:-1];
        datas = line.split(', ');
        label1 = "+1 ";
        label2 = "-1 ";
        for j in range(0, feature_num):
            label1 += str(j + 1) + ":" + datas[j] + " ";
            label2 += str(j + 1) + ":" + datas[j + 1] + " ";
        print label1;
        print label2;
        inputfile.readline();




data_path = "/media/cjy/Exp/MBStatistic/newresult.txt";
bt_start = 500;
bt_end = 1500;
feature_num = 5;
if(len(sys.argv) > 1):
    i = 1;
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-data"):
            data_path = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-bstart"):
            bt_start = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-bend"):
            bt_end = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-f"):
            feature_num = int(sys.argv[i + 1]);
            i += 2;

        else:
            print "Wrong parameters";
            exit(-1);
if(bt_start > bt_end):
    print "bt error";
    eixt(-1);
#print "Data is " + data_path;
#print "Output is " + output;
datafile = open(data_path, "r");
bt = range(bt_start, bt_end + 1, 100);

line = datafile.readline();
while(line):
    if(("bitrate: " + str(bt[0]) + "k") in line):
        generate(datafile, bt, feature_num);
    line = datafile.readline();

    



