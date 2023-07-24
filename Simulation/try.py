# animation
import roboticstoolbox as rtb
from roboticstoolbox.robot.DHLink import PrismaticDH, RevoluteDH
from spatialmath import *
import numpy as np
import math

# 标准的运动学模型
BZRobot = rtb.DHRobot([
    PrismaticDH(a=0, alpha=math.pi/2, theta=math.pi, offset=0),
    PrismaticDH(a=0, alpha=math.pi/2, theta=math.pi/2, offset=0),
    PrismaticDH(a=0, alpha=0, theta=0, offset=0),
    RevoluteDH(a=0, alpha=0, d=0),
], name="BoZhonRobot")

# animation
single_motion = np.linspace(0, 1, num=100)
reverse_array = single_motion[::-1]
motion_array = np.hstack((single_motion, reverse_array))
motion_array = np.vstack((motion_array, 0*motion_array, motion_array, motion_array))
motion_array = motion_array.T
motion_array


BZRobot.plot(motion_array, dt=0.1)

input()