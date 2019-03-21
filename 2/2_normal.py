import numpy as np 	
import math 

time_step = 1e-4
threshold_distance = 1e-1
gravitational_constant = 6.67e5
iteration = 0

def distance(x1,y1,x2,y2):
	return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
	
mass = np.load('masses.npy')
position = np.load('positions.npy')
velocity = np.load('velocities.npy')
position_i = position.T
velocity_i = velocity.T
position_n = np.empty((position_i.shape[0],position_i.shape[1]))
velocity_n = np.empty((position_i.shape[0],position_i.shape[1]))

def threshold():
	min_distance = 1e18
	for a in xrange(position_i.shape[1]-1):
		for b in xrange(a+1,position_i.shape[1]):
			p1x = position_i[0,a]
			p1y = position_i[1,a]
			p2x = position_i[0,b]
			p2y = position_i[1,b]
			min_distance = min(min_distance,distance(p1x,p1y,p2x,p2y))
	return min_distance

def acceleration(component,particle):
	acc = np.array([[0],[0]], dtype = float)
	for a in xrange(position_i.shape[1]):
		if(a!=particle):
			psx = position_i[0,particle]
			psy = position_i[1,particle]
			pox = position_i[0,a]
			poy = position_i[1,a]
			distance_cube = math.pow(distance(psx,psy,pox,poy),3)
			acc[0]+= mass[a]*(psx-pox)/distance_cube
			acc[1]+= mass[a]*(psy-poy)/distance_cube
	acc[0]*= gravitational_constant*-1
	acc[1]*= gravitational_constant*-1

	if(component==0):
		return acc[0]

	else:
		return acc[1]

while(threshold()>=threshold_distance): 
	print ("Minimum Distance = ", threshold())
	iteration+= 1
	print ("Iteration Number : ", iteration)
	# print("Position x:",position_n[0])
	for a in xrange(position_i.shape[1]):
		position_n[0,a] = position_i[0,a] + velocity_i[0,a]*time_step + acceleration(0,a)*math.pow(time_step,2)/2
		position_n[1,a] = position_i[1,a] + velocity_i[1,a]*time_step + acceleration(1,a)*math.pow(time_step,2)/2
		velocity_n[0,a] = velocity_i[0,a] + acceleration(0,a)*time_step
		velocity_n[1,a] = velocity_i[1,a] + acceleration(1,a)*time_step
	position_i = position_n*1
	velocity_i = velocity_n*1