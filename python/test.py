import scipy
import matplotlib.pyplot as plt
import random
import seaborn as sns

a = [random.randint(0,50) for _ in range (1278)]
b = [random.randint(50,100) for _ in range (1496)]
c = [random.randint(100,200) for _ in range (1190)]
d = [random.randint(200,400) for _ in range (952)]
e = [random.randint(400,800) for _ in range (762)]
f = [random.randint(800,1000) for _ in range (203)]

data = [a,b,c,d,e,f]
print(data)
norm_cdf = scipy.stats.norm.cdf(data)
plt.step(x=data, y=horm_cdf)
plt.show()