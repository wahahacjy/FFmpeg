import os
import os.path
import sys;



def generate(root):
    for parent, dirnames, filenames in os.walk(root):
        for i in range(0, len(filenames)):
            if(filenames[i] == "1-split-nomean"):
                is_single = True;
            elif(filenames[i] == "2-split-nomean"):
                is_single = False;
            else:
                continue;
            print parent + "/" + filenames[i];
            qs = parent[parent.rfind("_q") + 2:];
            out_name = root + "mp2-error-f100-q" + qs + "-svm-nomean";
            print out_name;
            file1 = open(parent + "/" + filenames[i], "r");
            output = open(out_name, "a");
            line = file1.readline();
            while(line != ""):
                features = line.split();
                if(is_single):
                    output.write("+1");
                else:
                    output.write("-1");
                for j in range(1, len(features) + 1):
                    output.write(" " + str(j) + ":" + features[j - 1]);

                output.write("\n");
                line = file1.readline();
            file1.close();
            output.close();


def generateCombine(data, root):
    data_file = open(data, "r");
    line = data_file.readline();
    single_list = list();
    double_list = list();
    times = 0;
    while(line != ""):
        if(not "frame" in line and not "[" in line):
            video = line.strip("\n");
            print video;
            if(video == "stefan"):
                line = data_file.readline();
                continue;
            for q in range(1, 16):
                err_list1 = list();
                err_list2 = list();
                err_file_name_1 = root + "/" + video + "_q" + str(q) + "/1-split-nomean"; 
                err_file_name_2 = root + "/" + video + "_q" + str(q) + "/2-split-nomean"; 
                err_file1 = open(err_file_name_1, "r");
                err_file2 = open(err_file_name_2, "r");
                for err_line in err_file1:
                    single_list.append(err_line.strip("\n"));
                for err_line in err_file2:
                    double_list.append(err_line.strip("\n"));
                err_file1.close();
                err_file2.close();
            #print single_list;
            #print double_list;
        elif("frame" in line):
            qs = int(line.split()[0][1:]);
            if(qs <= 15):
                result_name = root + "/combine-q" + str(qs) + "-f100-svm-nomean";
                output = open(result_name, "a");
                features = data_file.readline()[1:-2].split();
                print video + " " + str(qs) + " ",;
                output.write("+1 ");
                feature_nums = 5;
                for k in range(1, feature_nums + 1):
                    output.write(str(k) + ":" + features[k - 1].strip(",") + " ");
                single = single_list[times].split();
                for k in range(feature_nums + 1, feature_nums + len(single) + 1):
                    output.write(str(k) + ":" + single[k - feature_nums -1] + " ");
                output.write("\n");

                output.write("-1 ");
                for k in range(1, feature_nums + 1):
                    output.write(str(k) + ":" + features[k].strip(",") + " ");
                double = double_list[times].split();
                for k in range(feature_nums + 1, feature_nums + len(double) + 1):
                    output.write(str(k) + ":" + double[k - feature_nums - 1] + " ");
                output.write("\n");

                print features[0:-1];
                print features[1:];
                print single_list[times];
                print double_list[times];
                times += 1;
                output.close();
            else:
                double_list = [];
                single_list = [];
                times = 0;
        line = data_file.readline();


root = "/home/cjy/Desktop/MBStatistic+mv4/";
if(len(sys.argv) > 2):
    for i in range (1, len(sys.argv)):
        if(sys.argv[i] == "-r"):
            i = i + 1;
            root = sys.argv[i] + "/";
else:
    exit(-1);

data = "/media/cjy/mi/MBStatistic-xvid-gop10/data.txt"; 
generateCombine(data, root);
generate(root);
 
