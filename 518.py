import requests
from bs4 import BeautifulSoup
import lxml
import re

p = 1
dt_URL = []
while True:
	URL = "https://www.518.com.tw/job-index-P-"+str(p)+".html?i=1&am=1&ad=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E5%B8%AB&xq=1"  ##搜尋頁網址
	res = requests.get(URL)
	soup = BeautifulSoup(res.text,'lxml')
	page = soup.select('.pagecountnum')   ##搜尋共有幾頁
	num = (int)(page[0].text.split('/ ')[1].split('頁')[0])
	if res.status_code == 200:			#連線成功
		p_dt = soup.select('.title > a')	
		for al in p_dt:
			if re.compile(r'職缺名：').match(al['title']):
				dt_URL.append(al['href'])
		p += 1
		# page = soup.select('#linkpageTop')
		if p > num:
			break

kw = {}
kw["C"] = 0               
kw["C++"] = 0
kw["C#"] = 0
kw["C#.NET"] = 0
kw["PYTHON"] = 0
kw["JAVA"] = 0
kw["JAVASCRIPT"] = 0
kw["JSP"] = 0
kw["PHP"] = 0
kw["HTML"] = 0
kw["MYSQL"] = 0
kw["MS SQL"] = 0
kw["CSS"] = 0
kw["R"] = 0
kw["CSS"] = 0
kw["RUBY"] = 0
kw["PERL"] = 0
kw["SWIFT"] = 0
kw["DELPHI"] = 0
kw["JQUERY"] = 0
kw["SPSS"] = 0
kw['VISUAL STUDIO'] = 0
kw["ANGULARJS"] = 0
kw["IIS"] = 0
kw["ORACLE"] = 0
kw["AJAX"] = 0
kw["LINUX"] = 0
kw["DREAMWEAVER"] = 0
n = 0
length = len(dt_URL)
print(length)
while True:
	if n > length-1:
		break
	res = requests.get(dt_URL[n])
	print(n)
	soup = BeautifulSoup(res.text ,"lxml")
	line1 =soup.select(".JobDescription > p")
	line2 =soup.select('.job-detail-box')[2].select('dd')
	line = line1 + line2
	
	list = []
	for xx in line:	
		word = re.findall('[a-zA-z]+[\#\+\-\sa-zA-Z]*',xx.text)
		for words in word: 
			if words.upper() not in list:
				list.append(words.upper())
	for keyword in list:
		if keyword in kw:
			kw[keyword] += 1 
	n += 1
print(sorted(kw.items(), key=lambda x: x[1], reverse=True))