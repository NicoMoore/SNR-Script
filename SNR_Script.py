import numpy
from sys import argv
script, filename = argv

data = open(filename)

reader = data.readlines()
sattelites = []

#Creates a list of all the sattelites
x = range(len(reader))
for i in x:
	temp_line = reader[i].split(" ")
	if temp_line[0] == "0":
		sattelites.append(temp_line[2])
	else:
		break

print('Would you like to see a list of the sattelites? (y or n)')
user = input()
if user == "y":
	print(sattelites)


y = range(len(sattelites))
sat_org = []
for j in y:
	for i in x:
		if sattelites[j] in reader[i]:
			sat_org.append(reader[i])

#print(sat_org)
z = range(len(sat_org))
# Interating through list of sattelites
for i in y:
	temp2 = reader[i].split(" ")
	a = range(5,len(temp2))
	indeces = []
	# Looking through line to determine indeces where there are data points
	for j in a:
		if temp2[j] != "nan" and temp2[j] != "nan\n":
			indeces.append(j)
	#Using each indece value to create a list of data
	for k in range(len(indeces)):
		SNR_data = []
		#Iterating through each line of the data to find the specific sattelite and its corresponding data point
		for l in z:
			if sattelites[i] in sat_org[l]:
				temp3 = sat_org[l].split(" ")
				SNR_data.append(float(temp3[indeces[k]]))
		print("SNR data from " + sattelites[i] + " at indece " + str(indeces[k]))
		print(SNR_data)
