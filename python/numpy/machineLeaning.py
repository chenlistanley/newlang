import numpy
from scipy import stats

def test():
	a = [99, 86, 81, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 99]
	b = list(a)
	b.sort()
	print(b)
	print(a.index(min(a)), a.index(max(a)))
	print("average", sum(a)/len(a))
	print("average", numpy.mean(a))
	print("the center", numpy.median(a))
	print("std", numpy.std(a))
	print("var", numpy.var(a))
	print("percentile", numpy.percentile(a, 75))
	print(stats.mode(a))

def test2():
	x = numpy.random.uniform(0.0, 5.0, 250)
	plt.hist(x, 5)
	plt.show()

test()