import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
  data = mysock.recv(512)
  if (len(data)<1):
    break
  print data
mysock.close()


#way easier with urllib
import urllib
fh = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fh:
    print line.strip()

counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts
