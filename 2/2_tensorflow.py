import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np 	
import math 

time_step = tf.constant(1e-4, dtype = tf.float64)
threshold_distance = tf.constant(1e-1, dtype = tf.float64) 
gravitational_constant = tf.constant(6.67e5, dtype = tf.float64)
infinite = tf.constant(1e100, dtype = tf.float64)
iteration = 0

mass_p = np.load('masses.npy')
position_p = np.load('positions.npy')
velocity_p = np.load('velocities.npy')

position_px = position_p.T[0]
position_py = position_p.T[1]

velocity_px = velocity_p.T[0]
velocity_py = velocity_p.T[1]

mass = tf.placeholder(tf.float64)
position_x = tf.placeholder(tf.float64)
velocity_x = tf.placeholder(tf.float64)
position_y = tf.placeholder(tf.float64)
velocity_y = tf.placeholder(tf.float64)

with tf.Session() as sess:

	mass_1 = sess.run(mass, feed_dict={mass:mass_p})
	position_x_1 = sess.run(position_x, feed_dict={position_x:position_px})
	position_y_1 = sess.run(position_y, feed_dict={position_y:position_py})
	velocity_x_1 = sess.run(velocity_x, feed_dict={velocity_x:velocity_px})
	velocity_y_1 = sess.run(velocity_y, feed_dict={velocity_y:velocity_py})
	writer = tf.summary.FileWriter('./log9',graph=sess.graph)


	mass = tf.reshape(mass_1,[1,100])
	position_x = tf.reshape(position_x_1,[1,100])
	position_y = tf.reshape(position_y_1,[1,100])
	velocity_x = tf.reshape(velocity_x_1,[1,100])
	velocity_y = tf.reshape(velocity_y_1,[1,100])

	while(2>1):
		
		diff_x = position_x	- (tf.transpose(position_x))
		diff_y = position_y	- (tf.transpose(position_y))
		
		pairwise_distance = tf.sqrt(tf.pow(diff_x,2)+tf.pow(diff_y,2))		
		distance_corrected = tf.matrix_set_diag(pairwise_distance, tf.fill(pairwise_distance.shape[0:-1], infinite))
		distance_corrected_cube = tf.pow(distance_corrected,3)


		acceleration_x = gravitational_constant*tf.reduce_sum(mass*(tf.divide(diff_x,distance_corrected_cube)),1)
		acceleration_y = gravitational_constant*tf.reduce_sum(mass*(tf.divide(diff_y,distance_corrected_cube)),1)
		
		min_distance = tf.reduce_min(distance_corrected)

		position_x+= velocity_x*time_step + 0.5*acceleration_x*tf.square(time_step)
		position_y+= velocity_y*time_step + 0.5*acceleration_y*tf.square(time_step)
		velocity_x+= acceleration_x*time_step
		velocity_y+= acceleration_y*time_step

		
		if(sess.run(min_distance)<sess.run(threshold_distance)):
			np.save('./f_positions.npy',[sess.run(position_x),sess.run(position_y)])
			np.save('./f_velocities.npy',[sess.run(velocity_x),sess.run(velocity_y)])
			break

		print ("Minimum Distance = ", sess.run(min_distance))
		iteration+= 1
		print(iteration)
		
