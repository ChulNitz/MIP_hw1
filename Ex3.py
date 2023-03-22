from matplotlib import pyplot as plt
import numpy as np
import cv2

fig = plt.figure(figsize=(10, 7))

# Reading the image
img = plt.imread("res/lionking.jpg")
print(np.shape(img))
fig.add_subplot(2, 3, 1)
plt.imshow(img)
plt.title("Original image")

# Converting from RGB to GRAY
I_GRAY = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
fig.add_subplot(2, 3, 2)
plt.imshow(I_GRAY, cmap='gray')
plt.title("Gray image")


# resize
I_GRAY = cv2.resize(I_GRAY, (64, 64))
fig.add_subplot(2, 3, 3)
plt.imshow(I_GRAY, cmap='gray')
plt.title("Resized image")

I_GRAY_80 = I_GRAY.copy()
I_GRAY_80[I_GRAY_80 >= 80] = 255
I_GRAY_80[I_GRAY_80 < 80] = 0
fig.add_subplot(2, 3, 4)
plt.imshow(I_GRAY_80, cmap='gray')
plt.title("Threshold = 80")

I_GRAY_160 = I_GRAY.copy()
I_GRAY_160[I_GRAY_160 >= 160] = 255
I_GRAY_160[I_GRAY_160 < 160] = 0
fig.add_subplot(2, 3, 5)
plt.imshow(I_GRAY_160, cmap='gray')
plt.title("Threshold = 160")

plt.show()
