
import pdfkit
import requests
import bs4
import os
#change path to whatever you want, its where all the pdfs will be saved
path = "/Shield Hero"
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)
    os.chdir(path)
    print(os.getcwd())

res = requests.get('https://ohanashimi.wordpress.com/tate-no-yuusha/')
res.raise_for_status()
pdfthing = bs4.BeautifulSoup(res.text)
elems = pdfthing.select('a')
#these are 15 and 401 because thats where 
#the links for the chapters begin in the list of html <a> tags
startChapter = 15 
endChapter = 401
Shield = "Shield Hero "
chapter = 'Chapter'
chapterNum = 1;
pdf = '.pdf'
while(startChapter <= endChapter):
	chapterName = Shield + chapter + " " +str(chapterNum) + pdf
	print(elems[i].get('href'), " " ,i," ",chapterName)
	pdfkit.from_url(elems[i].get('href'),chapterName)
	i += 1
	chapterNum += 1
