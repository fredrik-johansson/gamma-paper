from pylab import *
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc
import matplotlib.pylab as plt


from mpmath import *
import pylab
plot = pylab.plot
arange = pylab.arange


rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


#stirt = [float(bernoulli(2*n)/(2*n*(2*n-1))) for n in range(1,100)]
#tayt = [float(c) for c in taylor(rgamma, 0, 100)]
tayt = []
for line in open("/home/fredrik/src/test/gammaser10k.txt").readlines():
    n, c = line.split()
    tayt.append(mpf(c))

stirt = [float(log(abs((bernoulli(2*n)/(2*n*(2*n-1)))),2)) for n in range(1,10000)]
tayt = [float(log(abs(c),2)) for c in tayt]
import math

def coststir(z, p):
    if re(z) < 0:
        z = -z
    cost = 0
    while abs(z) < 0.16 * p:
        z += 1
        cost += 1
    zm = math.log(abs(z), 2)
    for n in range(1,10000):
        cost += 1
        if stirt[n] - (2*n-1)*zm < -p:
            break
    return cost

def costtayl(z, p):
    if re(z) < 0.0:
        z = -z
    cost = 0
    while re(z) > 0.5:
        z -= 1
        cost += 1
    if z == 0.0:
        return cost
    zm = math.log(abs(z), 2)
    for n in range(2,10000):
        cost += 1
        if n * zm + tayt[n] < -p:
            break
    return cost

@memoize
def better(x, p):
    print("better", x)
    if costtayl(x, p) > coststir(x, p):
        return nan
    y = 0.0
    while costtayl(x + 1j*y, p) < coststir(x + 1j*y, p):
        #y += 0.1
        y = max(y*1.01, y+0.01)
    return y

def better2(x, p):
    return better(abs(x), p)

def betterx(p):
    x = 0.0
    while costtayl(x, p) < coststir(x, p):
        x = max(x*1.1, x+0.1)
    return x

xs = arange(-400.5, 400.5+0.1, 1)
ys = [better2(x, 1000) for x in xs]

xs2 = []
ys2 = []
for i in range(len(xs)):
    if isfinite(ys[i]):
        xs2.append(xs[i])
        ys2.append(ys[i])

xs, ys = xs2, ys2

vs = [-y for y in ys]

print(xs)
print(ys)
print(vs)


fill_between(xs, ys, vs, color=(0.96, 0.97, 1.0))

axhline(0, linewidth=0.5, color='gray')
axvline(0, linewidth=0.5, color='gray')

plot(xs, ys, color='C0')
plot(xs, vs, color='C0')

xlabel(r"$\textrm{Re}(z)$")
ylabel(r"$\textrm{Im}(z)$")

fig = plt.gcf()
fig.set_size_inches(5, 3)
tight_layout()

savefig("diamond.eps")
savefig("diamond.pdf")
savefig("diamond-eps-converted-to.pdf")


show()

