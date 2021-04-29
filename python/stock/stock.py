import requests 
import json
import time

stock = []
def call(pn=1):
	url=str("https://90.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112409544216457056496_1606040506149&pn=%s&pz=200&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f2,f12&_=1606040506150" %pn)
	r=requests.get(url) 
	s=r.text
	data=json.loads(s[42:-2])["data"]
	print(data)
	for k in data["diff"]:
		stock.append({k["f12"]: k["f2"]})
	if data["total"] > len(stock):
		call(pn + 1)

def save():
	t=time.strftime("%Y%m%d", time.localtime())
	file=str("data/%s.json" %t)
	a=open(file, mode='w')
	a.write(json.dumps(stock))
	a.close()

def test():
	call()
	save()

test()