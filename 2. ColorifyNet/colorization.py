### INSPIRED BY - https://github.com/opencv/opencv/blob/master/samples/dnn/colorization.py

#our program will just look at the grey scale of the balck
#and white images and accordingly it will be colorized

import numpy as np
import cv2

#we cant train the models our selves as we dont really have the datasets and hence we make use of already trained models
prototxt_path = 'Models/colorization_deploy_v2.prototxt'
model_path = 'Models/colorization_release_v2.caffemodel'
kernel_path = 'Models/pts_in_hull.npy'
image_path = 'Images/Lion_King.jpg'

#accessing the pretrained neural networks, net is our neural network
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path);
points = np.load(kernel_path)    #loading the points

#next three lines are inspired by the library used and hence the following parameters are passed
#we are basically defining the layers and loading them
points = points.transpose().reshape(2, 313, 1, 1)
net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1,313], 2.606, dtype="float32")]

#LAB colorscheme used where L-> Lightness and A and B are the colorvalues
#here we are converting our RGB scheme into LAB
bw_image = cv2.imread(image_path)
normalized = bw_image.astype("float32")/ 255.0   #normalizing the range from (0 to 255) to (0 to 1)
lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)   #cv2 take the colorscheme as BGR and not RGB

resized = cv2.resize(lab, (224, 224))    #resizing the image to required dimensions of the pretrained model
L = cv2.split(resized)[0]    #index 0 provides the L value
L -= 50 #we can playaround with this mean value and accordingly the results will differ

#acquiring the ab values for the respective L value
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1,2,0))

#since the value acquired is for a resized image we turn it back according to the original black and white image and change the lightness value
ab = cv2.resize(ab, (bw_image.shape[1], bw_image.shape[0]))
L = cv2.split(lab)[0]

#we concatenate the lab scheme and obtain the colorized image, which is later converted into the BGR scheme and
#denormalized so that it can be easily accessed throught cv
colorized = np.concatenate((L[:,:,np.newaxis],ab),axis=2)
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = (255.0 * colorized).astype("uint8")

cv2.imshow("BW Image", bw_image)
cv2.imshow("Colorized", colorized)
cv2.waitKey(0)
cv2.destroyAllWindows()