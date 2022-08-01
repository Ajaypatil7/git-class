import csv
with open("C:\\Users\\Admin\\Desktop\\SampleCSV.csv" ,'r') as fobj:
    csvreader = csv.reader(fobj)
    fields=csvreader.__next__()
    rows=[]
    print(fields)
    for row in csvreader:
        rows.append(row)
    print("Total rows :", csvreader.line_num)

#if we want to print the first 10 rows.
print(rows[:10])c