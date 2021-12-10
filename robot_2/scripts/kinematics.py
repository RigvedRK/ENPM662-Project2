import sympy as sp

"""################################ Transformation Matrix ################################"""

theta1, theta2, theta3, theta4, theta5, theta6, d1, d3, d5, d7, theta, alpha, a, d = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6 d1 d3 d5 d7 theta alpha a d')

t_matrix = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
                 [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
                 [0, sp.sin(alpha), sp.cos(alpha), d],
                 [0,0,0,1]])


v_a3 = 975
v_ad = 155.9
v_d4 = 744.92
v_d7 = 144.98

l01 = t_matrix.subs({a:0, alpha:-sp.pi/2, d:0, theta:theta1})
l12 = t_matrix.subs({a:0, alpha:0, d:0, theta:theta2-sp.pi/2})
l23 = t_matrix.subs({a:v_a3, alpha:0, d:0, theta:0})
l3d = t_matrix.subs({a:v_a3, alpha:-sp.pi/2, d:0, theta:theta3})
ld4 = t_matrix.subs({a:0, alpha:0, d:v_d4, theta:0})
l45 = t_matrix.subs({a:0, alpha:sp.pi/2, d:0, theta:theta4})
l56 = t_matrix.subs({a:0, alpha:-sp.pi/2, d:0, theta:theta5})
l67 = t_matrix.subs({a:0, alpha:0, d:v_d7, theta:theta6})

# Final Transformation Matrix.
T0n = l01*l12*l23*l3d*ld4*l45*l56*l67

# Forward Kinematics Validation
"""theta1:0, theta2:0, theta3:0, theta4:0,theta5:0, theta6:0"""
sp.pprint(T0n.subs({theta1:0, theta2:0, theta3:0, theta4:0,theta5:0, theta6:0}))
"""theta1:sp.pi/2, theta2:-sp.pi/2, theta3:0, theta4:sp.pi,theta5:0, theta6:0"""
sp.pprint(T0n.subs({theta1:sp.pi/2, theta2:-sp.pi/2, theta3:0, theta4:sp.pi,theta5:0, theta6:0}))

#Inverse Kinematics Validation
rotation = T0n.subs({theta1:0.7854, theta2:2.353, theta3:-1.0404, theta4:1.562,theta5:-0.3921, theta6:1.0566})[:3,:3]
sp.pprint(rotation)