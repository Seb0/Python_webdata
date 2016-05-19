import json
import urllib

input = raw_input('Enter URL: ')
temp = urllib.urlopen(input)
url = temp.read()
info = json.loads(url)

print 'Count: ', len(info['comments'])
summ = 0
for item in range(len(info['comments'])):
    summ += int(info['comments'][item]['count'])
print 'Sum: ', summ
