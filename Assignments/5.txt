import numpy,csv,statistics
with open('per_capita_income.csv','rt') as f:
	data = csv.reader(f)
	data=list(data)
	x=data[1::]
	a=[]
	for i in range(len(x)):
		a.append(float(x[i][1]))
	arr=numpy.array(a)
	y=1000
	c=arr//y
with open('pci.csv','w',newline='') as f:
	data[0].append("Income per Capita (,000)")
	for i in range(len(x)):
		x[i].append(c[i])
	writer = csv.writer(f, delimiter=',')
	writer.writerow(data[0])
	for row in x:
		writer.writerow(row)
	print("New column created!")
	m=statistics.mode(c)
	print("The mode is:",m)
	

	
