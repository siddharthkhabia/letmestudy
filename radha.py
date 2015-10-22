import sched, time
import os
from bs4 import BeautifulSoup
import urllib.request
from function import scoreget
url="https://cricket.yahoo.com/cricket/live-score/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
a=[]
universities=soup.find_all('a')
for university in universities:
   if (university.get('class')==['no-pjax', 'container-link']):
   		temp=(university.get('href'))
   		if "live" in temp:
   			a.append(temp)
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
	#os.system("echo 'clear'") 
    scoreget(a[0])
    sc.enter(20, 1, do_something, (sc,))

s.enter(20, 1, do_something, (s,))
s.run()

	##to print a list line by line without loop : print("\n".join(a))
