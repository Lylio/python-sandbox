
# coding: utf-8

# In[1]:


import cv2


# In[4]:


img_gray = cv2.imread("smallgray.png", 0)
img_gray


# In[6]:


img_colour = cv2.imread("smallcolour.png", 1)
img_colour


# In[8]:


print(img_colour)


# In[3]:


import numpy
import cv2
newImage = numpy.array([[101,28,3,49], [101,28,3,49], [101,28,3,49]])
cv2.imwrite("newgray.png", newImage)


# In[2]:


import numpy
import cv2
newImage2 = numpy.array([[0,0,0,0], [0,0,0,0], [0,0,0,0]])

cv2.imwrite("newgray2.png", newImage2)

