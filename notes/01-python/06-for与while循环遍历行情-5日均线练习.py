# -*- coding: utf-8 -*-
"""
《三密三千大千世界》· 事业线 · Python 筑基练习
=============================================
主题：for / while 循环遍历行情列表，算 5 日均线（MA5）
场景：把一段收盘价行情，用两种循环读一遍，再算出 MA5 趋势线
运行：python 06-for与while循环遍历行情-5日均线练习.py
"""

# ==================== 准备：行情数据 ====================
# 贵州茅台（600519）近 10 个交易日收盘价（元，示意数据，非实时行情）
dates = ["09-01", "09-02", "09-03", "09-04", "09-05",
         "09-08", "09-09", "09-10", "09-11", "09-12"]
closes = [1680.00, 1695.50, 1702.30, 1688.90, 1700.00,
          1712.50, 1708.20, 1720.00, 1715.60, 1725.80]

print("=" * 45)
print(f"行情样本：{len(closes)} 天收盘价")
print(f"范围：{dates[0]} ~ {dates[-1]}，最高 {max(closes)}，最低 {min(closes)}")

# ==================== 第 1 部分：for 循环遍历行情 ====================
print("\n" + "=" * 45)
print("第1部分 · for 循环遍历")

# 1.1 直接遍历列表：读出每一天的价格
print("逐日收盘价：")
for price in closes:
    print(f"  {price:.2f} 元")

# 1.2 enumerate 同时拿到日期下标，方便对齐日期
print("\n带日期的逐日行情：")
for i, price in enumerate(closes):
    print(f"  {dates[i]}：{price:.2f} 元")

# 1.3 遍历 + 累计统计：算区间涨跌
start, end = closes[0], closes[-1]
total_chg = end - start
print(f"\n区间累计涨跌：{end} - {start} = {total_chg:+.2f} 元（{(total_chg/start)*100:+.2f}%）")

# 1.4 for 遍历同时做判断：数一数"跑赢 1700"的天数
strong_days = []
for i, price in enumerate(closes):
    if price >= 1700:
        strong_days.append(dates[i])
print(f"价格 ≥1700 的日子：{strong_days}，共 {len(strong_days)} 天")

# ==================== 第 2 部分：while 循环遍历行情 ====================
print("\n" + "=" * 45)
print("第2部分 · while 循环遍历（索引式）")

# 2.1 用下标游标遍历：适合"边走边控"的场景
i = 0
while i < len(closes):
    print(f"  [{i}] {dates[i]}：{closes[i]:.2f} 元")
    i += 1

# 2.2 while 的 break：找到第一个突破 1700 的日子就停
print("\n第一个 ≥1700 的日子（while + break）：")
j = 0
while j < len(closes):
    if closes[j] >= 1700:
        print(f"  {dates[j]}：{closes[j]:.2f} 元（第 {j+1} 天）")
        break
    j += 1

# 2.3 while 的 continue：跳过"下跌日"，只打印上涨日
print("\n只打印上涨日（while + continue）：")
k = 0
while k < len(closes):
    if k > 0 and closes[k] <= closes[k - 1]:   # 比前一天低或平 → 跳过
        k += 1
        continue
    print(f"  {dates[k]}：{closes[k]:.2f} 元")
    k += 1

# 对比小结：数据量明确、要遍历完 → 用 for；需要"中途条件退出" → 用 while
print("\n小结：for 适合完整遍历；while 适合带条件的游标控制")

# ==================== 第 3 部分：5 日均线（滑动窗口法） ====================
print("\n" + "=" * 45)
print("第3部分 · 5 日均线 MA5（for + 滑动窗口）")

# 思路：MA5[i] = 从第 i-4 天到第 i 天共 5 天的平均值
# 前 4 天不足 5 个数据 → 记 None（不参与计算）
ma5 = []
for i in range(len(closes)):
    if i < 4:
        ma5.append(None)                        # 窗口不满 5 天
    else:
        window = closes[i - 4:i + 1]            # 切片取 5 天
        ma5.append(round(sum(window) / 5, 2))   # 均值保留 2 位

for i in range(len(closes)):
    tag = f"{ma5[i]:.2f}" if ma5[i] is not None else "  --  "
    print(f"  {dates[i]}：收盘 {closes[i]:.2f}，MA5 = {tag}")

# 验证第 5 天的手算：前 5 天之和 / 5
check = sum(closes[:5]) / 5
print(f"\n验证：第 5 天 MA5 = ({' + '.join(str(c) for c in closes[:5])}) / 5 = {check:.2f}")

# ==================== 第 4 部分：5 日均线（增量滚动法，更高效） ====================
print("\n" + "=" * 45)
print("第4部分 · 5 日均线 MA5（while + 增量滚动）")

# 思路：保持一个"窗口和"，每走一天：窗口和 = 窗口和 - 出窗口价 + 进窗口价
window_sum = sum(closes[:5])                    # 第一个完整窗口的和
ma5_fast = [None] * 4 + [round(window_sum / 5, 2)]

t = 5
while t < len(closes):
    window_sum = window_sum - closes[t - 5] + closes[t]   # 减掉最旧，加进最新
    ma5_fast.append(round(window_sum / 5, 2))
    t += 1

# 两种算法结果应完全一致
same = ma5 == ma5_fast
print(f"增量法结果：{ma5_fast}")
print(f"与滑动窗口法完全一致：{same}")

# ==================== 综合练习：MA5 趋势判断 ====================
print("\n" + "=" * 45)
print("综合练习 · 用 MA5 看趋势（价格 vs 均线）")

print("日期    收盘价    MA5      价格vs均线")
for i in range(len(closes)):
    if ma5[i] is None:
        print(f"  {dates[i]}  {closes[i]:.2f}   --      蓄势（窗口不足）")
    else:
        diff = closes[i] - ma5[i]
        pos = "多头（价在线上）" if diff > 0 else ("空头（价在线下）" if diff < 0 else "贴线")
        print(f"  {dates[i]}  {closes[i]:.2f}   {ma5[i]:.2f}    {pos} ({diff:+.2f})")

# 趋势结论：比较最后一个 MA5 和最早一个 MA5
first_ma = next(m for m in ma5 if m is not None)
last_ma = ma5[-1]
trend = "上行" if last_ma > first_ma else ("下行" if last_ma < first_ma else "走平")
print(f"\n结论：MA5 从 {first_ma} 走到 {last_ma}，短期趋势{trend}")
print("提醒：均线是描述工具，不是买卖信号；本文为学习示例，不构成投资建议。")
