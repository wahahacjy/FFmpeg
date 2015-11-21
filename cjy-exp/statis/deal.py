import os
import sys


input_file = ''
result = '';
i = 1;
while(i < len(sys.argv) - 1): 
    if(sys.argv[i] == '-i'):
        input_file = sys.argv[i + 1];
        i += 2;
    elif(sys.argv[i] == '-o'):
        result = sys.argv[i + 1];
        i += 2;

input1 = open(input_file, "r");
for line in input1:
    if(line.startswith("[")):
        temp = line[1:-2].split(',');
        for num in temp:
            print num,
        print;



