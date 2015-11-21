import os
import os.path
import sys
import numpy as np
import math
from scipy.fftpack import idct


def calError(root, video, qs):
    #folder = root + "/" + video + "_q" + qs;
    folder = root;
    for parent, dirnames, filenames in os.walk(folder):
        for i in range(0, len(filenames)):
            print parent + "/" + filenames[i];
            file1 = open(parent + "/" + filenames[i], "r");
            output = open(parent + "/" + filenames[i] + "_error", "w");
            line = file1.readline();
            while(line != ""):
                if(line.startswith("Dequan")):
                    dequant = list();
                    for i in range(0, 8):
                        line = file1.readline();
                        temp = line[0:-2].split();
                        dequant.append([float(ii) for ii in temp]);
                    idct_m = np.array(dequant);
                    #print idct;
                    idct_m = idct(idct(idct_m,norm='ortho').T, norm='ortho').T
                    #print idct;
                    q_idct = np.rint(idct_m);
                    for i in range(0, q_idct.shape[0]):
                        for j in range(0, q_idct.shape[1]):
                            if(q_idct[i, j] > 255):
                                q_idct[i, j] = 255;
                            elif(q_idct[i, j] < 0):
                                q_idct[i, j] = 0;
                    #print q_idct;
                    err = idct_m - q_idct;

                    is_trun = False;
                    for i in range(0, err.shape[0]):
                        for j in range(0, err.shape[1]):
                            err[i, j] =  round(err[i, j], 3);
                            if(abs(err[i, j]) > 0.5):
                                #print "yes";
                                is_trun = True;
                    if(is_trun):
                        output.write("Truncate\n");
                    else:
                        output.write("Round\n");
                    for i in range(0, err.shape[0]):
                        for j in range(0, err.shape[1]):
                            #print "%6.3f" % err[i, j] + " ",;
                            output.write("%6.3f" % err[i, j] + " ");
                        output.write("\n");
                        #print;
                line = file1.readline();

            file1.close();
            output.close();
    
def calDiffError(root):
    for parent, dirnames, filenames in os.walk(root):
        for i in range(0, len(filenames)):
            p_parent = parent[:parent.rfind('/') + 1];
            filename1 = parent + "/" + filenames[i];
            times = int(parent[-5]) + 1;
            if(times == 4):
                continue;
            filename2 = parent[:-5] + str(times) + parent[-4:] + "/" + filenames[i];
            result_filename = p_parent + str(times - 1);
            #print result_filename;
            print "1" + filename1;
            print "2" + filename2;
            file1 = open(filename1, "r");
            file2 = open(filename2, "r");
            line = file1.readline();
            line2 = file2.readline();
            t_max = 0;
            r_max = 0;
            t_num = 0;
            r_num = 0;
            unstable = 0;
            t_list = list();
            r_list = list();
            while(line != ""):
                if(line.startswith("Dequan")):
                    dequant = list();
                    for j in range(0, 8):
                        line = file1.readline();
                        temp = line[0:-2].split();
                        dequant.append([float(ii) for ii in temp]);
                    dequant2 = list();
                    for j in range(0, 8):
                        line2 = file2.readline();
                        temp = line2[0:-2].split();
                        dequant2.append([float(ii) for ii in temp]);
                    dequant_m = np.array(dequant);
                    dequant_m2 = np.array(dequant2);
                    if((dequant_m == dequant_m2).all()):
                        continue;
                    #print dequant_m;
                    unstable += 1;
                    idct_m = idct(idct(dequant_m,norm='ortho').T, norm='ortho').T
                    #print idct_m;
                    q_idct = np.rint(idct_m);
                    for j in range(0, q_idct.shape[0]):
                        for k in range(0, q_idct.shape[1]):
                            if(q_idct[j, k] > 255):
                                q_idct[j, k] = 255;
                            elif(q_idct[j, k] < 0):
                                q_idct[j, k] = 0;
                    #print q_idct;
                    err = idct_m - q_idct;

                    is_trun = False;
                    for j in range(0, err.shape[0]):
                        for k in range(0, err.shape[1]):
                            err[j, k] =  abs(round(err[j, k], 3));
                            if(err[j, k] > 0.5):
                                #print "yes";
                                is_trun = True;
                    if(is_trun):
                        t_num += 1;
                        for j in range(0, err.shape[0]):
                            for k in range(0, err.shape[1]):
                                t_list.append(err[j, k]);
                    else:
                        r_num += 1;
                        for j in range(0, err.shape[0]):
                            for k in range(0, err.shape[1]):
                                r_list.append(err[j, k]);

                    '''
                    if(is_trun):
                        output.write("Truncate\n");
                    else:
                        output.write("Round\n");

                    for i in range(0, err.shape[0]):
                        for j in range(0, err.shape[1]):
                            output.write("%6.3f" % err[i, j] + " ");
                        output.write("\n");
                        #print;
                    '''
                line = file1.readline();
                line2 = file2.readline();


            file1.close();
            file2.close();
            output = open(result_filename, "a");
            #"t_max t_num t_mean t_var r_max r_num r_mean r_var\n");
            output.write(filenames[i] + "\n");
            output.write('0' if len(t_list) == 0 else str(round(np.max(t_list), 3)));
            output.write(" " + str(len(t_list) / 64));
            output.write(" " + ('0' if len(t_list) == 0 else str(round(np.mean(t_list), 3))));
            output.write(" " + ('0' if len(t_list) == 0 else str(round(np.var(t_list), 3))));
            output.write(" " + ('0' if len(r_list) == 0 else str(round(np.max(r_list), 3))));
            output.write(" " + str(len(r_list) / 64));
            output.write(" " + ('0' if len(r_list) == 0 else str(round(np.mean(r_list), 3))));
            output.write(" " + ('0' if len(r_list) == 0 else str(round(np.var(r_list), 3))));
            output.write("\n");
            output.close();
    


