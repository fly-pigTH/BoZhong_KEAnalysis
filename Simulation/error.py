# 导入库
import sympy as sp

# 代求量——齐次变换矩阵
T_1__0 = sp.symbols("T_1^0")
T_2__1 = sp.symbols("T_2^1")
T_3__2 = sp.symbols("T_3^2")
T_4__3 = sp.symbols("T_4^3")

# 拖板误差量——平移和旋转
e_x1, e_y1, e_z1 = sp.symbols("\epsilon_x1 \epsilon_y1 \epsilon_z1")
e_x2, e_y2, e_z2 = sp.symbols("\epsilon_x2 \epsilon_y2 \epsilon_z2")
e_x3, e_y3, e_z3 = sp.symbols("\epsilon_x3 \epsilon_y3 \epsilon_z3")
e_x4, e_y4, e_z4 = sp.symbols("\epsilon_x4 \epsilon_y4 \epsilon_z4")

d_x1, d_y1, d_z1 = sp.symbols("\delta_x1 \delta_y1 \delta_z1")
d_x2, d_y2, d_z2 = sp.symbols("\delta_x2 \delta_y2 \delta_z2")
d_x3, d_y3, d_z3 = sp.symbols("\delta_x3 \delta_y3 \delta_z3")
d_x4, d_y4, d_z4 = sp.symbols("\delta_x4 \delta_y4 \delta_z4")

a1, b1, c1 = sp.symbols("a1 b1 c1")   # 位移量，应该是DH参数给出的
a2, b2, c2 = sp.symbols("a2 b2 c2")
a3, b3, c3 = sp.symbols("a3 b3 c3")

t_x, t_y, t_z = sp.symbols("theta_x theta_y theta_z")

# 齐次变换矩阵
T_1__0 = sp.Matrix([
    [1, -e_z1, e_y1, a1+d_x1],
    [e_z1, 1, -e_x1, b1+d_y1],
    [-e_y1, e_x1, 1, c1+d_z1],
    [0, 0, 0, 1]
])
T_2__1 = sp.Matrix([
    [1, -e_z2, e_y2, a2+d_x2],
    [e_z2, 1, -e_x2, b2+d_y2],
    [-e_y2, e_x2, 1, c2+d_z2],
    [0, 0, 0, 1]
])
T_3__2 = sp.Matrix([
    [1, -e_z3, e_y3, a3+d_x3],
    [e_z3, 1, -e_x3, b3+d_y3],
    [-e_y3, e_x3, 1, c3+d_z3],
    [0, 0, 0, 1]
])
T_4__3 = sp.Matrix([
    [sp.cos(t_z), -sp.sin(t_z), e_y4, d_x4],
    [sp.sin(t_z), sp.cos(t_z), -e_x4, d_y4],
    [e_x4*sp.sin(t_z)-e_y4*sp.cos(t_z), e_x4*sp.cos(t_z)+e_y4*sp.sin(t_z), 1, d_z4],
    [0, 0, 0, 1]
])

T_4__0 = T_1__0 * T_2__1 * T_3__2 * T_4__3
T_4__0 = T_4__0.expand()

# 忽略所有高阶小量
print("# 忽略所有高阶小量")
high_group = []
ex_list = [e_x1, e_x2, e_x3, e_x4]
ey_list = [e_y1, e_y2, e_y3, e_y4]
ez_list = [e_z1, e_z2, e_z3, e_z4]
d_list = [d_x1, d_x2, d_x3, d_x4, d_y1, d_y2, d_y3, d_y4, d_z1, d_z2, d_z3, d_z4]
ed_list = ex_list + ey_list + ez_list + d_list
for i in range(len(ed_list)):
    for j in range(len(ed_list)):
        high_group.append((ed_list[i]*ed_list[j], 0))
T_4__0 = T_4__0.subs(high_group).expand()

p_x, p_y, p_z = sp.symbols("p_x p_y p_z")
P_inp = sp.Matrix([p_x, p_y, p_z, 1])

P_exp = P_inp.copy()
P_list = [a1, b1, c1, a2, b2, c2, a3, b3, c3]
for i in range(3):
    P_exp[i] += (P_list[i] + P_list[i+3] + P_list[i+6])

P_real = T_4__0 * P_inp

P_err = P_real - P_exp
P_err.simplify()
for i in range(3):
    P_err[i] = P_err[i].collect([p_x, p_y, p_z])

if __name__ == '__main__':
    print(P_err[0])
    print(P_err[1])
    print(P_err[2])