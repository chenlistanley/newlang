import numpy
from scipy import stats

def test():
	a = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
	print("mean", numpy.mean(a), sum(a)/len(a))
	print("median", numpy.median(a))
	print("std", numpy.std(a))
	print("var", numpy.var(a))
	print("percentile", numpy.percentile(a, 75))
	print(stats.mode(a))

def test():
	x = numpy.random.uniform(0.0, 5.0, 250)
	plt.hist(x, 5)
	plt.show()
