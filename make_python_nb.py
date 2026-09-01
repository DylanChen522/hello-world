import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
nb.cells = []

# 帮助函数
def md(text):
    nb.cells.append(nbf.v4.new_markdown_cell(text))
def code(text):
    nb.cells.append(nbf.v4.new_code_cell(text))

# ============ 第3周：Python基础（变量/列表/字符串/条件/循环） ============
md("""# Python 基础模块（筑基期 · 第3-5周）

《三密三千大千世界》修行计划 · 事业线

- **第3周**：变量 / 列表 / 字符串 / 条件 / 循环
- **第4周**：函数 / 类 / 异常处理 / 文件读写
- **第5周**：NumPy 数组运算 + 向量化 / LeetCode 简单题 / SQL 基础

> 目标：从零掌握 Python 核心语法，为量化交易的数据处理打基础。""")

md("""## 第3周 · 变量与基本数据类型

**核心概念（口诀：四类数据记心中）**
- `int` 整数 → 1, 100, -5
- `float` 浮点数（小数）→ 1.5, 3.14
- `str` 字符串（文本）→ "你好", 'python'
- `bool` 布尔值 → True / False

**变量 = 给数据起名字**，用 `=` 赋值，无需声明类型。""")

code('''# === 变量与类型 ===
price = 100.5          # float 价格
shares = 3             # int 股数
stock_name = "平安银行" # str 股票名
is_profit = True       # bool 是否盈利

print("价格:", price)
print("股数:", shares)
print("股票:", stock_name)
print("是否盈利:", is_profit)
print("总市值:", price * shares)

# 查看类型
print("price 的类型:", type(price))
print("shares 的类型:", type(shares))''')

md("""### 列表（List）—— 有序可变序列

用 `[]` 创建，可存放任意数据，是 Python 最常用的容器。""")

code('''# === 列表 ===
prices = [100.5, 101.2, 99.8, 102.0, 100.1]  # 5天股价
print("价格列表:", prices)
print("第1个价格(索引0):", prices[0])
print("最后1个价格(索引-1):", prices[-1])
print("前3个价格:", prices[:3])
print("列表长度:", len(prices))

# 添加/修改
prices.append(103.5)   # 末尾添加
prices[0] = 99.9       # 修改第一个
print("更新后:", prices)

# 列表常用操作
print("最大值:", max(prices))
print("最小值:", min(prices))
print("平均值:", sum(prices)/len(prices))''')

md("""### 字符串（String）—— 文本处理

量化交易中经常处理股票代码、报告文本、日期格式。""")

code('''# === 字符串 ===
code1 = "600519"   # 贵州茅台
code2 = "000001"   # 平安银行

# 拼接与格式化
print("股票代码: " + code1)
print(f"今天买入 {code1}，价格 {100.5} 元")  # f-string 最常用

# 常用方法
text = "  Hello, Quant World  "
print("去除空格:", text.strip())
print("转大写:", text.upper())
print("是否以Hello开头:", text.strip().startswith("Hello"))
print("按逗号分割:", text.strip().split(","))

# 切片
s = "Python量化"
print("前6个字符:", s[:6])
print("后2个字符:", s[-2:])''')

md("""### 条件判断（if / elif / else）—— 让程序做决策

**口诀：从上到下找第一个为 True 的分支执行**""")

code('''# === 条件判断 ===
profit = -50  # 当日盈亏

if profit > 0:
    print("✅ 今日盈利", profit, "元")
elif profit == 0:
    print("➖ 今日平盘")
else:
    print("❌ 今日亏损", profit, "元")

# 逻辑运算
price = 100
if price > 90 and price < 110:
    print("价格在正常区间内")
if price < 90 or price > 110:
    print("价格异常波动")

# 真实场景：判断是否触发止损
cost = 100
stop_loss = 0.08  # 8%止损
if (cost - price) / cost >= stop_loss:
    print("⚠️ 触发止损线！考虑减仓")
else:
    print(f"回撤 {((cost-price)/cost*100):.2f}%，未触发止损")''')

md("""### 循环（for / while）—— 重复执行

**for 遍历**：对列表/范围逐个处理
**while 条件循环**：满足条件就一直执行""")

code('''# === for 循环 ===
prices = [100.5, 101.2, 99.8, 102.0]
for p in prices:
    print("价格:", p)

# range 生成数字序列
print("--- range(5) ---")
for i in range(5):
    print("第", i, "天")

# 计算收益率
prices = [100, 101, 99, 102, 105]
returns = []
for i in range(1, len(prices)):
    ret = (prices[i] - prices[i-1]) / prices[i-1]
    returns.append(ret)
print("每日收益率:", [f"{r:.4f}" for r in returns])

# === while 循环 ===
count = 0
total = 0
while total < 100:  # 累计到100停止
    count += 1
    total += 10
print(f"循环了 {count} 次，累计 {total}")

# 列表推导式（一行生成列表，量化常用）
squares = [x*x for x in range(1, 6)]
print("1-5的平方:", squares)''')

