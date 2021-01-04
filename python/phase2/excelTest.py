import xlrd
from datetime import date, datetime, timedelta

def test():
	workbook = xlrd.open_workbook("test.xls")
	sheet = workbook.sheet_by_index(0)
	print("%s %s %s" %(sheet.name, sheet.nrows, sheet.ncols))
	for row in range(sheet.nrows):
		for col in range(sheet.ncols):
			cell = sheet.cell(row, col)
			if cell.ctype == 3:
				date_value = xlrd.xldate_as_tuple(cell.value, workbook.datemode)
				print(date(*date_value[:3]))
				if date(*date_value[:3]) == (datetime.now().date() + timedelta(days=-30)):
					print("ok")
			else:
				print(cell.value)




test()