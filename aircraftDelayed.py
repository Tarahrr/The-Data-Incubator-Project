

#!/usr/bin/python

f = open('1.csv')
line = f.readline()
Carrier_Name = '"WN"' # AA, AS, CO, DH, DL, MQ, HP, FL, OO, RU, TZ, WN


totalOperation= [0] * 16
totalDelayed = [0] * 16
AVG = [0] * 16
while line:
    words = line.split(',')
    if words[2] == Carrier_Name and words[7] != '' and words[8] != '':
        totalOperation[int(words[0])-2003] += float(words[7])
        totalDelayed[int(words[0])-2003] += float(words[8])
    line = f.readline()

f.close()
counter = 0
while counter < 16:
    if totalOperation[counter] != 0:
        AVG[counter] = float(totalDelayed[counter]) / float(totalOperation[counter])
    counter +=1

counter =0
with open('result.csv', 'a+') as f:
    f.write(Carrier_Name + ",")
    while counter < 16:
        f.write(str(AVG[counter]) + ",")
        counter += 1
    f.write("\n")

f.close()