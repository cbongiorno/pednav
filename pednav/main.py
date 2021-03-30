import pickle as pk
import numpy as np
from collections import defaultdict, Counter
import igraph as ig

np.seterr(divide='ignore', invalid='ignore')

class Navigation:
	def __init__(self,graph_filename):
			'''graph_filename: pickle file with street network'''
			#Load network
			with open(graph_filename,'rb') as handle:
				self.g = pk.load(handle,encoding='latin1')
			
			#Projected Lat,Lon
			self.ppos = np.array(self.g.vs["ppos"])

			#Links weightes
			self.w = np.array(self.g.es["weight"])


			#Create directional Graph for the Vector shortest path
			#edges
			ed = [e.tuple for e in self.g.es]
			#directed edges
			eddir = ed+[(e[1],e[0]) for e in ed]
			#directed street length
			self.wdir = np.concatenate((self.w,self.w))
			
			#directed network
			self.gh = ig.Graph(n=self.g.vcount(),edges=eddir,directed=True)
			self.gh.es["weight"] = self.wdir
			self.frm, self.to = np.array([self.ppos[e[0]] for e in ed]), np.array([self.ppos[e[1]] for e in ed])

		
	def _GA(self,a,b,c):
		'''compute angles'''
		ba = a - b
		bc = c - b
		ang = np.degrees(np.arccos( (ba*bc).sum(axis=1)/(np.linalg.norm(ba,axis=1) * np.linalg.norm(bc,axis=1))) )
		ang[np.isnan(ang)] = 1e-10
		return ang

    
    
	def Stochastic_Vector_Path(self,destination, origins,sigma):
		'''
		INPUT:
		destination: index of destination;
		origins: list of origin for the same destination;
		sigma: stochastic noise parameter.
		
		OUTPUT:
		list of vector stochatistc paths. 
		'''
	
		#computes angle weights for all streets towards the destinations (directed network)
		angles = np.concatenate(  (self._GA(self.frm, self.to, self.ppos[destination][np.newaxis]),(self._GA(self.to, self.frm, self.ppos[destination][np.newaxis])  )))
		
		#compute reweighting of links
		wx = np.exp( np.random.normal( np.log(angles*self.wdir),sigma ))
		
		#get shortest path
		out =  self.gh.get_shortest_paths(destination,origins,weights= wx)
		out = list(map( lambda x: list(reversed(x)), out))

		return out

	def Stochastic_Shortest_Path(self,destination, origins,sigma):
		'''
		INPUT:
		destination: index of destination;
		origins: list of origin for the same destination;
		sigma: stochastic noise parameter.
		
		OUTPUT:
		list of vector stochatistc paths. 
		'''
		
		#compute reweighting of links
		wx = np.exp( np.random.normal( np.log(self.w),sigma ))
		
		#get shortest path		
		out =  self.g.get_shortest_paths(destination,origins,weights= wx)
		out = list(map( lambda x: list(reversed(x)), out))
		return out