md("""### 🧪 第3周小练习（动手做）

1. 创建一个包含你 5 只关注股票的列表，打印它们
2. 计算 `[88, 95, 102, 97, 91]` 的均值、最大、最小
3. 用循环计算 1 到 100 的和
4. 判断一个数字是奇数还是偶数（if 语句）""")

code('''# === 练习解答区（先自己写，再看答案） ===
# 1. 股票列表
stocks = ["贵州茅台", "宁德时代", "招商银行", "比亚迪", "腾讯控股"]
print("关注股票:", stocks)

# 2. 统计
data = [88, 95, 102, 97, 91]
print(f"均值:{sum(data)/len(data):.2f} 最大:{max(data)} 最小:{min(data)}")

# 3. 1到100求和
total = sum(range(1, 101))
print("1到100的和:", total)

# 4. 奇偶判断
n = 17
print(n, "是偶数" if n % 2 == 0 else "是奇数")''')

# ============ 第4周：函数/类/异常处理/文件读写 ============
md("""## 第4周 · 函数 / 类 / 异常处理 / 文件读写

### 函数（Function）—— 封装可复用代码

**def 定义 → 参数传入 → return 返回结果**""")

code('''# === 函数 ===
def calc_returns(prices):
    """计算价格列表的收益率序列"""
    returns = []
    for i in range(1, len(prices)):
        returns.append((prices[i] - prices[i-1]) / prices[i-1])
    return returns

# 调用函数
p1 = [100, 102, 101, 105]
r1 = calc_returns(p1)
print("收益率:", [f"{x:.4f}" for x in r1])

# 带默认参数
def calc_sharpe(returns, rf=0.02):
    """简化夏普比率计算"""
    mean_r = sum(returns)/len(returns) if returns else 0
    std_r = (sum((x-mean_r)**2 for x in returns)/len(returns))**0.5
    return (mean_r - rf/252) / std_r if std_r > 0 else 0

daily_r = [0.01, -0.005, 0.02, 0.008, -0.003]
print("简化夏普:", f"{calc_sharpe(daily_r):.4f}")''')

md("""### 类（Class）—— 对象化封装

把「数据 + 操作」打包成对象，适合构建交易策略等复杂结构。""")

code('''# === 类 ===
class Stock:
    """股票类：包含代码、名称、价格，和计算市值的方法"""
    def __init__(self, code, name, price, shares=0):
        self.code = code
        self.name = name
        self.price = price
        self.shares = shares

    def market_value(self):
        """计算市值"""
        return self.price * self.shares

    def update_price(self, new_price):
        self.price = new_price
        print(f"{self.name} 价格更新为 {new_price}")

# 创建对象
maotai = Stock("600519", "贵州茅台", 1500, 100)
pingan = Stock("000001", "平安银行", 10.5, 1000)

print(f"{maotai.name} 市值: {maotai.market_value()}")
maotai.update_price(1550)
print(f"更新后市值: {maotai.market_value()}")
print(f"{pingan.name} 市值: {pingan.market_value()}")''')

md("""### 异常处理（try / except）—— 程序出错不崩溃

量化交易中数据缺失、除零、网络异常很常见，必须学会容错。""")

code('''# === 异常处理 ===
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "错误：除数不能为0"
    except TypeError:
        return "错误：请输入数字"
    finally:
        pass  # 无论是否异常都会执行

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "abc"))

# 文件读取容错
def read_file_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "文件不存在"
    except Exception as e:
        return f"读取失败: {e}"

print(read_file_safe("不存在的文件.txt"))''')

md("""### 文件读写 —— 保存与读取数据

量化交易要保存策略结果、读取历史行情。""")

code('''# === 文件读写 ===
import os

# 写入文件
with open("strategy_result.txt", "w", encoding="utf-8") as f:
    f.write("策略回测结果\\n")
    f.write("年化收益率: 15.2%\\n")
    f.write("最大回撤: -8.5%\\n")
print("文件写入完成")

# 读取文件
with open("strategy_result.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("--- 文件内容 ---")
print(content)

# 追加写入
with open("strategy_result.txt", "a", encoding="utf-8") as f:
    f.write("夏普比率: 1.35\\n")
print("追加完成")

# 重新读取验证
with open("strategy_result.txt", "r", encoding="utf-8") as f:
    print(f.read())''')

md("""### 🧪 第4周小练习

1. 写一个函数 `max_drawdown(returns)` 计算最大回撤
2. 用类封装一个简单的移动平均策略
3. 写一个能容错的函数（处理除零和类型错误）""")

code('''# === 练习：计算最大回撤 ===
def max_drawdown(prices):
    """计算价格序列的最大回撤"""
    peak = prices[0]
    max_dd = 0
    for p in prices:
        if p > peak:
            peak = p
        dd = (peak - p) / peak
        if dd > max_dd:
            max_dd = dd
    return max_dd

prices = [100, 102, 98, 95, 99, 92, 96]
dd = max_drawdown(prices)
print(f"最大回撤: {dd*100:.2f}%")''')

