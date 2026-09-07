# -*- coding: utf-8 -*-
"""
《三密三千大千世界》· 事业线 · Python 筑基练习
=============================================
主题：变量 / 列表 / 字典 / 循环（100 行动手版）
场景：投教博主「三密」的交易心理日志与分析
运行：python 03-变量列表字典循环练习.py
"""

# ==================== 第 1 部分：变量 ====================
# 1.1 四种基本类型：int / float / str / bool
account = 100000          # int 账户本金（元）
risk_ratio = 0.02         # float 单笔风险比例 2%
author = "三密"           # str 作者名
is_discipline = True      # bool 是否守纪律

print("=" * 40)
print("第1部分 · 变量")
print(f"账户本金：{account} 元，单笔风险：{risk_ratio*100:.0f}%")
print(f"作者：{author}，守纪律：{is_discipline}")

# 1.2 变量是动态类型，可重新赋值
x = 21          # 先存整数
x = "二十一"     # 再存字符串
print(f"变量 x 当前类型：{type(x).__name__}，值：{x}")

# 1.3 一行交换两个变量（Python 特色）
a, b = 100, 200
a, b = b, a
print(f"交换后：a={a}, b={b}")

# ==================== 第 2 部分：列表 ====================
# 2.1 创建 / 索引 / 切片
prices = [100.5, 101.2, 99.8, 102.0, 100.1]   # 5 天收盘价
print("\n第2部分 · 列表")
print(f"价格列表：{prices}")
print(f"首日价：{prices[0]}，末日价：{prices[-1]}，前3天：{prices[:3]}")

# 2.2 增删改
prices.append(103.2)      # 末尾追加
prices.insert(0, 99.5)    # 开头插入
prices[2] = 100.0         # 修改第3个
print(f"增删改后：{prices}")

# 2.3 遍历 + enumerate 取索引
print("逐日价格：")
for i, p in enumerate(prices):
    print(f"  第{i+1}天：{p}")

# 2.4 推导式 + 常用函数
ups = [p for p in prices if p > 100]     # 大于100的日子
print(f"价格>100 的天数：{len(ups)} 天，均值：{sum(prices)/len(prices):.2f}")

# ==================== 第 3 部分：字典 ====================
# 3.1 创建与增删改查
position = {"code": "600519", "name": "贵州茅台", "shares": 100, "cost": 1500.0}
print("\n第3部分 · 字典")
print(f"持仓：{position}")
print(f"股票名：{position['name']}，成本价：{position['cost']}")

position["price"] = 1620.0    # 新增键：现价
position["shares"] = 200      # 修改键
del position["code"]          # 删除键
print(f"更新后：{position}")

# 3.2 遍历 keys / values / items
for k, v in position.items():
    print(f"  {k} = {v}")

# 3.3 get() 默认值，避免 KeyError
print(f"行业：{position.get('industry', '未知')}")

# 3.4 嵌套字典：行为金融四大心理偏差
biases = {
    "损失厌恶": {"痛苦倍数": 2, "典型操作": "亏了死扛"},
    "锚定效应": {"痛苦倍数": 1, "典型操作": "死盯成本价"},
    "过度自信": {"痛苦倍数": 1, "典型操作": "频繁交易"},
    "从众":     {"痛苦倍数": 1, "典型操作": "追涨杀跌"},
}
print(f"心理偏差数量：{len(biases)} 种")

# ==================== 第 4 部分：循环 ====================
# 4.1 for + range
print("\n第4部分 · 循环")
total = 0
for i in range(1, 11):        # 1~10
    total += i
print(f"1+2+...+10 = {total}")

# 4.2 while + break / continue
n, count = 1, 0
while n <= 100:
    if n % 2 == 0:            # 偶数跳过
        n += 1
        continue
    if n > 9:                 # 只统计前几个奇数
        break
    count += 1
    n += 1
print(f"1~9 中奇数个数：{count}")

# 4.3 嵌套循环：状态 × 纪律
print("止损纪律检查（持仓状态 × 是否守纪律）：")
states = ["浮亏", "浮盈", "平盘"]
for s in states:
    for d in [True, False]:
        action = "按计划止损" if d else "死扛"
        print(f"  {s} + 纪律{d} → {action}")

# ============ 综合练习：交易心理日志（四件套合体） ============
# 用变量 / 列表 / 字典 / 循环，统计 5 笔交易的心理偏差
print("\n综合练习 · 交易心理日志")
trades = [
    {"日期": "09-01", "偏差": "损失厌恶", "盈亏": -800},
    {"日期": "09-02", "偏差": "锚定效应", "盈亏": -300},
    {"日期": "09-03", "偏差": "过度自信", "盈亏": 200},
    {"日期": "09-04", "偏差": "损失厌恶", "盈亏": -500},
    {"日期": "09-05", "偏差": "从众",     "盈亏": 400},
]
total_pnl = 0
loss_count = 0
bias_stat = {}                       # 统计每种偏差出现次数
for t in trades:
    total_pnl += t["盈亏"]
    if t["盈亏"] < 0:
        loss_count += 1
    bias_stat[t["偏差"]] = bias_stat.get(t["偏差"], 0) + 1
    print(f"  {t['日期']} {t['偏差']}：{t['盈亏']:+d} 元")

print(f"总盈亏：{total_pnl:+d} 元；亏损笔数：{loss_count}/5")
print("偏差频率：")
for name, cnt in bias_stat.items():
    print(f"  {name}：{cnt} 次")
print("结论：亏损全部来自心理偏差 → 纪律是第一位！")
