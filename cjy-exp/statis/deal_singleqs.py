import os
import sys


input_file = ''
result = '';
i = 1;
qs = '1';
while(i < len(sys.argv) - 1): 
    if(sys.argv[i] == '-i'):
        input_file = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == '-o'):
        result = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == '-q'):
        qs = sys.argv[i + 1];
        i += 2;

input1 = open(input_file, "r");
line = input1.readline()
while(line != ""):
    if(line.startswith("q" + qs + " ")):
        line = input1.readline()
        print line[1:-2];

    line = input1.readline()



