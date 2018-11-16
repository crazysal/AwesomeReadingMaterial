import numpy as np
import math

def ssd(x, y):
    x = x.ravel()
    y = y.ravel()
    difference = x - y
    return np.matmul(difference, np.transpose(difference))

def ncc(x, y):
    x = x.ravel()
    y = y.ravel()
    x = x - np.mean(x)
    y = y - np.mean(y)

    return np.matmul(x, np.transpose(y))/math.sqrt(np.matmul(x, np.transpose(x))*np.matmul(y, np.transpose(y)));


if __name__ == "__main__":
    p1 = np.asarray([[0,0,0],[72,0,84],[170,26,54]])
    p2 = np.asarray([[75,127,52],[87,86,0],[12,188,176]])
    p3 = np.asarray([[3,9,208],[1,2,6],[22,40,9]])
    t = np.asarray([[3,10,20],[18,1,5],[2,30,3]]);

    s1 = ssd(p1, t)
    s2 = ssd(p2, t)
    s3 = ssd(p3, t)
    print("SSD error of pixel 1: {:.3f}".format(s1))
    print("SSD error of pixel 2: {:.3f}".format(s2))
    print("SSD error of pixel 3: {:.3f}".format(s3))
    print("Pixel 3 is the best match, as it has the smallest SSD error.\n")

    n1 = ncc(p1, t)
    n2 = ncc(p2, t)
    n3 = ncc(p3, t)
    print("NCC value of pixel 1: {:.3f}".format(n1))
    print("NCC value of pixel 2: {:.3f}".format(n2))
    print("NCC value of pixel 3: {:.3f}".format(n3))
    print("Pixel 3 is the best match, as it has the largest NCC value.\n")