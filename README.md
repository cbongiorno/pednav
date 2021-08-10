# PEDNAV ####################

PEDNAV is a python3 library for the stochastic vector-based navigation and stochastic shortest path navigation.


## INSTALLATION ########

Typical installations time: <10sec

On Linux: sudo pip3 install pednav

On Windows: pip3 install pednav

Requirements:

numpy>=1.14.2
python-igraph>=0.8.0

## EXAMPLE ############

import pednav
import pickle as pk

#initialize the module with the street network
nav = pednav.Navigation('DATA/graph_clusters_30m_bos.pk')

#noise parameter
sigma = 0.7

#Load pedestrian paths
with open('DATA/Human_Paths_bos.pk','rb') as handle:
	H = pk.load(handle)
	
#Select one human path	
path0 = list(H.values())[0]
origin,destination = path0[0], path0[-1]

print('Real Pedestrian Path:')
print(path0)
print('Stochastic Vector Path:')
print(nav.Stochastic_Vector_Path(destination,[origin],sigma)[0])
print('Stochastic Shortest Path:')
print(nav.Stochastic_Shortest_Path(destination,[origin],sigma)[0]) 
