import csv,statistics
with open('per_capita_income.csv','rt') as f:
	data = csv.reader(f)
	data=list(data)
	x=[]
	for i in range(1,len(data)):
		x.append(float(data[i][1]))
	avg=statistics.mean(x)
	print("The average is:",avg)
	
