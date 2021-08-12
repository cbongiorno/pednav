# PEDNAV ####################

PEDNAV is a python3 library for the stochastic vector-based navigation and stochastic shortest path navigation.


## INSTALLATION ########

Typical installations time: <10sec

On Linux: sudo pip3 install pednav

On Windows: pip3 install pednav

Requirements:

numpy>=1.14.2
python-igraph>=0.8.0

## DATA ###################

data/graph_clusters_30m_bos.pk: 
It is a pickle igraph object with the pedestrian street network for Boston.
g.vs["pos"] contains the lat,lon of the street intersections
g.vs["ppos"] contains the projected lat,lon of the street intersection
g.ws["weights"] contains the length in meters of the street
  
data/graph_clusters_30m_sf.pk: 
It is a pickle igraph object with the pedestrian street network for San Francisco.


data/Human_Paths_bos.pk:
It is a pickle of a dictionary containing a sample of the pedestrian paths for Boston.
The keys are the path IDs, the values are the sequence of index intersections of the path.
The index intersections are matched with graph_clusters_30m_bos.pk


## EXAMPLE ############

```import pednav
import pickle as pk

#####initialize the module with the street network
nav = pednav.Navigation('data/graph_clusters_30m_bos.pk')

#####noise parameter
sigma = 0.7

#####Load pedestrian paths
with open('data/Human_Paths_bos.pk','rb') as handle:

	H = pk.load(handle)
	
#####Select one human path	
path0 = list(H.values())[0]
origin,destination = path0[0], path0[-1]

print('Real Pedestrian Path:')

print(path0)

print('Stochastic Vector Path:')

print(nav.Stochastic_Vector_Path(destination,[origin],sigma)[0])

print('Stochastic Shortest Path:')

print(nav.Stochastic_Shortest_Path(destination,[origin],sigma)[0]) '''
