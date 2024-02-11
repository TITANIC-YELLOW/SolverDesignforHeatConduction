import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # 导入3D绘图工具
import numpy as np
import readDAT

points = readDAT.getdata('model1_job1.dat')[0]
X = points[:, 0]
Y = points[:, 1]
Z = points[:, 2]
C0 = np.loadtxt('3d_temperature.txt')

# 设置图表和坐标轴
fig = plt.figure()  # 创建一个图
ax = fig.add_subplot(111, projection='3d')

# 创建散点图
scatter = ax.scatter3D(X, Y, Z, c=C0[:, 0], cmap='jet')

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# 创建 colorbar
# cb = plt.colorbar(scatter, ax=ax)


# 你的动画函数
def update(frame):
    # 在这里更新你的图表或动画内容
    # 这个函数会为每一帧调用
    # scatter._offsets3d = (X, Y, Z)  # 更新散点位置
    scatter.set_array(C0[:, frame])  # 更新颜色数据
    print(np.min(C0[:, frame]))
    return scatter,  # 返回一个可迭代的对象


# 设置帧数
num_frames = 100

# 创建动画
ani = FuncAnimation(fig, update, frames=num_frames, interval=1)

# 显示图表（可选）
plt.show()
