from bs4 import BeautifulSoup
import urllib.request
import os

def scoreget(link):
	 
	page = urllib.request.urlopen(link)
	soup = BeautifulSoup(page.read())
	info = soup.find_all('div',class_='match-info')
	tit=""
	m_type=""
	day=""
	ssn=""
	sts=""
	for i in (info[1].contents):
		if ("Tag" in str(type(i))):
			if("match-type" in str(i)):
				m_type=i.contents[0]
				#print(m_type)
			if("match-day" in str(i)):
				day=i.contents[0]+"  "
				#print(day,end='')
			if("session" in str(i)):
				ssn=i.contents[0]
				#os.system("clear")
				ssn=ssn+"  "				
				#print(ssn,end='')
			if("status" in str(i)):
				sts="( "+i.contents[0]+" )"
				#print(sts)
	tit=tit+"'"+day
	tit=tit+ssn
	tit=tit+sts
	tit=tit+"' "
	#print (tit)
				
	team_name=""
	score=""
	team = soup.find('div',class_=['tm-scr']).find('span',class_=['name'])
	k=str(type(team))
	if ("bs4" in k):
		team_name=(team.contents)[0]
		#print(team_name)
	sc_ext = soup.find('div',class_=['tm-scr']).find('span',class_=['scr'])
	k=str(type(sc_ext))
	if ("bs4" in k):
		score=(sc_ext.contents)[0]
		#print(team_name+" : "+score,end='')
	#print(str((soup.find('div',class_='ings-overs').contents)[0]))
	con=repr(team_name+" : "+score+"\n"+str((soup.find('div',class_='ings-overs').contents)[0]))
	#con="'"+con+"'"
	#print(tit+" "+con)
	os.system('notify-send '+tit+" "+con)