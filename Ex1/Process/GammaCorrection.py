
def gamma_correction(img,gamma):
    img = img/(255)
    img = img**(1/gamma)
    return img