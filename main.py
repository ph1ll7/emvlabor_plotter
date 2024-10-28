import math
import matplotlib.pyplot as plt

def toDB(x):
  20 * math.log10(x/10)
  
f = [100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,1500000,2000000,5000000,10000000,15000000,20000000,50000000,100000000]
gegen = []
gleich = []

TYPE = "LOG"

if TYPE=="LOG":
  for x in range(len(gegen):
      gegen = map(toDB,gegen)
      gleich = map(toDB,gleich)

fig = plt.figure()

ax = fig.add_subplot(211)
plt.xscale("log")
ax.set_xlabel("Frequenz [Hz]")
ax.set_ylabel("Ausgangsspannung")
ax.set_title("Vermessung Gleichtaktdrossel")
ax.grid(True,'both')

# uncomment following lines for -3dB reference line for analyzing bandwidth
# only paplable with TYPE "LOG"
#grenze = [gegen[0]-3]*21
#ax.plot(f,grenze)

ax.plot(f,gegen,label="Gegentaktsignal")
ax.plot(f,gleich,label="Gleichtaktsignal")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=2)
plt.show()
