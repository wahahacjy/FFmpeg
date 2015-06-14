import os
import sys

def cal_D(folder1, folder2):
    result = list();
    for parent, dirnames, filenames in os.walk(folder1):
        i = 0;
        count = 0;
        filenames.sort();
        for filename in filenames:
            if("I" in filename):
                print filename;
                i += 1;
                file1 = open(folder1 + "/" + filename, "r");
                file2 = open(folder2 + "/" + filename, "r");
                line1 = file1.readline();
                line2 = file2.readline();
                while(line1 != ''):
                    if(not ("Quantized") in line1):
                        line1 = file1.readline();
                        continue;
                    while(not ("Quantized") in line2):
                        line2 = file2.readline();
                    for j in range(0, 6):
                        tmp1 = file1.readline();
                        tmp2 = file2.readline();
                        if(tmp1 != tmp2):
                            array1 = tmp1[0:-2].split(';');
                            array2 = tmp2[0:-2].split(';');
                            for k in range(0, len(array1)):
                                coeff1 = array1[k].split();
                                coeff2 = array2[k].split();
                                print coeff1;
                                print coeff2;

                                if(coeff1 != coeff2):
                                    for l in range(0, 8):
                                        if(coeff1[l] != coeff2[l]):
                                            count+=1;
                            print count;

                    line1 = file1.readline();
                    line2 = file2.readline();
                file1.close();
                file2.close();
                if(i % 10 == 0):
                    result.append(count);
                    count = 0;
    return result;


folder1 = sys.argv[1];
folder2 = sys.argv[2];
print cal_D(folder1, folder2);
