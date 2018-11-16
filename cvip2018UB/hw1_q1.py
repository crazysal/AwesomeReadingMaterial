import numpy as np


def Rxz(angle, deg2rad=True):
    if deg2rad:
        angle = np.deg2rad(angle)
    return np.asarray(
        [[np.cos(angle), np.sin(angle), 0],
         [-np.sin(angle), np.cos(angle), 0],
         [0, 0, 1]])

def Ry(angle, deg2rad=True):
    if deg2rad:
        angle = np.deg2rad(angle)
    return np.asarray(
        [[1, 0, 0],
         [0, np.cos(angle), np.sin(angle)],
         [0, -np.sin(angle), np.cos(angle)]])


if __name__ == "__main__":
    alpha = 30
    beta = 50
    gamma = 70

    r_x = Rxz(alpha)
    r_y = Ry(beta)
    r_z = Rxz(gamma)

    # Question 1-1
    r = r_z @ r_y @ r_x
    # print(r_x)
    # print(r_y)
    # print(r_z)
    print("Question 1-1 result:\n{}\n".format(np.matmul(r_z, np.matmul(r_y, r_x))))
    

    # Question 1-2
    pw = np.asarray([600, 300, 200])
    t = -r @ np.asarray([600, 300, 200])
    print("Question 1-2 result:\n{}\n".format(t))

    # Question 1-3
    pc = r @ pw + t
    print("Question 1-3 result:\n{}\n".format(pc))

    # Question 1-4
    K = np.asarray(
        [[100, 0.5, 200],
         [0, 100, 150],
         [0, 0, 1]])
    print("Question 1-4 result:\n{}\n".format(K))

    # # Question 1-5
    p = np.asarray([60, 80, 100])
    pi = K @ p
    print("Question 1-5 result:\n{}\n".format(pi))