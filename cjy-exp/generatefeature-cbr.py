import sys
import os

def generate(inputfile, bt, feature_num):
        line = inputfile.readline().strip('\n')[1:-1];
        datas = line.split(', ');
        label1 = "+1 ";
        label2 = "-1 ";
        for j in range(0, feature_num):
            label1 += str(j + 1) + ":" + datas[j] + " ";
            label2 += str(j + 1) + ":" + datas[j + 1] + " ";
        print label1;
        print label2;




data_path = "/media/cjy/Exp/MBStatistic/newresult.txt";
bt_start = 500;
bt_end = 1500;
bt_interval = 100;
feature_num = 5;
is_all = 0;
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
        elif(sys.argv[i] == "-bi"):
            bt_interval = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-f"):
            feature_num = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-all"):
            is_all = 1;
            i += 1;

        else:
            print "Wrong parameters";
            exit(-1);
if(bt_start > bt_end):
    print "bt error";
    eixt(-1);
#print "Data is " + data_path;
#print "Output is " + output;
datafile = open(data_path, "r");

if(is_all):
    line = datafile.readline();
    while(line):
        if("bitrate: " in line):
            line = datafile.readline().strip('\n')[1:-1];
            datas = line.split(', ');
            label1 = "+1 ";
            label2 = "-1 ";
            for j in range(0, feature_num):
                label1 += str(j + 1) + ":" + datas[j] + " ";
                label2 += str(j + 1) + ":" + datas[j + 1] + " ";
            print label1;
            print label2;
        line = datafile.readline();
else:
    bt = range(bt_start, bt_end + 1, bt_interval);

    line = datafile.readline();
    while(line):
        if("bitrate: " in line):
            bitrate = int(line[len("bitrate: "):line.index("k frame")]);
            if(bitrate in bt):
                generate(datafile, bt, feature_num);
        line = datafile.readline();

    



