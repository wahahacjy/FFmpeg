import sys
import os


#Get all the video names and qs in dirnames
def count_videos(dirnames):
    video_set = set();
    bt_set = set();
    for i in range(0, len(dirnames)):
        if('data' in dirnames[i]):
            continue;
        elif('_' in dirnames[i]):
            video_set.add(dirnames[i][0:dirnames[i].index('_')]);
            bt_set.add(dirnames[i][dirnames[i].index('_b') + 2:]);
    bt_list = list(bt_set);
    bt_list.sort();
    video_list = list(video_set);
    video_list.sort();
    return video_list,bt_list;
    

#count the p frames of one video
def count_p_frame_number(root, video, bt):
    temp = video + "_b" + bt;
    folder = root + "/" + temp + "/" + temp + "_1_dec";
    parent, dirnames, filenames = os.walk(folder).next();
    count = 0;
    for filename in filenames:
        if("_P" in filename):
            count += 1;
    return count;

root = '/media/cjy/Exp/MBStatistic';
size = 352 * 288 / 64
p_frames = 270;
if(len(sys.argv) > 1):
    i = 1;
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-root"):
            i += 1;
            root = sys.argv[i];
        elif(sys.argv[i] == "-pf"):
            i += 1;
            p_frames = int(sys.argv[i]);
        else:
            print "Wrong Para";
            exit(-1);
        i += 1;
for parent, dirnames, filenames in os.walk(root):
    video_list, bt_list = count_videos(dirnames);
    break;

for video in video_list:
    print video;
    for bt in bt_list:
        #only calculate the P-frames
        #frame_number = count_p_frame_number(root, video, bt);
        data_list = list();
        filename = root + "/" + video + "_b" + bt + "/mbdiff/diff.txt";
        data = open(filename);
        times = 1;
        for line in data:
            #line = line.strip('\n');
            if("P-mb" in line):
                diff = line[line.index("=") + 2: -1];
                if(diff == ''):
                    break;
                diff_in_seg = diff.split(',');
                if(times == 1):
                    for i in range(0, len(diff_in_seg)):
                        data_list.append(list());
                index = 0;
                for dif in diff_in_seg:
                    diff_per_frame = "%.2f" %  (float(dif) / (p_frames));
                    data_list[index].append(float(diff_per_frame));
                    index += 1;
                times += 1;
        for result in data_list:
            print "bitrate: " + bt + " frame: " + str(p_frames);
            print result;

