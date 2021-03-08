import cv2
import numpy as np

def rgb_to_xyz(image):
    
    img = (image.astype(float)/255)
    XYZ_img = np.empty((img.shape[0], img.shape[1], 3), float)
    X = np.empty([img.shape[0],img.shape[1]], dtype = float)
    Y = np.empty([img.shape[0],img.shape[1]], dtype = float)
    Z = np.empty([img.shape[0],img.shape[1]], dtype = float)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            X[i,j] = (0.4124)*(img[i,j][2]) + (0.3576)*(img[i,j][1]) + (0.1805)*(img[i,j][0])
            Y[i,j] = (0.2126)*(img[i,j][2]) + (0.7151)*(img[i,j][1]) + (0.0721)*(img[i,j][0])
            Z[i,j] = (0.0193)*(img[i,j][2]) + (0.1192)*(img[i,j][1]) + (0.9505)*(img[i,j][0])
    
    XYZ_img[...,0] = Z*255
    XYZ_img[...,1] = Y*255
    XYZ_img[...,2] = X*255
    
    return XYZ_img

img = cv2.imread('frog.jpg',1)
XYZImg = rgb_to_xyz(img)
cv2.imwrite('XYZ.jpg',XYZImg)

def xyz_to_rgb(image):
    
    img = (image.astype(float)/255)
    RGB_img = np.empty((img.shape[0], img.shape[1], 3), float)
    r = np.empty([img.shape[0],img.shape[1]], dtype = float)
    g = np.empty([img.shape[0],img.shape[1]], dtype = float)
    b = np.empty([img.shape[0],img.shape[1]], dtype = float)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r[i,j] = (3.2410)*(img[i,j][2]) + (-1.5374)*(img[i,j][1]) + (-0.4986)*(img[i,j][0])
            g[i,j] = (-0.9692)*(img[i,j][2]) + (1.8760)*(img[i,j][1]) + (0.0416)*(img[i,j][0])
            b[i,j] = (0.0556)*(img[i,j][2]) + (-0.2040)*(img[i,j][1]) + (1.0570)*(img[i,j][0])

    RGB_img[...,0] = b*255
    RGB_img[...,1] = g*255
    RGB_img[...,2] = r*255
    
    return RGB_img

RGBImg = xyz_to_rgb(XYZImg)
cv2.imwrite('RGB.jpg',RGBImg)
