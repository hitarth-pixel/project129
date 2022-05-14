import csv

dataset1=[]
dataset2=[]
with open("dwarf_stars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader: dataset1.append(row)

with open("bright_stars.csv","r") as f:
    csvreader2=csv.reader(f)
    for row in csvreader2:dataset2.append(row)

planet_data_1=dataset1[1:]
planet_data_2=dataset2[1:]

headers1=dataset1[0]
header2=dataset2[0]

headers=headers1+header2
planet_data=[]
#print(planet_data_1)
for index, data_row in enumerate(planet_data_1): planet_data.append(data_row)

    #print(data_row)
   
    
# planet_data.append(planet_data_1,planet_data_2)
with open("newdata.csv","a+") as f:
   csvwriter=csv.writer(f)
   csvwriter.writerow(headers1)
   csvwriter.writerow(planet_data)
