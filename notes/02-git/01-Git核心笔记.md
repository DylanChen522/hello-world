# Git / GitHub 核心笔记

《三密三千大千世界》学习笔记

> **主题**：Git 版本控制 + GitHub 协作  
> **日期**：2026-09-02  
> **状态**：✅ 已完成  
> **要点**：掌握 add/commit/push 闭环，SSH 免密推送

---

## 1. 三个区域

| 区域 | 含义 | 命令 |
|------|------|------|
| 工作区 | 正在编辑的文件 | 直接操作 |
| 暂存区 | 待提交清单 | `git add` |
| 仓库 | 历史版本 | `git commit` |

## 2. 核心命令（每天只用这些）

```bash
git status                 # 查看状态（最常用）
git add .                  # 暂存所有修改
git commit -m "说明"       # 提交
git push                   # 推送到GitHub
git pull                   # 拉取最新
git log --oneline          # 查看历史
```

## 3. 首次配置

```bash
git config --global user.name "DylanChen522"
git config --global user.email "Cdy55@126.com"
git config --global init.defaultBranch main
```

## 4. 关联远程仓库

```bash
git remote add origin git@github.com:DylanChen522/hello-world.git
git push -u origin main     # 首次推送
```

## 5. 易错点（中文用户名坑）

- Windows 用户名含中文会导致 git 内置 SSH 找不到密钥
- 解决：配置 ASCII 路径密钥
```bash
git config --global core.sshCommand "ssh -i C:/Users/Public/.ssh/id_ed25519 -o StrictHostKeyChecking=accept-new -o UserKnownHostsFile=C:/Users/Public/.ssh/known_hosts"
```

## 6. 口诀

```
改 → add → commit → push    # 日常四步
```

---

*笔记状态：✅ 已完成*
