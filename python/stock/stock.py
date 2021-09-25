import requests 
import json
import time

price = []
name = []
def call(pn=1):
	url = "https://push2.eastmoney.com/api/qt/clist/get?cb=jQuery11230921854548933221_1627040275764&fid=f184&po=1&pz=3000&pn=" + str(pn) +"&np=1&fltt=2&invt=2&fields=f2%2Cf3%2Cf12%2Cf13%2Cf14%2Cf62%2Cf184%2Cf225%2Cf165%2Cf263%2Cf109%2Cf175%2Cf264%2Cf160%2Cf100%2Cf124%2Cf265%2Cf1&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2%2Cm%3A1%2Bt%3A2%2Bf%3A!2%2Cm%3A1%2Bt%3A23%2Bf%3A!2%2Cm%3A0%2Bt%3A7%2Bf%3A!2%2Cm%3A1%2Bt%3A3%2Bf%3A!2"
	# url=str("https://90.push2.eastmoney.com/api/qt/slist/get?cb=jQuery112409544216457056496_1606040506149&pn=%s&pz=200&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f2,f12,f14&_=1606040506150" %pn)
	r=requests.get(url) 
	s=r.text
	data=json.loads(s[len("jQuery11230921854548933221_1627040275764("):-2])["data"]
	print(data)
	for k in data["diff"]:
		price.append({k["f12"]: k["f2"]})
		name.append({k["f12"]: k["f14"]})
	if data["total"] > len(price):
		call(pn + 1)

def save():
	t=time.strftime("%Y%m%d", time.localtime())
	file=str("data/%s.json" %t)
	a=open(file, mode='w')
	a.write(json.dumps(price))
	a.close()

	a = open("name.json", encoding='utf-8', mode='w')
	a.write(json.dumps(name, ensure_ascii=False))
	a.close()

def test():
	call()
	save()

test()