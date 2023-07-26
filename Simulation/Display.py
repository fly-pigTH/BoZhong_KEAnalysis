# 用于展示多自由度的运动仿真结果
import roboticstoolbox as rtb
from roboticstoolbox.robot.DHLink import PrismaticDH, RevoluteDH
from spatialmath import *
import numpy as np
import math
import sympy as sp
import random
import matplotlib.pyplot as plt


class Sim():
    def __init__(self): 
        # 整体的运动学模型
        self.rotcoeff = 0.2
        self.coeff = 0
        self.BZRobot = rtb.DHRobot([
            PrismaticDH(a=0, alpha=math.pi/2, theta=math.pi/2, offset=0), # LINK1
                # 平移误差器
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                # 旋转误差器
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
            PrismaticDH(a=0, alpha=math.pi/2, theta=math.pi/2, offset=0),   # LINK2
                # 平移误差器
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                # 旋转误差器
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
            PrismaticDH(a=0, alpha=0, theta=0, offset=0),   # LINK3
                # 平移误差器
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                # 旋转误差器
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
            RevoluteDH(a=0, alpha=0, d=0),  # LINK4
                # 平移误差器
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                PrismaticDH(a=0, alpha=math.pi/2, offset=self.coeff, theta=math.pi/2),
                # 旋转误差器
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
                RevoluteDH(a=0, alpha=math.pi/2, d=self.rotcoeff, offset=math.pi/2),
        ], name="BZRobot")

        # self.BZRobot.plot([1]+[0]*6+[1]+[0]*6+[1]+[0]*6+[0]+[0]*6);
        # TODO: 展示28个自由度



robot = Sim().BZRobot

single_motion = np.linspace(0, 3, num=10)
reverse_array = single_motion[::-1]
single_motion = np.hstack((single_motion, reverse_array))
arm_motion = single_motion*0.3 + 1
coeffList = [1] + [0.2] * 6 + [1] + [0.2] * 6 + [1] + [0.2] * 6 + [0] + [0.2] * 6

a = arm_motion.copy()
for i in range(27):
    if (i % 7) == 6:
        a = np.vstack((a, arm_motion*coeffList[i+1]))
    else:
        a = np.vstack((a, single_motion*coeffList[i+1]))
# print(single_motion_list)
a = a.T
for i in range(2):
    robot.plot(a[5, :], dt=0.1, vellipse=True, loop=False, limits=[-1, 6, -1, 6, 0, 6], jointaxes=True)   # 动画展示

a = input()

plt.close(fig=None)

# Translator
Translator = rtb.DHRobot([
    PrismaticDH(a=0, alpha=math.pi/2, offset=1*0.5, theta=math.pi/2),
    PrismaticDH(a=0, alpha=math.pi/2, offset=1*0.5, theta=math.pi/2),
    PrismaticDH(a=0, alpha=math.pi/2, offset=1*0.5, theta=math.pi/2),
], name="Translator")

single_motion = np.linspace(1, 2, num=50)
reverse_array = single_motion[::-1]
single_motion = np.hstack((single_motion, reverse_array))
motionArr = single_motion

for i in range(2):
    motionArr = np.vstack((motionArr, single_motion))

for i in range(2):
    Translator.plot(motionArr.T, dt=0.1, vellipse=True, loop=False, limits=[-3, 3, -3, 3, 0, 3], eeframe=True, jointaxes=True)   # 动画展示

plt.close(fig=None)

input()

# Rotator
coeff = 1
Rotator = rtb.DHRobot([
    RevoluteDH(a=0, alpha=math.pi/2, d=coeff, offset=math.pi/2),
    RevoluteDH(a=0, alpha=math.pi/2, d=coeff, offset=math.pi/2),
    RevoluteDH(a=0, alpha=math.pi/2, d=coeff, offset=math.pi/2),
], name="Rotator")

single_motion = np.linspace(0, 6, num=50)
reverse_array = single_motion[::-1]
single_motion = np.hstack((single_motion, reverse_array))
motionArr = single_motion
coeffList = [0.2] * 5
for i in range(2):
    motionArr = np.vstack((motionArr, single_motion*coeffList[i+1]))

for i in range(2):
    Rotator.plot(motionArr.T, dt=0.1, vellipse=True, loop=False, limits=[-3, 3, -3, 3, 0, 3], eeframe=True, jointaxes=True)   # 动画展示

plt.close(fig=None)

input()
# 全体机器人
single_motion = np.linspace(0, 3, num=10)
reverse_array = single_motion[::-1]
single_motion = np.hstack((single_motion, reverse_array))
arm_motion = single_motion*0.3 + 1
coeffList = [1] + [0.2] * 6 + [1] + [0.2] * 6 + [1] + [0.2] * 6 + [0] + [0.2] * 6

a = arm_motion.copy()
for i in range(27):
    if (i % 7) == 6:
        a = np.vstack((a, arm_motion*coeffList[i+1]))
    else:
        a = np.vstack((a, single_motion*coeffList[i+1]))
# print(single_motion_list)
a = a.T
for i in range(2):
    robot.plot(a, dt=0.1, vellipse=True, loop=False, limits=[-1, 6, -1, 6, 0, 6], jointaxes=True)   # 动画展示

plt.close(fig=None)