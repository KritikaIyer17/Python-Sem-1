import csv
with open('per_capita_income.csv','rt') as f:
	data = csv.reader(f)
	data=list(data)
	x=data[1::]
	sortedlist=sorted(x,key=lambda row: float (row[1]) , reverse=True)
with open('sorted.csv','w') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow(data[0])
	for row in sortedlist:
		writer.writerow(row)
print("File has been sorted")
