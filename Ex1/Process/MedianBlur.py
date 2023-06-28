import numpy as np

def median_blur(img,ker):
    img1 = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img1[i,j] = np.median(img[i:i+ker,j:j+ker])
    return img1