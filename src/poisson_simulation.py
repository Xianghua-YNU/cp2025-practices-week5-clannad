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
      # 生成l值序列
    l_values = np.arange(0, max_l + 1)
    
    # 计算泊松分布概率质量函数
    pmf = np.exp(-lambda_param) * (lambda_param ** l_values) / factorial(l_values)
    
    # 绘制图形
    plt.figure(figsize=(10, 6))
    plt.bar(l_values, pmf, color='skyblue', alpha=0.7)
    plt.title(f'泊松分布概率质量函数 (λ={lambda_param})')
    plt.xlabel('事件发生次数 (l)')
    plt.ylabel('概率 P(X=l)')
    plt.xticks(l_values)
    plt.grid(True, linestyle='--', alpha=0.6)

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
     # 使用二项分布模拟抛硬币实验更高效
    results = np.random.binomial(n=n_flips, p=p_head, size=n_experiments)
    return results

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
    # 获取实验结果
    results = simulate_coin_flips(n_experiments=n_experiments)
    
    # 计算理论分布
    max_k = np.max(results)
    k_values = np.arange(0, max_k + 1)
    theory_pmf = np.exp(-lambda_param) * (lambda_param ** k_values) / factorial(k_values)
    
    # 绘制直方图和理论曲线
    plt.figure(figsize=(12, 6))
    plt.hist(results, bins=k_values - 0.5, density=True, 
             color='lightgreen', alpha=0.7, label='实验结果')
    plt.plot(k_values, theory_pmf, 'ro-', markersize=5, 
             linewidth=2, label='理论泊松分布')
    
    plt.title(f'泊松分布数值模拟 (N={n_experiments}组实验)')
    plt.xlabel('正面朝上次数')
    plt.ylabel('概率密度')
    plt.xticks(k_values)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # 计算并打印统计信息
    print(f"实验均值: {np.mean(results):.3f} (理论值: {lambda_param})")
    print(f"实验方差: {np.var(results):.3f} (理论值: {lambda_param})")

if __name__ == "__main__":
    # 设置随机种子
    np.random.seed(42)
    
    # 1. 绘制理论分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    plt.show()
