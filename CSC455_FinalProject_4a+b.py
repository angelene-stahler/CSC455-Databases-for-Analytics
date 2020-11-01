file = open("C:\\Users\Angelene\Documents\FinalProject_GeoTable.txt", "a+")
file.write('\n' + 'Unknown' + '| ' 'NULL' + '| ' + '0'+ '|  ' +'0')
file.close


nullEntry = '\n' + 'Unknown' + '| ' 'NULL' + '| ' + '0'+ '|  ' +'0'
with open("C:\\Users\Angelene\Documents\FinalProject_TweetsTable.txt", "r") as file:
    filedata = file.read()
filedata = filedata.replace('NULL', nullEntry)
with open("C:\\Users\Angelene\Documents\FinalProject_TweetsTable.txt", "w") as file:
    file.write(filedata)
