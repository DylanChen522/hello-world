# 虚拟环境 venv + 依赖管理

《三密三千大千世界》学习笔记

> **主题**：Python 虚拟环境与依赖管理  
> **日期**：2026-09-02  
> **状态**：✅ 已完成  
> **要点**：venv 隔离环境 + pip 安装 + requirements.txt 复现依赖

---

## 1. 为什么需要虚拟环境？

**问题**：不同项目需要不同版本的包（如 A 项目要 numpy 1.x，B 项目要 2.x），全部装在一起会冲突。

**方案**：每个项目建独立环境，互不干扰。

| 对比 | 无虚拟环境 | 有虚拟环境 |
|------|-----------|-----------|
| 包隔离 | ❌ 全局共享 | ✅ 项目独立 |
| 版本冲突 | 常见 | 避免 |
| 复现部署 | 难 | 简单（requirements） |

## 2. 创建与使用 venv

```bash
# 创建虚拟环境（在项目目录下）
python -m venv venv

# Windows 激活
venv\Scripts\activate

# macOS/Linux 激活
source venv/bin/activate

# 退出
deactivate
```

> **核心认知**：激活后，`python` / `pip` 都指向项目内的 venv，与全局隔离。

## 3. pip 依赖安装

```bash
# 安装包
python -m pip install numpy pandas

# 指定版本
python -m pip install numpy==2.5.2

# 安装到 requirements.txt
python -m pip install -r requirements.txt

# 卸载
python -m pip uninstall numpy

# 查看已装
python -m pip list
```

## 4. requirements.txt（依赖清单）

```bash
# 导出当前环境所有依赖及版本
python -m pip freeze > requirements.txt

# 内容示例
# numpy==2.5.2
# pandas==3.0.5

# 他人/新环境一键复现
python -m pip install -r requirements.txt
```

**最佳实践**：`requirements.txt` 提交到 Git 仓库，别人克隆后一条命令即可搭建相同环境。

## 5. 项目结构（含 venv）

```
my_project/
├── venv/               # 虚拟环境（不提交Git）
├── src/
├── requirements.txt    # 依赖清单（提交Git）
└── .gitignore
```

## 6. .gitignore 必须忽略 venv

```gitignore
venv/
```

## 7. 易错点 / 踩坑记录

### ⚠️ pip.conf 编码错误（实测踩坑）
- 现象：`pip` 报 `Configuration file contains invalid utf-8 characters`
- 原因：pip.conf 中 `cache-dir` 含中文用户名，被写成 GBK 乱码字节
- 解决：用**无 BOM 的 UTF-8** 重写 pip.conf（含中文路径用正斜杠 `C:/Users/...`）

### ⚠️ 其他
- Windows 激活脚本在 PowerShell 需 `venv\Scripts\activate`
- 装了包但 import 失败 → 检查是否激活了正确环境

---

*笔记状态：✅ 已完成*
