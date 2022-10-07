import random

file="gua.txt"
mapList={}
gua = ['乾', '兑', '离', '震', '巽', '坎', '艮', '坤']

def init():
	print(gua)
	for k in gua:
		for v in gua:
			mapList.update({str("下%s上%s" %(k, v)):[]})

def read():
	threeLines=[]
	with open(file, mode='r', encoding="utf-8") as f:
		for line in f:
			threeLines.append(line)
			if(len(threeLines) == 3):
				for key in mapList:
					if key in line:
						mapList.update({key:threeLines})
				threeLines = []

def result(a, b):
	a=mapList.get("下%s上%s" %(b, a))
	for k in a:
		print(k)

def test():
	s = input("请输入上卦:").strip()
	s1 = input("请输入下卦:").strip()
	if s == "" and s1 == "":
		print(gua)
	elif s == "":
		for k in gua:
			result(k, s1)
	elif s1 == "":
		for k in gua:
			result(s, k)
	else:
		result(s, s1)

init()
read()
test()