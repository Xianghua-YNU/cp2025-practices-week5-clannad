import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps=1000, num_walks=1000):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。

    参数:
        num_steps (int, optional): 每次随机游走的步数. 默认值为1000
        num_walks (int, optional): 随机游走的次数. 默认值为1000
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组
            - y_finals: 所有随机游走终点的y坐标数组
    """
    # TODO: 实现随机游走算法
    # 提示：
    # 1. 使用np.zeros初始化数组
    # 2. 使用np.random.choice生成随机步长
    # 3. 使用np.sum计算总位移
      # 初始化步长数组
    steps_x = np.random.choice([-1, 1], size=(num_walks, num_steps))
    steps_y = np.random.choice([-1, 1], size=(num_walks, num_steps))
    
    # 计算总位移
    x_finals = np.sum(steps_x, axis=1)
    y_finals = np.sum(steps_y, axis=1)
    
    return x_finals, y_finals


def calculate_mean_square_displacement():
    """计算不同步数下的均方位移
    
    对于预设的步数序列[1000, 2000, 3000, 4000]，分别进行多次随机游走模拟，
    计算每种步数下的均方位移。每次模拟默认进行1000次随机游走取平均。
    
    返回:
        tuple: 包含两个numpy数组的元组 (steps, msd)
            - steps: 步数数组 [1000, 2000, 3000, 4000]
            - msd: 对应的均方位移数组
    """
    # TODO: 实现均方位移计算
    # 提示：
    # 1. 使用random_walk_finals获取终点坐标
    # 2. 计算位移平方和
    # 3. 使用np.mean计算平均值
    steps = np.array([1000, 2000, 3000, 4000])
    msd = np.zeros_like(steps, dtype=float)
    
    for i, num_steps in enumerate(steps):
        x_finals, y_finals = random_walk_finals(num_steps=num_steps)
        # 计算位移平方和
        displacement_sq = x_finals**2 + y_finals**2
        msd[i] = np.mean(displacement_sq)
    
    return steps, msd


def analyze_step_dependence():
    """分析均方位移与步数的关系，并进行最小二乘拟合
    
    返回:
        tuple: (steps, msd, k)
            - steps: 步数数组
            - msd: 对应的均方位移数组
            - k: 拟合得到的比例系数
    """
    # TODO: 实现数据分析
    # 提示：
    # 1. 调用calculate_mean_square_displacement获取数据
    # 2. 使用最小二乘法拟合 msd = k * steps
    # 3. k = Σ(N·msd)/Σ(N²)
    steps, msd = calculate_mean_square_displacement()
    
    # 最小二乘拟合 msd = k * steps
    k = np.sum(steps * msd) / np.sum(steps**2)
    
    return steps, msd, k


if __name__ == "__main__":
    # TODO: 完成主程序
    # 提示：
    # 1. 获取数据和拟合结果
    # 2. 绘制实验数据点和理论曲线
    # 3. 设置图形属性
    # 4. 打印数据分析结果
    # 获取数据和拟合结果
    steps, msd, k = analyze_step_dependence()
    
    # 绘制实验数据点和理论曲线
    plt.figure(figsize=(8, 6))
    plt.scatter(steps, msd, label='Simulation Data', color='b')
    plt.plot(steps, k * steps, 'r-', label=f'Fit: MSD = {k:.2f} * N')
    
    # 设置图形属性
    plt.xlabel('Number of Steps (N)')
    plt.ylabel('Mean Square Displacement (MSD)')
    plt.title('Random Walk: MSD vs Number of Steps')
    plt.legend()
    plt.grid(True)
    
    # 打印数据分析结果
    print(f"Fitted proportionality constant k = {k:.4f}")
    print("Theoretical value for 2D random walk should be 1.0")
    
    plt.show()
