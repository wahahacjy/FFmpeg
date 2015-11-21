import os;
import sys;
import subprocess;


root = "/media/cjy/mi/MBStatistic-mp4native-gop10/";
type_w = '3';
mv_w = '1';
frames = 100;

i = 1;
while(i < len(sys.argv) - 1):
    if(sys.argv[i] == "-root"):
        root = sys.argv[i + 1].rstrip('/') + '/';
        i += 2;
    elif(sys.argv[i] == "-wt"):
        type_w = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == "-wm"):
        mv_w = sys.argv[i + 1];
        i += 2;
    else:
        print "para wrong";
        exit(-1);

parent, dirnames, filenames = os.walk(root).next();
for folder in dirnames:
    cmd = 'python change_score.py -folder ' + root + folder + '/mbdiff -wt ' + type_w + " -wm " + mv_w + " > " + root + folder + '/mbdiff/diff-score.txt';
    print cmd;
    subprocess.call(cmd, shell=True);
