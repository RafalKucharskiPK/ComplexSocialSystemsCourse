import pycxsimulator
from pylab import *

import copy as cp

nr = 500.  # carrying capacity of rabbits

r_init = 100  # initial rabbit population
mr = 0.03     # rabbit movement
dr = 1.0      # death rate of rabbits when facing predators
rr = 0.1      # rabbit reproduction rate

f_init = 30   # initial fox population
mf = 0.05     # fox movement
df = 0.1      # fox death rate without food
rf = 0.5      # fox reproduction rate

w_init = 10   # initial wolf population
mw = 0.08     # wolf movement (faster than foxes)
dw = 0.1      # wolf death rate without food
rw = 0.4      # wolf reproduction rate
w_kill_fox_prob = 0.3  # chance a wolf kills a nearby fox

cd = 0.02     # collision radius
cdsq = cd ** 2

class agent:
    pass

def initialize():
    global agents, rdata, fdata, wdata
    agents = []
    rdata = []
    fdata = []
    wdata = []

    for i in range(r_init + f_init + w_init):
        ag = agent()
        if i < r_init:
            ag.type = 'r'
        elif i < r_init + f_init:
            ag.type = 'f'
        else:
            ag.type = 'w'
        ag.x = random()
        ag.y = random()
        agents.append(ag)

def observe():
    global agents, rdata, fdata, wdata

    subplot(2, 1, 1)
    cla()
    rabbits = [ag for ag in agents if ag.type == 'r']
    foxes = [ag for ag in agents if ag.type == 'f']
    wolves = [ag for ag in agents if ag.type == 'w']

    if rabbits:
        plot([ag.x for ag in rabbits], [ag.y for ag in rabbits], 'b.')
    if foxes:
        plot([ag.x for ag in foxes], [ag.y for ag in foxes], 'ro')
    if wolves:
        plot([ag.x for ag in wolves], [ag.y for ag in wolves], 'ks')

    axis('image')
    axis([0, 1, 0, 1])

    subplot(2, 1, 2)
    cla()
    plot(rdata, label='rabbits')
    plot(fdata, label='foxes')
    plot(wdata, label='wolves')
    legend()

def update_one_agent():
    global agents

    if not agents:
        return

    ag = choice(agents)

    # Movement
    if ag.type == 'r':
        m = mr
    elif ag.type == 'f':
        m = mf
    else:
        m = mw

    ag.x += uniform(-m, m)
    ag.y += uniform(-m, m)
    ag.x = max(0, min(1, ag.x))
    ag.y = max(0, min(1, ag.y))

    # Nearby agents of different type
    neighbors = [nb for nb in agents if nb != ag and (ag.x - nb.x)**2 + (ag.y - nb.y)**2 < cdsq]

    if ag.type == 'r':
        predators = [nb for nb in neighbors if nb.type in ('f', 'w')]
        if predators and random() < dr:
            agents.remove(ag)
            return
        if random() < rr * (1 - sum(1 for x in agents if x.type == 'r') / nr):
            agents.append(cp.copy(ag))

    elif ag.type == 'f':
        rabbits = [nb for nb in neighbors if nb.type == 'r']
        if not rabbits:
            if random() < df:
                agents.remove(ag)
                return
        else:
            if random() < rf:
                agents.append(cp.copy(ag))

        wolves = [...]
        if wolves and random() < ...:
            agents.remove(ag)
            return

    elif ag.type == 'w':
        rabbits = [...]
        if not rabbits:
            if random() < ...:
                agents.remove(ag)
                return
        else:
            if random() < ...:
                agents.append(cp.copy(ag))

def update():
    global agents, rdata, fdata, wdata
    t = 0.
    while t < 1. and agents:
        t += 1. / len(agents)
        update_one_agent()

    rdata.append(sum(1 for x in agents if x.type == 'r'))
    fdata.append(sum(1 for x in agents if x.type == 'f'))
    wdata.append(sum(1 for x in agents if x.type == 'w'))

pycxsimulator.GUI().start(func=[initialize, observe, update])
