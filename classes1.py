import json
import re

with open('/home/ojasvini/Desktop/consul1.txt') as oldfile, open('/home/ojasvini/Desktop/new_file.txt', 'w') as newfile:
    for line in oldfile:
        if not line.startswith('#') and not line.startswith('[root'):
            newfile.write(line)


with open('/home/ojasvini/Desktop/new_file.txt') as f:
  data = json.load(f)
#print(type(data))
#print(data)

filtered_list = ['Checks']

#print(data[0])
#print(len(data))


length= len(data)

def service_ID():
	for data1 in data :
		checks_data = data1["Checks"]
		#print(checks_data)
		for checks_data1 in checks_data:
			servID = checks_data1["ServiceID"]
			xyz="ServiceID"+":"+ servID
			print(xyz)
			
			
			#save_data.append(xyz)
#save_data=[]

service_ID()
#print(save_data)

def vlocation_ID():
	for data1 in data:
		checks_data = data1["Checks"]
		for checks_data1 in checks_data:
			VID = checks_data1["ServiceTags"]
			print(VID)
			matching = [s for s in VID if "VLocationId" in s]
			print(matching)
			#return matching
			for match in matching:
				extract= re.search(r"\d+", match)
				number = extract.group(0)
				print(number)
			#VLocationId_\s*(-?\d+(?:\.\d+)?)
			#patterns = ["VLocationId"]
			#for pattern in patterns:
				#if re.search(pattern, VID):
					

vlocation_ID()

#def getNumbers(str): 
	#vlocation_ID()
	#array = re.findall(r'[0-9]+', str) 
	#return array 
	#print(array)

	#for match in matching:
		#getNumbers(match)
		#array = getNumbers(match)
		#print(*array)

	#getNumbers()












