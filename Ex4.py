import matplotlib.pyplot as plt
import numpy as np
import cv2

#plot images
def show_img(img,title,cmap):
    plt.imshow(img,cmap)
    plt.title(title)
    plt.show()

#Load image
def Q_4_a():
    img = plt.imread(r"res/kinova.jpg")
    show_img(img,"Original kinova Image",None)
    return img

#adding gauss noise
def Q_4_b(img):
    mean =0
    sigma = 25
    gauss = np.random.normal(mean,sigma,img.shape)
    noisy = np.clip((img + gauss).astype(np.uint8), 0, 255)
    show_img(noisy,"Gaussian Dirty Image",None)
    return (noisy)

#filter image with gauss filter according to kernel size
def Q_4_c(noisy_img,kernel):
    b, g, r = cv2.split(noisy_img)
    b_filtered = cv2.GaussianBlur(b,kernel,0)
    g_filtered = cv2.GaussianBlur(g,kernel,0)
    r_filtered = cv2.GaussianBlur(r,kernel,0)
    filtered_img = cv2.merge((b_filtered,g_filtered,r_filtered))
    show_img(filtered_img, "Gaussian filtered image with kernel "+str(kernel),None)
    return filtered_img

def calc_RMS(f, f_hat):
    f= cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    f_hat= cv2.cvtColor(f_hat, cv2.COLOR_BGR2GRAY)
    m,n = f.shape
    RMS = np.sqrt((1/(m*n))*(np.sum(((f_hat-f)**2))))
    return RMS

#compare two gauss filtered images with different kernels
def Q_4_c_compare(my_img, filtered_ker_3,filtered_ker_5):
    RMS_ker_3=calc_RMS(my_img,filtered_ker_3)
    RMS_ker_5=calc_RMS(my_img,filtered_ker_5)
    if (RMS_ker_3<RMS_ker_5):
        show_img(filtered_ker_3,"the better filter accordig to RMS is with kernel = 3",None)
    else:
        show_img(filtered_ker_5,"the better filter accordig to RMS is with kernel = 5",None)
    return

#Filter with a median filter
def Q_4_d(noisy_img,size):
    b, g, r = cv2.split(noisy_img)
    b_filtered = cv2.medianBlur(b,size)
    g_filtered = cv2.medianBlur(g,size)
    r_filtered = cv2.medianBlur(r,size)
    filtered_img = cv2.merge((b_filtered,g_filtered,r_filtered))
    show_img(filtered_img,"Median filtered image, filter size "+str(size)+"X"+str(size),None)
    return

#Load image,convert image to gray and show histogram
def Q_4_e():
    img = plt.imread(r"res/dark.jpg")
    show_img(img,"Original Dark Image",None)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_img(gray,"Gray Scale dark Image", cmap='gray')
    hist=cv2.calcHist(gray,[0],None,[256],[0,256])
    plt.plot(hist,color = 'blue')
    plt.xlim([0,256])
    plt.title("dark gray image histogram")
    plt.show()
    return img

#perform Histogram equalization
def Q_4_f(gray):
    img_eq = cv2.equalizeHist(gray)
    show_img(img_eq,"gray image after histogram equalization", cmap='gray')
    return

if __name__ == "__main__":
    my_kinova_img = Q_4_a()
    gauss_noisy_img = Q_4_b(my_kinova_img)
    gauss_filtered_ker_3 =Q_4_c(gauss_noisy_img,(3,3))
    gauss_filtered_ker_5 =Q_4_c(gauss_noisy_img,(5,5))
    Q_4_c_compare(my_kinova_img, gauss_filtered_ker_3,gauss_filtered_ker_5)
    median_filtered = Q_4_d(gauss_noisy_img,3)
    dark_img_gray = Q_4_e()
    Q_4_f(dark_img_gray)
