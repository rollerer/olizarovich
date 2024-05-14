import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

with open('settings.txt', 'r') as settings:
    set = [float(i) for i in settings.read().split('\n')]
dat = np.loadtxt('data.txt', dtype=int)

dat = dat*set[0]
num = []
for i in range(len(dat)):
    num.append(i)
time = np.array(num)*set[1]
print(time)
fig, ax = plt.subplots(figsize =(16, 10), dpi=400)
line, = ax.plot(time, dat)
dat_s = []
time_s = []
for i in range(len(dat)):
    if i%10 == 0:
        dat_s.append(dat[i])
        time_s.append(time[i])
dat_s = np.array(dat_s)
ax.scatter(time_s, dat_s, 100,  marker = '.')
ax.set_ylim([0, 3.3])
ax.set_xlim([0, 10])
ax.grid()
ax.grid(which = 'minor',linewidth = 0.3)

t_z = dat.argmax()*set[1]
t_r = len(dat)*set[1] - t_z

line.set_label('U(t)')
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_title("Процесс зарядки и разрядки конденсатора в RC цепи", fontsize=20, verticalalignment='bottom')
ax.set_ylabel("Напряжение, В", fontsize=14)
ax.set_xlabel("Время, с", fontsize=14)
ax.legend(loc="upper right", fontsize=14)

ax.text(2, 1.5, 'Время зарядки = {}c'.format(t_z))
ax.text(2, 1, 'Время разрядки = {}c'.format(t_r))

fig.savefig('graf.png')

