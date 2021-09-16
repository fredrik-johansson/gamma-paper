from pylab import *

import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc
import matplotlib.pylab as plt

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

data = """
 10     2.2e-5     4.6e-6     5.2e-6       4.1e-6       4.7e-5            3.3e-5          2.6e-7 
 30     6.1e-5     1.2e-5       1.3e-5       8.8e-6       0.00012        9.6e-5         1.8e-6 
 100     0.00035     5.2e-5      5.2e-5       2.9e-5       0.00032       0.00082          8.6e-6 
 300     0.0021     0.00025      0.00038       9.6e-5       0.0011        0.0077          4.0e-5 
 1000     0.029     0.0027      0.0021       0.00073         0.0064       0.13            0.00046 
 3000     0.47     0.042      0.015        0.0064             0.11        1.7               0.0051
 10000     11     1.0      0.20        0.087                   0.95       40                0.082
 30000     184     16      2.3         1.0                     7.1          807                1.0
 100000    3683     266     38         16                      67           nan                     nan
 300000    nan     nan     478        173                     481          nan                     nan
 1000000   nan     nan     nan        nan                     4108            nan           nan
"""

bsdata = """10  1.81e-05
30  3.4e-05
100  9.72e-05
300  0.000303
1000  0.0012
3000  0.00445
10000  0.0211
30000  0.0955
100000  0.492
300000  1.95
1000000  7.901
3000000  30.84"""



ns = []
spouge1 = []
spouge2 = []
stirling1 = []
stirling2 = []
hyper = []
taylor1 = []
taylor2 = []
bss = []
for line in data.splitlines():
    if line.strip():
        n, t1, t2, t3, t4, t5, t6, t7 = line.split()
        ns.append(float(n))
        spouge1.append(float(t1))
        spouge2.append(float(t2))
        stirling1.append(float(t3))
        stirling2.append(float(t4))
        hyper.append(float(t5))
        taylor1.append(float(t6))
        taylor2.append(float(t7))

for line in bsdata.splitlines():
    n, t1 = line.split()
    bss.append(float(t1))

def ploat(x, y, **kwargs):
    #loglog(x, [y[i] / (x[i]**2) for i in range(len(x))], **kwargs)
    loglog(x, y, **kwargs)

#grid(True, color="gray", linewidth=0.25, linestyle=":")

W = 1.5

ploat(ns, spouge1, label="Spouge (first)", color="C1", linewidth=W, linestyle="-.")
ploat(ns, spouge2, label="Spouge (repeated)", color="C1", linewidth=W)
ploat(ns, stirling1, label="Stirling (first)", color="C0", linewidth=W, linestyle="--")
ploat(ns, stirling2, label="Stirling (repeated)", color="C0", linewidth=W)
ploat(ns, taylor1, label="Taylor (first)", color="C2", linestyle=":", linewidth=W)
ploat(ns, taylor2, label="Taylor (repeated)", color="C2", linewidth=W)
ploat(ns, hyper, label="Hypergeometric", color="C3", linewidth=W)
ns.append(3000000.0)
ploat(ns, bss, label="Hypergeometric\n(rational $x = 13/10$)", color="gray", linewidth=W, linestyle=":")



legend()

xlabel("Decimal digits $d$")
ylabel("Time (seconds)")

#show()
# isceral
# scared


fig = plt.gcf()
fig.set_size_inches(6, 5)
tight_layout()

savefig("gammatime.eps")
savefig("gammatime.pdf")
savefig("gammatime-eps-converted-to.pdf")

show()

