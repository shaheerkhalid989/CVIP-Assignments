import cv2
import numpy

# Reading images
img1 = cv2.imread('testing_images/1.jpeg')
img2 = cv2.imread('testing_images/2.jpeg')
img3 = cv2.imread('testing_images/3.jpeg')
img4 = cv2.imread('testing_images/4.jpeg')

# Resizing
resized_1 = cv2.resize(img1 , (250 , 250))
resized_2 = cv2.resize(img2 , (250 , 250))
resized_3 = cv2.resize(img3 , (250 , 250))
resized_4 = cv2.resize(img4 , (250 , 250))

# Vertically stacking
col1 = numpy.vstack([resized_1 , resized_3])
col2 = numpy.vstack([resized_2 , resized_4])

# Combining Horizontally
collage = numpy.hstack([col1 , col2])

cv2.imshow("collage" , collage)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.destroyAllWindows()
