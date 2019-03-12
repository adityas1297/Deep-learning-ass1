from PIL import Image
import numpy as np
import random
import math
import os

def rotate(image_path):

    im = Image.open(image_path)
    i=0
    for i in range(0,180,15): 
        rotated_image = im.rotate(i)

    # rotated_image.save(saved_location)
        rotated_image.show()
        print(i)

def translate(img,l,theta):
	a = 1
	b = 0
	c = 0 #left/right (i.e. 5/-5)
	d = 0
	e = 1
	f = 5 #up/down (i.e. 5/-5)
	img = img.transform(img.size, Image.AFFINE, (1, 0, c, 0, 1, f))
	img.show()
	img.save('my1.png')

def translation(img,l,theta,t,color):
	# a = 1
	# b = 0
	# c = 0 #left/right (i.e. 5/-5)
	# d = 0
	# e = 1
	# f = 5 #up/down (i.e. 5/-5)
	# img = img.transform(img.size, Image.AFFINE, (1, 0, c, 0, 1, f))
	# img.show()
	# img.save('my1.png')

	# count=12
	y = random.randrange(math.ceil(-1*(14-(l*math.sin(math.radians(theta)))/2)),math.floor(14-(l*math.sin(math.radians(theta)))/2),1)
	x = random.randrange(math.ceil(-1*(14-(l*math.cos(math.radians(theta)))/2)),math.floor(14-(l*math.cos(math.radians(theta)))/2),1)
	img_new = img.transform(img.size, Image.AFFINE, (1, 0, x, 0, 1, y))
	# img_new.save(str(l)+'_'+str(t)+'_'+str(theta)+'_'+str(color)+'_'+str(count)+'.jpg')
	# img_new.show()


if __name__ == '__main__':
	path = '/home/aditya/6thsem/deeplearning/ass1/images/'
	w, h = 28, 28
	data = np.zeros((h, w, 3), dtype=np.uint8)
	l=15
	theta =15
	t=1
	color=1
	# for i in range(7,23): #when l = 15
	# # for i in range(11,19): #when l=7
	# 	data[14,i] = [255, 0, 0]
	# 	# data[15,i] = [255, 0, 0]
	# 	# data[13,i] = [255, 0, 0]
	# 	# data[14,i] = [0, 0, 255]

	for i in [0,1]: # length
		for j in [0,1]: #Thickness
			for k in range(0,12): #angle
				theta = k*15
				for o in [0,1]: #color
					val1 = [255,0,0]
					val2 = [0,0,255]
					if i==0:	
						l=7
					else:
						l=15
					if o==0:
						val=val1
					else:
						val=val2
					for p in range(14-(l//2),16+(l//2)): 
							data[14,p] = val
					if j==1:
						for p in range(14-(l//2),16+(l//2)): 
							data[13,p] = val
							data[15,p] = val
					img = Image.fromarray(data, 'RGB')
					img = img.rotate(theta)
					new_path = str(i)+'_'+str(j)+'_'+str(k)+'_'+str(o)
					# os.mkdir(path+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(o))
					os.mkdir(path+new_path)
					img.save(path+new_path+'/'+str(i)+'_'+str(j)+'_'+str(k)+'_'+str(o)+'_1.jpg')



					









	# img = Image.fromarray(data, 'RGB')
	# img.save('my.png')
	# img = img.rotate(15)
	# translation(img,l,theta,t,color)
	# img.show()