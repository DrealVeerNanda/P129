import pandas as pd
import csv


df = pd.read_csv("dwarf_stars.csv", encoding = "utf8")

df = df[df['column_name'].notna()]
df = df.dropna()
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

file_1 = "dwarf_stars.csv"
file_2 = "bright_stars.csv"
#merged_files = "mergedfile.csv"
d1 = []
d2 = []
with open(file_1, 'r', encoding = "utf8") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        d1.append(i)
with open(file_2, 'r', encoding = "utf8") as f:
    csvReader = csv.reader(f)
    for i in csvReader: 
        d2.append(i)
h1 = d1[0]
h2 = d2[0]
pd1 = d1[1:]
pd2 = d2[1:]
h = h1+ h2
p_d = []
for i in pd1:
    p_d.append(i)
for k in pd2:
    p_d.append(k)
with open("mergedfile1.csv", 'w', encoding = "utf8") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(h)
    csvWriter.writerows(p_d)

df = pd.read_csv("mergedfile1.csv",encoding = "utf8")
df.tail(8)

