import cv2
import glob
import numpy as np
import os

path = '/home/aditya/6thsem/deeplearning/ass1/images/'



# folders = sorted(os.listdir(path))
# folders = glob.glob(path)
# folders.sort()
# print(folders)
image_list  = []
for i in [0,1]: # length
		for t in [0,1]: #Thickness
			for k in range(0,12): #angle
				# theta = k*15
				for o in [0,1]:
					rel_path = str(i)+'_'+str(t)+'_'+str(k)+'_'+str(o)
					count = 0
					folder_images = []
					for f in glob.glob(path+rel_path+'/*.jpg'):
						
						# print(folder)
						
						if count>=90:
							break
						else:

						# folder_images.append(cv2.imread(f))
							count = count+1
							img = cv2.imread(f)
							folder_images.append(img)
					# frame_array.append(img)
					# horizonal_concat = np.array(frame_array[0])
					for j in range(0,10):
						horizonal_concat1 = np.concatenate((folder_images[(j*9)+0],folder_images[(j*9)+1]), axis=1)
						horizonal_concat2 = np.concatenate((folder_images[(j*9)+3],folder_images[(j*9)+4]), axis=1)
						horizonal_concat3 = np.concatenate((folder_images[(j*9)+6],folder_images[(j*9)+7]), axis=1)
						# for i in range(2,9):
						# 	horizonal_concat = np.concatenate((horizonal_concat,folder_images[(j*9)+i]), axis=1)
						# horizonal_concat =np.reshape(horizonal_concat,(3,3))
						horizonal_concat1 = np.concatenate((horizonal_concat1,folder_images[(j*9)+2]), axis=1)
						horizonal_concat2 = np.concatenate((horizonal_concat2,folder_images[(j*9)+5]), axis=1)
						horizonal_concat3 = np.concatenate((horizonal_concat3,folder_images[(j*9)+8]), axis=1)
						vertical_concat = np.concatenate((horizonal_concat1,horizonal_concat2),axis=0)
						vertical_concat = np.concatenate((vertical_concat,horizonal_concat3),axis=0)
						image_list.append(vertical_concat)




# cv2.waitKey()
print(len(image_list))
# print(len(image_list[0]))
# print(len(image_list[0][0]))
# print(image_list[0][0][0])

fps=2
height, width, layers = (image_list[0].shape)
size = (width,height)
out = cv2.VideoWriter('video1.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(image_list)):
    # writing to a image array
    out.write(image_list[i])
out.release()

