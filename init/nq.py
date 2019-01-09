import csv
import sys
with open('NQ.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data=list(csv.reader(csvfile))
    lengthList = len(data)
    outputList = []
    outputList.append(data[0])
    print(len(data))
    rownum = 2
    while rownum < lengthList:
        if(data[rownum][0]!=data[rownum-1][0]):
            outputList.append(data[rownum])
        rownum+=1
print(outputList[3])
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(outputList)