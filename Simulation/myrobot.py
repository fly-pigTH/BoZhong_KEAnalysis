import roboticstoolbox as rtb
from roboticstoolbox.robot.DHLink import PrismaticDH, RevoluteDH
from spatialmath import *
import numpy as np
import math
import time

BZRobot = rtb.DHRobot([
    PrismaticDH(a=0, alpha=math.pi/2, theta=math.pi, offset=1),
    PrismaticDH(a=0, alpha=math.pi/2, theta=math.pi/2, offset=1),
    PrismaticDH(a=0, alpha=0, theta=0, offset=1),
    RevoluteDH(a=0, alpha=0, d=0),
], name="BoZhonRobot")

# for i in range(100):
#     BZRobot.plot([1, 1, 1-i/100, i/100*math.pi*3])
#     if i%30 == 0:
#         time.sleep(0.001)

# for i in range(100):
#     BZRobot.plot([1, 1-i/100, i/100, i/100*math.pi*3])
#     if i%30 == 0:
#         time.sleep(0.001)

# for i in range(100):
#     BZRobot.plot([1-i/100, i/100, 1, i/100*math.pi*3])
#     if i%30 == 0:
#         time.sleep(0.001)

# input()

single_motion = np.linspace(0, 0.1, num=100)
reverse_array = single_motion[::-1]
motion_array = np.hstack((single_motion, reverse_array))
motion_array = np.vstack((motion_array, 0*motion_array, motion_array, motion_array))
motion_array = motion_array.T

# 使用逆运动学求解
# target_point_list = [[i, j, k] for i in [0, 0.5, 1] for j in [0, 0.5, 1] for k in [0, 0.5, 1]]
# target_point = SE3(np.array(target_point_list))
target_point = SE3(np.array([-0.5, 0.5, 0.5]))

kres = BZRobot.fkine([0.222, 0.989, 0, 0])
print(kres)
BZRobot.plot(motion_array, dt=0.01)
# ikres = BZRobot.ikine_LM(target_point)
# print(ikres)
# print(ikres[0])
# print(ikres[1])

# BZRobot.plot(ikres.q, dt=0.1)
input()

