# Python 基础核心笔记

《三密三千大千世界》学习笔记

> **主题**：Python 基础语法  
> **日期**：2026-09-02  
> **状态**：✅ 已完成  
> **要点**：掌握变量/列表/字符串/条件/循环/函数/类/异常/文件/NumPy，为量化打基础

---

## 1. 变量与类型

```python
price = 100.5        # float
shares = 3           # int
name = "平安银行"     # str
is_profit = True     # bool
```

## 2. 列表（最常用容器）

```python
prices = [100.5, 101.2, 99.8]
prices.append(103.5)   # 添加
prices[0]              # 索引，第一个
prices[-1]             # 最后一个
prices[:2]             # 切片，前2个
```

## 3. 字符串

```python
name = "量化交易"
print(f"今日{name}")       # f-string 最常用
text.strip()               # 去空格
text.split(",")            # 分割
```

## 4. 条件与循环

```python
if profit > 0:
    print("盈利")
elif profit == 0:
    print("平盘")
else:
    print("亏损")

for p in prices:           # 遍历
    print(p)

total = sum(range(1, 101)) # 1到100求和
```

## 5. 函数

```python
def calc_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        returns.append((prices[i]-prices[i-1])/prices[i-1])
    return returns
```

## 6. 类

```python
class Stock:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def market_value(self, shares):
        return self.price * shares
```

## 7. 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为0")
```

## 8. 文件读写

```python
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("回测结果")
```

## 9. NumPy 向量化

```python
import numpy as np
prices = np.array([100, 102, 98, 105])
returns = np.diff(prices) / prices[:-1]   # 一步算收益率
prices.mean()  # 均值
```

## 10. 易错点

- 索引从 **0** 开始
- `=` 赋值，`==` 比较
- 字符串用 `+` 拼接，数字不能直接拼
- 浮点运算有精度误差（`0.1+0.2 != 0.3`）

---

*笔记状态：✅ 已完成*