def calDiffErrorSplit(root):
    for parent, dirnames, filenames in os.walk(root):
        filenames.sort(); 
        frame_t_list = list();
        frame_r_list = list();
        for i in range(0, len(filenames)):
            if(not "_I" in filenames[i]):
                continue;
            p_parent = parent[:parent.rfind('/') + 1];
            filename1 = parent + "/" + filenames[i];
            times = int(parent[-5]) + 1;
            if(times == 4):
                continue;
            filename2 = parent[:-5] + str(times) + parent[-4:] + "/" + filenames[i];
            result_filename = p_parent + str(times - 1) + "-split";
            #print result_filename;
            print "1" + filename1;
            print "2" + filename2;
            file1 = open(filename1, "r");
            file2 = open(filename2, "r");
            line = file1.readline();
            line2 = file2.readline();
            t_max = 0;
            r_max = 0;
            t_num = 0;
            r_num = 0;
            unstable = 0;
            t_list = list();
            r_list = list();
            while(line != ""):
                if(line.startswith("Dequan")):
                    dequant = list();
                    for j in range(0, 8):
                        line = file1.readline();
                        temp = line[0:-2].split();
                        dequant.append([float(ii) for ii in temp]);
                    dequant2 = list();
                    for j in range(0, 8):
                        line2 = file2.readline();
                        temp = line2[0:-2].split();
                        dequant2.append([float(ii) for ii in temp]);
                    dequant_m = np.array(dequant);
                    dequant_m2 = np.array(dequant2);
                    if((dequant_m == dequant_m2).all()):
                        continue;
                    #print dequant_m;
                    unstable += 1;
                    idct_m = idct(idct(dequant_m,norm='ortho').T, norm='ortho').T
                    #print idct_m;
                    q_idct = np.rint(idct_m);
                    for j in range(0, q_idct.shape[0]):
                        for k in range(0, q_idct.shape[1]):
                            if(q_idct[j, k] > 255):
                                q_idct[j, k] = 255;
                            elif(q_idct[j, k] < 0):
                                q_idct[j, k] = 0;
                    #print q_idct;
                    err = idct_m - q_idct;

                    is_trun = False;
                    for j in range(0, err.shape[0]):
                        for k in range(0, err.shape[1]):
                            err[j, k] =  abs(round(err[j, k], 3));
                            if(err[j, k] > 0.5):
                                #print "yes";
                                is_trun = True;
                    if(is_trun):
                        for j in range(0, err.shape[0]):
                            for k in range(0, err.shape[1]):
                                frame_t_list.append(err[j, k]);
                    else:
                        for j in range(0, err.shape[0]):
                            for k in range(0, err.shape[1]):
                                frame_r_list.append(err[j, k]);

                    '''
                    if(is_trun):
                        output.write("Truncate\n");
                    else:
                        output.write("Round\n");

                    for i in range(0, err.shape[0]):
                        for j in range(0, err.shape[1]):
                            output.write("%6.3f" % err[i, j] + " ");
                        output.write("\n");
                        #print;
                    '''
                line = file1.readline();
                line2 = file2.readline();

            if(i % 10 == 9):
                output = open(result_filename, "a");
                output.write('0' if len(frame_t_list) == 0 else str(round(np.max(frame_t_list), 3)));
                output.write(" " + str(len(frame_t_list) / 64));
                output.write(" " + ('0' if len(frame_t_list) == 0 else str(round(np.mean(frame_t_list), 3))));
                output.write(" " + ('0' if len(frame_t_list) == 0 else str(round(np.var(frame_t_list), 3))));
                output.write(" " + ('0' if len(frame_r_list) == 0 else str(round(np.max(frame_r_list), 3))));
                output.write(" " + str(len(frame_r_list) / 64));
                output.write(" " + ('0' if len(frame_r_list) == 0 else str(round(np.mean(frame_r_list), 3))));
                output.write(" " + ('0' if len(frame_r_list) == 0 else str(round(np.var(frame_r_list), 3))));
                output.write("\n");
                output.close();
                frame_r_list = [];
                frame_t_list = [];
           



            file1.close();
            file2.close();
 

#def statistic(root):

    
    
root = "/home/cjy/Desktop/MBStatistic+mv4/";
video = "foreman";
qs = "2";
frames = 100;
type_weight = 2;
if(len(sys.argv) > 2):
    for i in range (1, len(sys.argv)):
        if(sys.argv[i] == "-v"):
            i = i + 1;
            video = sys.argv[i];
        if(sys.argv[i] == "-r"):
            i = i + 1;
            root = sys.argv[i] + "/";
        if(sys.argv[i] == "-q"):
            i = i + 1;
            qs = sys.argv[i];
        if(sys.argv[i] == "-f"):
            i = i + 1;
            frames = int(sys.argv[i]);
else:
    exit(-1);


calDiffErrorSplit(root);

