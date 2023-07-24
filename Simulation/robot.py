import roboticstoolbox as rtb
import sys, os
# puma = rtb.models.DH.Puma560()
# puma.plot([0, 0, 0, 0, 0, 0])
# # os.system('pause')
# input()

# panda = rtb.models.URDF.Panda()
# panda.plot(panda.qz, backend="swift")   # 使用网页进行渲染
# input()


puma = rtb.models.DH.Puma560()
traj = rtb.jtraj(puma.qz, puma.qr, 100)
traj.q.shape
rtb.qplot(traj.q)