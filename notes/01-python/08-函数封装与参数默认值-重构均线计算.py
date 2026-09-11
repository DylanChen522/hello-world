# -*- coding: utf-8 -*-
"""
《三密三千大千世界》· 事业线 · Python 筑基练习
=============================================
主题：函数封装 + 参数默认值 + 返回值 —— 重构均线计算
场景：把第 06 课手写的均线逻辑，升级成"可复用的函数工具箱"
前置：先做过 06 课（for/while + MA5），本课是它的函数化重构
运行：python 08-函数封装与参数默认值-重构均线计算.py
"""

# ==================== 数据准备：沿用 06 课的茅台行情 ====================
dates = ["09-01", "09-02", "09-03", "09-04", "09-05",
         "09-08", "09-09", "09-10", "09-11", "09-12"]
closes = [1680.00, 1695.50, 1702.30, 1688.90, 1700.00,
          1712.50, 1708.20, 1720.00, 1715.60, 1725.80]

print("=" * 45)
print(f"行情样本：{len(closes)} 天收盘价（{dates[0]}~{dates[-1]}）")

# ==================== 第 1 部分：函数封装 ====================
# 函数 = def 名字(参数): ... return 结果
# 好处：逻辑写一次，随处可调，不用复制粘贴
print("\n" + "=" * 45)
print("第1部分 · 函数封装（把 MA5 逻辑装进函数）")


def calc_ma5(closes):
    """计算 5 日均线，返回与输入等长的列表，前 4 天为 None。"""
    ma5 = []
    for i in range(len(closes)):
        if i < 4:                              # 窗口不足 5 天
            ma5.append(None)
        else:
            ma5.append(round(sum(closes[i - 4:i + 1]) / 5, 2))
    return ma5                                 # return 把结果交出去


ma5 = calc_ma5(closes)                         # 调用：实参 closes 传给形参
print(f"MA5 = {ma5}")
print(f"第 5 天 MA5 = {ma5[4]}（与 06 课手算一致）")

# 函数可重复调用：同样的输入得到同样结果，逻辑只维护一份
print(f"再调一次，结果相同：{calc_ma5(closes) == ma5}")

# ==================== 第 2 部分：参数默认值 ====================
# 把"窗口期"也变成参数 period，默认 5 → 一个函数同时算出 MA5 / MA10 / MA20
print("\n" + "=" * 45)
print("第2部分 · 参数默认值（period=5，想算几天就传几天）")


def calc_ma(closes, period=5):
    """计算 period 日均线。period 有默认值 5，不传就按 MA5 算。"""
    ma = []
    for i in range(len(closes)):
        if i < period - 1:                     # 前 period-1 天窗口不足
            ma.append(None)
        else:
            window = closes[i - period + 1:i + 1]
            ma.append(round(sum(window) / period, 2))
    return ma


ma5 = calc_ma(closes)                          # 省略第二参 → 用默认值 5
ma10 = calc_ma(closes, 10)                     # 位置传参 → MA10
ma3 = calc_ma(closes, period=3)                # 关键字传参 → MA3（可读性更好）
print(f"MA5  = {ma5}")
print(f"MA10 = {ma10}")
print(f"MA3  = {ma3}")

# 默认值陷阱提醒：默认参数在"定义时"只求值一次，
# 千万别用可变对象（列表/字典）当默认值
print("\n默认值陷阱提醒：")


def bad_append(x, acc=[]):                     # 反例：acc 默认是同一个列表
    acc.append(x)
    return acc


def good_append(x, acc=None):                  # 正例：用 None 占位，进来再建
    if acc is None:
        acc = []
    acc.append(x)
    return acc


print(f"  反例：bad_append(1)={bad_append(1)}，bad_append(2)={bad_append(2)}（被污染了！）")
print(f"  正例：good_append(1)={good_append(1)}，good_append(2)={good_append(2)}（互不影响）")

# ==================== 第 3 部分：返回值 ====================
# return 可以返回：单个值 / 元组（多个值）/ 字典（结构化结果）
print("\n" + "=" * 45)
print("第3部分 · 返回值（从'一个列表'升级为'一份报告'）")


def analyze_ma(closes, period=5):
    """返回一个字典：均线 + 最新值 + 区间趋势。"""
    ma = calc_ma(closes, period)
    valid = [m for m in ma if m is not None]   # 去掉窗口不足的部分
    first, last = valid[0], valid[-1]
    trend = "上行" if last > first else ("下行" if last < first else "走平")
    return {
        "period": period,
        "ma": ma,
        "latest": last,                        # 最新一个均线值
        "trend": trend,                        # 区间趋势
        "days": len(valid),                    # 有效均线天数
    }


report = analyze_ma(closes, period=5)
print(f"MA5 分析报告：{report}")
print(f"  最新 MA5 = {report['latest']}，短期趋势 = {report['trend']}")

# 元组返回：一次性拿多个值（解包）
def latest_price(closes):
    """返回 (日期, 价格, 涨跌额) 三件套。"""
    last_date, last_p = dates[-1], closes[-1]
    chg = closes[-1] - closes[-2]
    return last_date, last_p, chg


d, p, c = latest_price(closes)                 # 元组解包，一次拿三个值
print(f"最新交易日：{d}，收盘 {p}，较前日 {c:+.2f} 元")

# ==================== 第 4 部分：重构 ====================
# 把 06 课的"滑动窗口 + 增量滚动 + 趋势判断"全部函数化，
# 主流程只剩几行调用 —— 这就是"重构"的意义：逻辑复用、易读易测
print("\n" + "=" * 45)
print("第4部分 · 重构：均线工具箱（一处实现，处处调用）")


def calc_ma_sliding(closes, period=5):
    """法一：滑动窗口法（每步切片求和）。"""
    return calc_ma(closes, period)             # 06 课"滑动窗口"的通用版


def calc_ma_incremental(closes, period=5):
    """法二：增量滚动法（窗口和 减旧加新，O(n) 更高效）。"""
    if len(closes) < period:
        return [None] * len(closes)
    win_sum = sum(closes[:period])
    ma = [None] * (period - 1) + [round(win_sum / period, 2)]
    for i in range(period, len(closes)):
        win_sum = win_sum - closes[i - period] + closes[i]
        ma.append(round(win_sum / period, 2))
    return ma


def ma_report(closes, period=5):
    """组合拳：两种算法 + 交叉验证 + 趋势判断，一次输出完整报告。"""
    if len(closes) < period:
        return {"period": period, "ma": [None] * len(closes),
                "trend": "数据不足", "consistent": True}
    ma_a = calc_ma_sliding(closes, period)
    ma_b = calc_ma_incremental(closes, period)
    assert ma_a == ma_b, "两种算法结果不一致！"   # 内部自检
    valid = [m for m in ma_a if m is not None]
    trend = "上行" if valid[-1] > valid[0] else "下行"
    return {"period": period, "ma": ma_a, "trend": trend, "consistent": True}


# 主流程：三行调用，覆盖 MA5 / MA10 / MA20
for p in (5, 10, 20):
    r = ma_report(closes, period=p)
    print(f"  MA{p}：趋势{r['trend']}，两算法一致={r['consistent']}，"
          f"最新值={r['ma'][-1]}")

# 对比：06 课是"平铺的脚本"，本课是"可复用的工具箱"
print("\n重构前后对比：")
print("  06 课：逻辑全部平铺在脚本里，想算 MA10 得改代码再跑一遍")
print("  本课：calc_ma(closes, 10) 一行搞定，period 想传几就传几")
print("  下一步：把工具箱存成 .py 模块 import 复用，就是'工程化'")
