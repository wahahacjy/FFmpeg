import sys
import os

def generate_generalize(inputfile, qs, feature_num):
    for i in qs:
        line = inputfile.readline().strip('\n')[1:-1];
        datas = line.split(', ');
        label1 = "+1 ";
        label2 = "-1 ";
        count1 = 0;
        count2 = 0;
        for i in range(0, feature_num):
            count1 += float(datas[i]);
            count2 += float(datas[i + 1]);
        for j in range(0, feature_num):
            label1 += str(j + 1) + ":" + str(float(datas[j]) / count1) + " ";
            label2 += str(j + 1) + ":" + str(float(datas[j + 1]) / count2) + " ";
        print label1;
        print label2;
        inputfile.readline();

def generate(inputfile, feature_num):
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
qs_start = 1;
qs_end = 10;
feature_num = 5;
if(len(sys.argv) > 1):
    i = 1;
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-data"):
            data_path = sys.argv[i + 1];
            i += 2;
        elif(sys.argv[i] == "-qstart"):
            qs_start = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-qend"):
            qs_end = int(sys.argv[i + 1]);
            i += 2;
        elif(sys.argv[i] == "-f"):
            feature_num = int(sys.argv[i + 1]);
            i += 2;

        else:
            print "Wrong parameters";
            exit(-1);
if(qs_start > qs_end):
    print "qs error";
    eixt(-1);
#print "Data is " + data_path;
#print "Output is " + output;
datafile = open(data_path, "r");
qs = range(qs_start, qs_end + 1);

line = datafile.readline();
while(line):
    if("q" in line):
        q = int(line[1:line.index("frame") - 1])
        if(q in qs):
            generate(datafile, feature_num);
    line = datafile.readline();

    



