import json
import re

with open('/home/ojasvini/Desktop/consul1.txt') as oldfile, open('/home/ojasvini/Desktop/new_file.txt', 'w') as newfile:
    for line in oldfile:
        if not line.startswith('#') and not line.startswith('[root'):
            newfile.write(line)


with open('/home/ojasvini/Desktop/new_file.txt') as f:
  data = json.load(f)

filtered_list = ['Checks']
length= len(data)

def service_ID():
	for data1 in data :
		checks_data = data1["Checks"]
		for checks_data1 in checks_data:
			servID = checks_data1["ServiceID"]
			if servID.isdigit() :
				xyz="ServiceID"+":"+ servID
				save_data.append(servID)
save_data=[]

service_ID()
print(save_data)

def vlocation_ID():
	for data1 in data:
		checks_data = data1["Checks"]
		for checks_data1 in checks_data:
			VID = checks_data1["ServiceTags"]
			#print(VID)
			matching = [s for s in VID if "VLocationId" in s]
			#print(matching)
			#return matching
			for match in matching:
				extract= re.search(r"\d+", match)
				number = extract.group(0)
				Number = int(number,10)
				if Number !=0 :
					abc="VLocationID"+":"+number
					save_data1.append(Number)
save_data1=[]
	

vlocation_ID()
print(save_data1)

def Repeat(x): 
	_size = len(x) 
	repeated = [] 
	for i in range(_size): 
		k = i + 1
		for j in range(k, _size): 
			if x[i] == x[j] and x[i] not in repeated: 
				repeated.append(x[i]) 
	return repeated 

repeat_numbers=Repeat(save_data1)


index=[]
size=len(repeat_numbers)
size1=len(save_data1)
for i in range(size1) :
	for j in range(size) :
		if save_data1[i] == repeat_numbers[j] :
			index.append(i)
#print(index)

repeat_ServiceID=[]
for j in range(len(index)):
	repeat_ServiceID.append(save_data[index[j]]) 

print(repeat_ServiceID)

length = len(repeat_ServiceID)
length=int(length/2)

for i in range(length):
	if i%2==0:
		print("ServiceID  "+ (repeat_ServiceID[i])+", "+ (repeat_ServiceID[i+1])+ " for the same VLocationId " +  str(repeat_numbers[i] ))
	
