# ============ 第5周：NumPy ============
md("""## 第5周 · NumPy 数组运算 + 向量化

**为什么量化必须用 NumPy？**
- 纯 Python 循环处理 100 万条数据很慢
- NumPy 向量化运算：一次操作整个数组，速度快几十倍
- 它是 pandas / 回测框架的底层引擎""")

code('''# === 安装并导入 NumPy ===
try:
    import numpy as np
    print("NumPy 版本:", np.__version__)
except ImportError:
    print("需要安装: pip install numpy")''')

code('''# === 创建数组 ===
import numpy as np

# 从列表创建
arr1 = np.array([100, 101, 99, 102, 105])
print("数组1:", arr1)
print("类型:", type(arr1))
print("形状:", arr1.shape)  # (5,) 一维5个元素

# 特殊数组
zeros = np.zeros(5)         # 全0
ones = np.ones((2, 3))      # 2行3列全1
arange = np.arange(0, 10, 2) # 0,2,4,6,8
print("zeros:", zeros)
print("ones 2x3:", ones)
print("arange(0,10,2):", arange)

# 随机数（模拟价格）
np.random.seed(42)  # 固定随机种子，结果可复现
prices = np.random.normal(100, 2, 10)  # 均值100,标准差2,10个
print("模拟价格:", np.round(prices, 2))''')

md("""### 向量化运算 —— 一次算一整组

**关键优势：不用写循环，整组数据一次算完**""")

code('''# === 向量化运算 ===
import numpy as np

prices = np.array([100, 102, 98, 105, 101])
print("原始价格:", prices)

# 整组加减乘除
print("×1.01:", prices * 1.01)
print("+5:", prices + 5)
print("平方:", prices ** 2)

# 布尔筛选（找出高于100的）
high = prices[prices > 100]
print(">100的:", high)

# 收益率向量化计算
returns = np.diff(prices) / prices[:-1]
print("收益率:", np.round(returns, 4))

# 统计函数
print("均值:", prices.mean())
print("标准差:", prices.std())
print("最大值:", prices.max(), "最小值:", prices.min())
print("百分位(90%):", np.percentile(prices, 90))''')

code('''# === 性能对比：循环 vs 向量化 ===
import numpy as np
import time

# 100万个数据点
big = np.random.random(1_000_000)

# 方式1：纯Python循环
start = time.time()
total_loop = sum(big)
t_loop = time.time() - start

# 方式2：NumPy向量化
start = time.time()
total_vec = big.sum()
t_vec = time.time() - start

print(f"循环法: {t_loop:.4f}秒")
print(f"向量化: {t_vec:.4f}秒")
print(f"向量化快 {t_loop/t_vec:.0f} 倍")
print("结果一致:", total_loop == total_vec)''')

md("""### 🧪 第5周练习

1. 用 NumPy 生成 30 天模拟股价，计算收益率
2. 找出收益率大于 1% 的天数
3. 计算年化波动率""")

code('''# === 练习：30天模拟行情分析 ===
import numpy as np

np.random.seed(7)
# 模拟30天日收益率（均值0.05%，标准差1%）
daily_returns = np.random.normal(0.0005, 0.01, 30)
# 模拟价格路径
price = 100
prices = [price]
for r in daily_returns:
    price *= (1 + r)
    prices.append(price)
prices = np.array(prices)

print("30天收盘价:")
print(np.round(prices, 2))
print(f"期末价格: {prices[-1]:.2f} (期初100)")
print(f"总收益率: {(prices[-1]/prices[0]-1)*100:.2f}%")
print(f"年化波动率: {daily_returns.std()*np.sqrt(252)*100:.2f}%")
print(f"上涨天数: {(daily_returns>0).sum()}, 下跌天数: {(daily_returns<0).sum()}")''')

md("""## 📝 模块总结

### 掌握清单（自检）
- [ ] 变量与 4 种基本类型（int/float/str/bool）
- [ ] 列表创建、索引、切片、增删改
- [ ] 字符串拼接、f-string、常用方法
- [ ] if/elif/else 条件判断
- [ ] for / while 循环、列表推导式
- [ ] 函数定义（def、参数、返回值、默认参数）
- [ ] 类（__init__、方法、对象）
- [ ] try/except 异常处理
- [ ] 文件读写（open / with）
- [ ] NumPy 数组、向量化运算、性能优势

### 核心口诀
```
改 → add → commit      # Git
价格 → 收益率 → 回撤     # 量化分析主线
循环慢，向量快          # NumPy 核心优势
```

### 下一步
完成本模块后，可以：
1. 刷 3 道 LeetCode 简单题（数组/字符串类）
2. 学习 SQL 基础（SELECT / WHERE / ORDER BY）
3. 进入「概率统计」模块""")

nbf.write(nb, "python_basics.ipynb")
print("Notebook 已创建: python_basics.ipynb")
print("共", len(nb.cells), "个单元格")
