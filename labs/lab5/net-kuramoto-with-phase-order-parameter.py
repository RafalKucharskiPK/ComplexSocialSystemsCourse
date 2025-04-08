import pycxsimulator
from pylab import *
import networkx as nx

# Initialize global variables
def initialize():
    global g, nextg, r_values, t_values, t
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['theta'] = 2 * pi * random()
        g.nodes[i]['omega'] = 1. + uniform(-0.05, 0.05)
    nextg = g.copy()
    nextg.pos = g.pos

    # initialize time and order parameter tracking
    r_values = []
    t_values = []
    t = 0

# Compute Kuramoto order parameter r(t)
def compute_order_parameter():
    N = len(g.nodes)
    complex_phases = [exp(1j * ...) for i in g.nodes]
    r = abs(sum(...) / ...)
    return r

# Visualize: network, phase circle, and r(t)
def observe():
    global g, r_values, t_values

    subplot(1, 3, 1)
    cla()
    nx.draw(g, cmap=cm.hsv, vmin=-1, vmax=1,
            node_color=[sin(g.nodes[i]['theta']) for i in g.nodes],
            pos=g.pos)
    title("Network view")

    subplot(1, 3, 2)
    cla()
    plot([cos(g.nodes[i]['theta']) for i in g.nodes],
         [sin(g.nodes[i]['theta']) for i in g.nodes], '.')
    axis('image')
    axis([-1.1, 1.1, -1.1, 1.1])
    title("Phase circle")

    subplot(1, 3, 3)
    cla()
    plot(t_values, r_values, '-k')
    xlabel("Time")
    ylabel("r(t)")
    ylim(0, 1)
    title("Order parameter r(t)")

# Kuramoto model parameters
alpha = 1    # coupling strength
Dt = 0.01    # time step

# Update function
def update():
    global g, nextg, r_values, t_values, t

    for i in g.nodes:
        theta_i = g.nodes[i]['theta']
        nextg.nodes[i]['theta'] = theta_i + (g.nodes[i]['omega'] + alpha * (
            sum([sin(g.nodes[j]['theta'] - theta_i) for j in g.neighbors(i)]) / g.degree(i))) * Dt

    # Advance time
    t += Dt

    # Compute and record order parameter
    r = compute_order_parameter()
    r_values.append(r)
    t_values.append(t)

    # Swap graphs
    g, nextg = nextg, g

# Start the simulation GUI
pycxsimulator.GUI().start(func=[initialize, observe, update])
