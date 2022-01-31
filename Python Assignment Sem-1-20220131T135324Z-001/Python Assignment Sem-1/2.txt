import csv
with open('per_capita_income.csv','rt')as f:
	data = csv.reader(f)
	data=list(data)
	fr=data[1:6]
	l=len(data)
	lr=data[l:l-6:-1]
	print("First Five-")
	for i in fr:
		print(i)
	print("Last Five-")
	for i in lr:
		print(i)
	
