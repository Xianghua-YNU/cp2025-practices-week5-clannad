import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数
    
    参数:
        lambda_param (float): 泊松分布参数λ
        max_l (int): 最大的l值
    """
    # TODO: 实现泊松分布概率质量函数的计算和绘制
    # 提示：
    # 1. 使用np.arange生成l值序列
    # 2. 使用给定公式计算PMF
    # 3. 使用plt绘制图形并设置标签
    l_values = np.arange(max_l)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    plt.figure(figsize=(10, 6))
    plt.plot(l_values, pmf, 'bo-', markersize=5, linewidth=2, 
             label=f'泊松分布 (λ={lambda_param})')
    plt.title('泊松分布概率质量函数')
    plt.xlabel('事件发生次数 (l)')
    plt.ylabel('概率 P(X=l)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    return pmf

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验
    
    参数:
        n_experiments (int): 实验组数N
        n_flips (int): 每组抛硬币次数
        p_head (float): 正面朝上的概率
        
    返回:
        ndarray: 每组实验中正面朝上的次数
    """
    # TODO: 实现多组抛硬币实验
    # 提示：
    # 1. 使用np.random.choice模拟硬币抛掷
    # 2. 统计每组实验中正面的次数
     return np.random.binomial(n=n_flips, p=p_head, size=n_experiments)
   
def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布
    
    参数:
        n_experiments (int): 实验组数
        lambda_param (float): 泊松分布参数λ
    """
    # TODO: 实现实验结果与理论分布的对比
    # 提示：
    # 1. 调用simulate_coin_flips获取实验结果
    # 2. 计算理论分布
    # 3. 绘制直方图和理论曲线
    # 4. 计算并打印统计信息
    # 进行实验模拟
     results = simulate_coin_flips(n_experiments)
    max_l = max(int(lambda_param * 2), np.max(results) + 1)
    l_values = np.arange(max_l)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    plt.figure(figsize=(12, 7))
    plt.hist(results, bins=range(max_l+1), density=True, alpha=0.7,
             label='实验结果', color='skyblue', edgecolor='white')
    plt.plot(l_values, pmf, 'r-', linewidth=2, 
             label=f'理论分布 (λ={lambda_param})')
    
    plt.title(f'泊松分布数值模拟比较 (N={n_experiments})')
    plt.xlabel('正面朝上次数')
    plt.ylabel('频率/概率')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()
    
    # 计算并显示统计量
    print("实验统计量:")
    print(f"均值: {np.mean(results):.2f} (理论值: {lambda_param})")
    print(f"方差: {np.var(results):.2f} (理论值: {lambda_param})")

if __name__ == "__main__":
    # 设置随机种子
    np.random.seed(42)
    
    # 1. 绘制理论分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    plt.show()
