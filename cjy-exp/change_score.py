import os
import re
import sys
import math

#Do not support 4 Mvs
def mb_diff_score_split(file, type_weight, mv_weight, frames = 100):
    input1 = open(file, "r");
    line = input1.readline();
    i = 0;
    flag = False;
    score_list = [];
    score = 0;
    type_num_list = [];
    type_num = 0;
    mv_num_list = [];
    mv_num = 0;
    while(line != ''):
        x = re.match(r'[0-9]{4}_[PI]', line);
        if(x != None):
            i += 1;
            if(i == (frames + 1)):
                i = 1;
                score_list.append(score);
                type_num_list.append(type_num);
                mv_num_list.append(mv_num);
                score = 0;
                type_num = 0;
                mv_num = 0;
        if(line.startswith('MB')):
            #print line;
            type1 = get_type(line);
            mv1 = get_mv(line);
            line1 = line;
            line = input1.readline();
            line2 = line;
            #print line;
            type2 = get_type(line);
            mv2 = get_mv(line);
            #print "1: ", type1, mv1;
            #print "2:, ", type2, mv2;
            if(type1 != type2):
                score += type_weight;
                type_num += 1;
            elif(mv1 != mv2):
                score += mv_weight * norm2(int(mv1[0]) - int(mv2[0]), int(mv1[1]) - int(mv2[1]));
                mv_num += 1;
            #print "score = ", score
            line = input1.readline();
            line = input1.readline
        line = input1.readline();
    input1.close();
    if(i ==  frames):
        score_list.append(score);
        type_num_list.append(type_num);
        mv_num_list.append(mv_num);
    print 'score ', score_list;
    print 'type ', type_num_list;
    print 'mv ', mv_num_list;

def get_type(line):
    x = re.match(r'^MB.+MB_TYPE = (\S+).*', line);
    return x.group(1);

def get_mv(line):
    x = re.match(r'^MB.+MB_TYPE = \S+\s+F.+X =\s*([\-0-9]+),Y =\s*([\-0-9]+)', line);
    if(not x == None):
        return x.groups();
    else:
        return ('0','0');

def norm2(x, y):
    return math.sqrt(x * x + y * y);

test = "MB at 18x5 : QScale = 2   Rounding = 0   MB_TYPE = >    Forward MV0 : X =-39,Y =  0";
root_folder = "/media/cjy/mi/MBStatistic-mp4native-gop10/bridge-far_q2/mbdiff";
type_w = 2;
mv_w = 0.5;
video = "foreman";
qs = "2";
frames = 100;
i = 1;
while( i < len(sys.argv) - 1):
    if(sys.argv[i] == "-folder"):
        root_folder = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == "-v"):
        video = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == "-q"):
        qs = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == "-wt"):
        type_w = float(sys.argv[i + 1]);
        i += 2;
    elif(sys.argv[i] == "-wm"):
        mv_w = float(sys.argv[i + 1]);
        i += 2;
    else:
        print "para error";
        exit(-1);
mb_diff_score_split(root_folder + '/1_2.txt', type_w, mv_w);
mb_diff_score_split(root_folder + '/2_3.txt', type_w, mv_w);
mb_diff_score_split(root_folder + '/3_4.txt', type_w, mv_w);
mb_diff_score_split(root_folder + '/4_5.txt', type_w, mv_w);
mb_diff_score_split(root_folder + '/5_6.txt', type_w, mv_w);
mb_diff_score_split(root_folder + '/6_7.txt', type_w, mv_w);
