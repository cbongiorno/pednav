##################PEDNAV ####################

PEDNAV is a python3 library for the stochastic vector-based navigation and stochastic shortest path navigation.




###### INSTALLATION ########

Typical installations time: <10sec

On Linux: sudo pip3 install pednav

On Windows: pip3 install pednav

Requirements:

numpy>=1.14.2
python-igraph>=0.8.0

##### DATA ###################


DATA/graph_clusters_30m_bos.pk: 
It is a pickle igraph object with the pedestrian street network for Boston.
g.vs["pos"] contains the lat,lon of the street intersections
g.vs["ppos"] contains the projected lat,lon of the street intersection
g.ws["weights"] contains the length in meters of the street
  
DATA/graph_clusters_30m_sf.pk: 
It is a pickle igraph object with the pedestrian street network for San Francisco.


DATA/Human_Paths_bos.pk:
It is a pickle of a dictionary containing a sample of the pedestrian paths for Boston.
The keys are the path IDs, the values are the sequence of index intersections of the path.
The index intersections are matched with graph_clusters_30m_bos.pk

###### CODE #####################

PKG/pednav/main.py contains the code

It contains the functions for the stochastic vector-based navigation and  stochastic shortest path navigation.


##### EXAMPLE ############

test.py:  It contains an example on a small sample of trajectories

Expected output:

Running time: <100ms

Real Pedestrian Path:
[13909, 3454, 6340, 13572, 6279, 6280, 64849]
Stochastic Vector Path:
[13909, 3454, 6340, 13572, 6279, 6280, 64849]
Stochastic Shortest Path:
[13909, 62854, 3454, 6340, 13572, 6279, 6280, 64849]

Where numbers between brackets correspond to road intersection indexes as reported in the file graph_clusters_30m_bos.pk

Notice that the outcome of the code is stochastic, so the one reported above is only an example of a possible outcome.# pednav
