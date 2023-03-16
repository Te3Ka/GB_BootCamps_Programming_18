file = open("file.txt", 'r', encoding='utf-8')

list_1 = list()
resultData = list()
for line in file.readlines():
	resultData.append(tuple(line.split('\n')[0].split(';')))

print(resultData)

file.close()