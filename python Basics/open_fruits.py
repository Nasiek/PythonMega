myfile = open("fruits.txt")
content = myfile.read()
myfile.close()
content = content.splitlines()
for i in content:
	print(len(i))


file = open("fruits.txt")
content = file.readlines()
content=[line.strip() for line in content]
file.close()
for i in content:
	print(len(i))
