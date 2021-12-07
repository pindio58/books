import numpy as np
def genertes(n):
	states = np.loadtxt('states.txt',delimiter="\n", dtype=str)
	states = list(map(lambda x: x.replace(' ',''),states))
	states = np.array(states)
	return np.random.choice(states,n)

