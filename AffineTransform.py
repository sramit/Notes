import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def affineTransform(image:str, pt1:list, pt2:list):
    '''
    Preserves: points, straight lines and planes, parallel lines,
    ratio of distances between the points lying on same straight line.

    Not Preserved: angle between lines, distance between lines
         
    '''
    img = cv2.imread(image)
    #img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    rows, cols, channel = img.shape

    point1 = np.float32(pt1)
    point2 = np.float32(pt2)

    matrix = cv2.getAffineTransform(point1, point2)
    new_image = cv2.warpAffine(img, matrix, (cols, rows))
    
    #plot results
    plt.subplot(121)
    plt.imshow(img)
    plt.title("InputImage")
    plt.subplot(122)
    plt.imshow(new_image)
    plt.title("OutputImage")
    plt.show()

def main():
    dirname = os.path.dirname(__file__)
    image= 'provide image name'
    image_path = os.path.join(dirname, image)
    
    pt1 = [[50,100], [100, 200], [150, 250]]
    pt2 = [[100, 200], [200, 400], [300, 500]]
    affineTransform(image_path, pt1, pt2)

if __name__=="__main__":
    main()