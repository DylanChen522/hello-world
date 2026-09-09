# -*- coding: utf-8 -*-
"""
《三密三千大千世界》· 事业线 · Python 筑基练习
=============================================
主题：pandas 数据分析入门 —— 真实行情分析（阶段② 数据期）
场景：用 akshare（腾讯通道）拉取贵州茅台真实日线，算收益率、看波动、画走势
运行：python 04-pandas数据分析-茅台行情.py
依赖：pip install pandas matplotlib akshare（已装入 venv）
"""

# ==================== 第 1 步：取数 ====================
# akshare 腾讯通道（东财通道偶发断连，腾讯更稳定），拉取 A 股日线（前复权）
import pandas as pd
import akshare as ak

df = ak.stock_zh_a_hist_tx(
    symbol="sh600519",        # 贵州茅台（上交所前缀 sh）
    start_date="20260801",    # 起始日期
    end_date="20260905",      # 结束日期
    adjust="qfq",             # 前复权
)

print("=" * 45)
print("第1步 · 拉取真实行情")
print(f"数据条数：{len(df)} 天")
print(f"字段：{list(df.columns)}")

# 用日期做索引
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# 自行计算涨跌幅（腾讯接口不直接给）
df["pct_chg"] = df["close"].pct_change() * 100
print(df.head(3))

# ==================== 第 2 步：pandas 核心操作 ====================
print("\n" + "=" * 45)
print("第2步 · pandas 基础操作")
print(f"区间最高收盘价：{df['close'].max():.2f}")
print(f"区间最低收盘价：{df['close'].min():.2f}")
print(f"平均收盘价：{df['close'].mean():.2f}")
print(f"总成交量（股）：{df['volume'].sum():,.0f}")

# 条件筛选：找出涨幅超过 1% 的日子
big_days = df[df["pct_chg"] > 1]
print(f"涨幅>1% 的天数：{len(big_days)} 天")
print(big_days[["close", "pct_chg"]])

# ==================== 第 3 步：算收益率（核心） ====================
print("\n" + "=" * 45)
print("第3步 · 计算收益率")
# 单日收益率 = 今日收盘 / 昨日收盘 - 1
df["daily_ret"] = df["close"].pct_change()
# 累计收益率（从区间起点算起，复利）
df["cum_ret"] = (1 + df["daily_ret"]).cumprod() - 1
print(df[["close", "daily_ret", "cum_ret"]].tail(5))

# 区间总收益
total_ret = df["cum_ret"].iloc[-1]
print(f"区间累计收益：{total_ret * 100:.2f}%")

# 波动率（日收益率标准差，衡量风险）
vol = df["daily_ret"].std()
print(f"日波动率（标准差）：{vol * 100:.2f}%")

# ==================== 第 4 步：可视化 ====================
print("\n" + "=" * 45)
print("第4步 · 画走势图")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]  # 中文显示
plt.rcParams["axes.unicode_minus"] = False

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

# 上图：收盘价走势
axes[0].plot(df.index, df["close"], color="#1f77b4", linewidth=1.8)
axes[0].set_title("贵州茅台 2026-08 至 09 收盘价走势（真实数据）")
axes[0].set_ylabel("收盘价（元）")
axes[0].grid(alpha=0.3)

# 下图：每日收益率
axes[1].bar(df.index, df["daily_ret"] * 100, color=[
    "#d62728" if r >= 0 else "#2ca02c" for r in df["daily_ret"]
])
axes[1].axhline(0, color="gray", linewidth=0.8)
axes[1].set_title("每日收益率（%）")
axes[1].set_ylabel("收益率（%）")
plt.tight_layout()
plt.savefig("assets/maotai_analysis.png", dpi=120, bbox_inches="tight")
print("图表已保存：assets/maotai_analysis.png")

# ==================== 第 5 步：一句话结论 ====================
print("\n" + "=" * 45)
print("结论")
print(f"茅台该区间累计收益 {total_ret * 100:.2f}%，日波动率 {vol * 100:.2f}%，"
      f"最大单日涨幅 {df['pct_chg'].max():.2f}%，最大单日跌幅 {df['pct_chg'].min():.2f}%。")
