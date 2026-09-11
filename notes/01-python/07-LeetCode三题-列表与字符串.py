# -*- coding: utf-8 -*-
"""
《三密三千大千世界》· 事业线 · Python 筑基练习
=============================================
主题：LeetCode 简单题 3 道（列表 / 字符串类）
题单：1. 两数之和 ｜ 26. 删除有序数组中的重复项 ｜ 125. 验证回文串
场景：用刷题把「列表遍历 / 哈希表 / 双指针 / 字符串清洗」练扎实
运行：python 07-LeetCode三题-列表与字符串.py
"""

# ==================== 第 1 题：两数之和（LeetCode 1） ====================
"""
题目：给定整数数组 nums 和目标值 target，找出和为目标值的两个整数，
     返回它们的下标。每种输入只有唯一答案，同一元素不能用两次。
示例：nums = [2, 7, 11, 15], target = 9 → [0, 1]（因为 2 + 7 = 9）

思路（哈希表一遍遍历）：
  边遍历边把"见过的数"存进字典（值 → 下标）。
  对当前数 x，只需要查 target - x 在不在字典里。
  时间 O(n)，空间 O(n)——比双重循环 O(n²) 快得多。
"""
print("=" * 45)
print("第1题 · 两数之和（列表 + 哈希表）")


def two_sum(nums, target):
    seen = {}                        # 字典：{数值: 下标}，记录"已经路过"的数
    for i, x in enumerate(nums):     # 遍历时同时拿下标
        need = target - x            # 需要的另一半
        if need in seen:             # 之前遇到过 → 找到答案
            return [seen[need], i]
        seen[x] = i                  # 没找到就登记当前数，供后面查
    return []                        # 题目保证有解，这里兜底


# 验证
cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]
for nums, target, expect in cases:
    got = two_sum(nums, target)
    mark = "✓" if got == expect else "✗"
    print(f"  {mark} nums={nums}, target={target} → {got}（期望 {expect}）")

# ==================== 第 2 题：删除有序数组中的重复项（LeetCode 26） ====================
"""
题目：给定升序数组 nums，原地删除重复元素，使每个元素只出现一次。
     返回新长度 k；要求 nums 前 k 位就是不重复的升序序列，不关心后面。
示例：nums = [1,1,2] → 返回 2，nums 前 2 位变为 [1,2]

思路（快慢双指针，原地）：
  慢指针 k 指向"下一个不重复元素该放的位置"；
  快指针 i 往后扫，发现 nums[i] != nums[k-1]（新数）就往前放。
  因为数组有序，重复元素必然相邻，只需跟前一个比较。
  空间 O(1)，时间 O(n)。
"""
print("\n" + "=" * 45)
print("第2题 · 删除有序数组中的重复项（列表 + 双指针）")


def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1                                # 第一个元素一定保留
    for i in range(1, len(nums)):        # 从第 2 个开始扫
        if nums[i] != nums[k - 1]:       # 和前一个"已保留"的元素不同
            nums[k] = nums[i]            # 放到保留区末尾
            k += 1
    return k                             # k 就是不重复元素个数


# 验证
for nums in ([1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [1, 2, 3]):
    orig = list(nums)
    k = remove_duplicates(nums)
    print(f"  ✓ {orig} → k={k}，前{k}位={nums[:k]}")

# ==================== 第 3 题：验证回文串（LeetCode 125） ====================
"""
题目：给定字符串 s，只考虑字母和数字字符，忽略大小写，判断它是否回文。
     空串视为有效回文。
示例："A man, a plan, a canal: Panama" → True（忽略标点空格后是回文）
     "race a car" → False

思路（字符串清洗 + 双指针）：
  第一步：过滤——只保留字母和数字，统一转小写；
  第二步：双指针——左指针从左、右指针从右往中间走，逐位比较。
  时间 O(n)，空间 O(n)（清洗后的新串）。
"""
print("\n" + "=" * 45)
print("第3题 · 验证回文串（字符串 + 双指针）")


def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())  # 清洗：字母数字 + 小写
    left, right = 0, len(cleaned) - 1
    while left < right:                # 双指针向中间靠拢
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# 验证
pal_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("0P", False),                     # '0' 和 'p' 不同（数字 vs 字母）
    ("上海自来水来自海上", True),       # 中文也适用（无标点清洗需求时）
]
for s, expect in pal_cases:
    got = is_palindrome(s)
    mark = "✓" if got == expect else "✗"
    print(f"  {mark} {s!r} → {got}（期望 {expect}）")

# ==================== 小结：三题覆盖的核心套路 ====================
print("\n" + "=" * 45)
print("小结 · 三个可复用的套路")
print("  1. 哈希表（字典）：用空间换时间，把 O(n²) 的查找降成 O(n)")
print("  2. 双指针：有序数组去重、回文判断这类问题，一个指针负责定位、")
print("     一个指针负责扫描，常能原地完成，空间 O(1)")
print("  3. 字符串清洗：先过滤/归一化（isalnum + lower），再判断，")
print("     把'带杂质的输入'变干净，后续逻辑就简单了")
