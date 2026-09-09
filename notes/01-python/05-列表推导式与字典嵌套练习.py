# -*- coding: utf-8 -*-
"""
《三密三千大千世界》· 事业线 · Python 筑基练习
=============================================
主题：列表推导式 + 字典嵌套 —— 股票字典的增删改查
场景：自选股池管理系统（持仓 + 心理偏差标签）
运行：python 05-列表推导式与字典嵌套练习.py
"""

# ==================== 第 1 部分：列表推导式 ====================
# 列表推导式：一行代码生成新列表 [表达式 for 元素 in 可迭代 if 条件]
print("=" * 45)
print("第1部分 · 列表推导式")

# 1.1 基础推导：从价格列表算出"涨跌额"（相对昨日收盘 100）
closes = [100.5, 101.2, 99.8, 102.0, 100.1, 103.5]
changes = [c - 100 for c in closes]          # 每个价格减基准
print(f"收盘价：{closes}")
print(f"相对基准的涨跌额：{[round(x, 2) for x in changes]}")

# 1.2 带条件推导：只保留上涨的日子
up_days = [c for c in closes if c > 100]
print(f"上涨（>100）的日子：{up_days}，共 {len(up_days)} 天")

# 1.3 推导式 + 三目运算：给每个价格打标签
labels = ["强" if c >= 102 else ("平" if c >= 100 else "弱") for c in closes]
print(f"强度标签：{labels}")

# 1.4 嵌套推导式：二维场景（3 天 × 2 只股票的涨跌幅矩阵）
matrix = [[1.2, -0.8], [0.5, 1.1], [-0.3, 0.7]]   # 行=天，列=股票
flatten_pos = [x for row in matrix for x in row if x > 0]  # 所有正数
print(f"矩阵中所有上涨数值：{[round(x, 2) for x in flatten_pos]}")

# ==================== 第 2 部分：字典嵌套 ====================
# 字典嵌套：外层键=股票代码，内层=该股的属性字典
print("\n" + "=" * 45)
print("第2部分 · 字典嵌套（股票池）")

portfolio = {
    "600519": {"name": "贵州茅台", "price": 1358.98, "shares": 100, "bias": "损失厌恶"},
    "000001": {"name": "平安银行", "price": 12.35, "shares": 2000, "bias": "锚定效应"},
    "300750": {"name": "宁德时代", "price": 185.60, "shares": 300, "bias": "过度自信"},
}

# 2.1 深层取值：两层索引
print(f"茅台现价：{portfolio['600519']['price']} 元")
print(f"平安银行持仓心理偏差：{portfolio['000001']['bias']}")

# 2.2 遍历嵌套字典：打印每只股票
print("\n当前自选股池：")
for code, info in portfolio.items():
    market_value = info["price"] * info["shares"]
    print(f"  {code} {info['name']}：{info['price']}元 × {info['shares']}股 = {market_value:,.0f}元（偏差：{info['bias']}）")

# ==================== 第 3 部分：增删改查（CRUD） ====================
print("\n" + "=" * 45)
print("第3部分 · 增删改查")

# --- 增（Create）---
portfolio["601318"] = {"name": "中国平安", "price": 45.20, "shares": 500, "bias": "从众"}
print("增：加入中国平安 →", list(portfolio.keys()))

# --- 删（Delete）---
removed = portfolio.pop("000001")     # pop 返回被删的字典
print(f"删：移除平安银行（{removed['name']}）→", list(portfolio.keys()))

# --- 改（Update）---
portfolio["600519"]["price"] = 1360.00      # 修改内层价格
portfolio["600519"]["shares"] += 100        # 加仓 100 股
print(f"改：茅台现价 1360，持仓 200 股 → 市值 {portfolio['600519']['price']*portfolio['600519']['shares']:,.0f} 元")

# --- 查（Read/Query）---
# 查 1：按条件筛选（配合推导式）——找出市值 > 5 万的股票
big = {code: info for code, info in portfolio.items() if info["price"] * info["shares"] > 50000}
print(f"查：市值>5万的股票 → {[v['name'] for v in big.values()]}")

# 查 2：找出有"损失厌恶"偏差的股票（行为金融视角）
loss_averse = [info["name"] for info in portfolio.values() if info["bias"] == "损失厌恶"]
print(f"查：带'损失厌恶'标签的股票 → {loss_averse}")

# 查 3：get() 安全取值，避免 KeyError
print(f"查：600000 是否存在 → {portfolio.get('600000', '不在池中')}")

# ==================== 综合：完整操作流程 ====================
print("\n" + "=" * 45)
print("综合练习 · 一次完整的股票池操作")

# 模拟行情更新：所有股票涨 2%（用推导式改嵌套字典）
for info in portfolio.values():
    info["price"] = round(info["price"] * 1.02, 2)
print("行情更新后（全部 +2%）：")
for code, info in portfolio.items():
    print(f"  {code} {info['name']}：{info['price']} 元")

# 统计总市值
total = sum(info["price"] * info["shares"] for info in portfolio.values())
print(f"组合总市值：{total:,.0f} 元")

# 心理偏差分布统计（用推导式生成标签列表再统计）
bias_list = [info["bias"] for info in portfolio.values()]
print(f"心理偏差标签分布：")
for b in set(bias_list):
    print(f"  {b}：{bias_list.count(b)} 只")
