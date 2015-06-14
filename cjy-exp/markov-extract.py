import os.path
import sys

def cal_markov(folder, label):
    for parent, dirnames, filenames in os.walk(folder):
        for j in range(0, len(filenames)):
            trans = [ [ [0 for i in range(9)] for i in range(9)] for i in range(4)];
            diff = [ [ [0 for i in range(8)] for i in range(8)] for i in range(4)];
            dct = [ [0 for i in range(8)] for i in range(8)];
            #print "Frame " + filenames[j];
            file1 = folder + filenames[j];
            input1 = open(file1, "r");
            line = input1.readline();
            eof = 0;
            while(line != ''):
                while(not line.startswith("Quantized")):
                    line = input1.readline();
                    if(line == ''):
                        eof = 1;
                        break;
                if(eof == 1):
                    break;
                for k in range(0,8):
                    line = input1.readline().strip('\n').strip(';');
                    dct[k] = (line.split());

                #calculate right diff
                for x in range(8):
                    for y in range(7):
                        diff[0][x][y] = int(dct[x][y]) - int(dct[x][y + 1]) + 4;
                        if(diff[0][x][y] > 8):
                            diff[0][x][y] = 8;
                        elif(diff[0][x][y] < 0):
                            diff[0][x][y] = 0;
                for x in range(8):
                    for y in range(6):
                        trans[0][diff[0][x][y]][diff[0][x][y+1]] += 1;
                #calculate down diff
                for x in range(7):
                    for y in range(8):
                        diff[1][x][y] = int(dct[x][y]) - int(dct[x + 1][y]) + 4;
                        if(diff[1][x][y] > 8):
                            diff[1][x][y] = 8;
                        elif(diff[1][x][y] < 0):
                            diff[1][x][y] = 0;
                for x in range(6):
                    for y in range(8):
                        trans[1][diff[1][x][y]][diff[1][x + 1][y]] += 1;
                #calculate right-down diff
                for x in range(7):
                    for y in range(7):
                        diff[2][x][y] = int(dct[x][y]) - int(dct[x + 1][y + 1]) + 4;
                        if(diff[2][x][y] > 8):
                            diff[2][x][y] = 8;
                        elif(diff[2][x][y] < 0):
                            diff[2][x][y] = 0;
                for x in range(6):
                    for y in range(6):
                        trans[2][diff[1][x][y]][diff[1][x + 1][y + 1]] += 1;
                #calculate left-down diff
                for x in range(7):
                    for y in range(7):
                        diff[3][x][y] = int(dct[x][y + 1]) - int(dct[x + 1][y]) + 4;
                        if(diff[3][x][y] > 8):
                            diff[3][x][y] = 8;
                        elif(diff[3][x][y] < 0):
                            diff[3][x][y] = 0;
                for x in range(6):
                    for y in range(6):
                        trans[3][diff[1][x][y + 1]][diff[1][x + 1][y]] += 1;
                line = input1.readline();
            #print trans[0];
            #print trans[1];
            #print trans[2];
            #print trans[3];
            F = [ [ [0 for i in range(9)] for i in range(9)] for i in range(2)];
            i = 1;
            print label,;
            for x in range(9):
                for y in range(9):
                    F[0][x][y] = float(trans[0][x][y] + trans[1][x][y]) / (2 * right_total);
                    print str(i) + ":" + str(F[0][x][y]),;
                    i += 1;
            for x in range(9):
                for y in range(9):
                    F[1][x][y] = float(trans[2][x][y] + trans[3][x][y]) / (2 * diag_total);
                    print str(i) + ":" + str(F[1][x][y]),;
                    i += 1;
            print;
            input1.close();
root = "/media/cjy/mi/MBStatistic-xvid-gop10-markov/";
video = "akiyo";
qs = "1";
if(len(sys.argv) > 1):
    i = 1;
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-root"):
            i += 1;
            root = sys.argv[i] + "/";
        elif(sys.argv[i] == "-v"):
            i += 1;
            video = sys.argv[i];
        elif(sys.argv[i] == "-q"):
            i += 1;
            qs = (sys.argv[i]);
        else:
            print "Wrong Para";
            exit(-1);
        i += 1;


folder1 = video + "_q" + qs + "/" + video + "_q" + qs + "_1_dec/";
folder2 = video + "_q" + qs + "/" + video + "_q" + qs + "_2_dec/";
right_total = 22 * 18 * 4 * 48;
diag_total = 22 * 18 * 4 * 36;

cal_markov(root + folder1, "+1");
cal_markov(root + folder2, "-1");
