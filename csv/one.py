import csv
csvfile=open("person.csv",'r',newline=)
obj=csv.reader(csvfile)
for row in obj:
            print(row)