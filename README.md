# 🎨 OpenCV Logo 综合项目

基于 OpenCV 的图像处理项目，实现将 OpenCV logo 无缝融合到 Lena 图片中。

## ✨ 项目功能

- 📷 **图像读取** - 读取 Lena 原图和 OpenCV logo
- ✂️ **ROI 提取** - 从 Lena 图片中提取右下角感兴趣区域
- 🎚️ **灰度转换** - 将 logo 转换为灰度图
- 🎭 **掩码生成** - 通过二值化生成前景和背景掩码
- 🔧 **按位运算** - 使用 bitwise_and 分离前景和背景
- ➕ **图像融合** - 将 logo 与背景图无缝叠加

## 📁 项目结构

```
opencv_logo_split_join/
├── Opencv+logo综合项目.py    # 主程序文件
├── picture/                  # 图片文件夹
│   ├── lena03.png           # Lena 原图
│   └── OpenCV-logo.png      # OpenCV logo
└── README.md                 # 项目说明
```

## 🚀 快速开始

### 环境要求

- Python 3.6+
- OpenCV 4.x

### 安装依赖

```bash
pip install opencv-python
```

### 运行程序

```bash
python "Opencv+logo综合项目.py"
```

## 📖 实现原理

### 核心步骤

| 步骤 | 操作 | 说明 |
|------|------|------|
| 1 | 读取图片 | 加载 Lena 和 logo 图像 |
| 2 | 提取 ROI | 获取 Lena 右下角区域 |
| 3 | 灰度转换 | 将 logo 转为灰度图 |
| 4 | 二值化 | 生成掩码（阈值 220） |
| 5 | 背景提取 | 保留背景，挖空 logo 区域 |
| 6 | 前景提取 | 保留 logo，挖空背景 |
| 7 | 图像相加 | 融合前景和背景 |
| 8 | 更新 ROI | 将融合结果放回原图 |

### 代码流程图

```
Lena原图 ──→ 提取ROI ──→ 与fig1相加 ──→ 更新ROI ──→ 显示结果
                    ↑
OpenCV Logo ──→ 灰度图 ──→ 二值化 ──→ 生成mask
                              ↓
                    ┌─────────┴─────────┐
                    ↓                   ↓
                  mask1               mask2
              (THRESH_BINARY)     (THRESH_BINARY_INV)
                    ↓                   ↓
                fig1(背景)           fig2(前景)
                    └─────────┬─────────┘
                              ↓
                          cv2.add()
```

## 🎯 关键代码解析

### 1. 提取 ROI
```python
h1, w1 = lena.shape[:2]
h2, w2 = logo.shape[:2]
roi = lena[h1-h2:h1, w1-w2:w1]
```

### 2. 生成掩码
```python
# 保留背景（挖空 logo 前景）
_, mask1 = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

# 保留 logo 前景（挖空背景）
_, mask2 = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
```

### 3. 按位运算
```python
# 提取背景部分
fig1 = cv2.bitwise_and(roi, roi, None, mask=mask1)

# 提取 logo 前景部分
fig2 = cv2.bitwise_and(logo, logo, None, mask=mask2)
```

### 4. 图像融合
```python
# 将背景和前景相加
roi[:] = cv2.add(fig1, fig2)
```

## 📊 显示效果

程序运行后会依次显示以下窗口：

1. **roi** - 提取的 Lena 右下角区域
2. **roi_gray** - logo 灰度图
3. **mask1** - 背景掩码（白色为背景区域）
4. **mask2** - 前景掩码（白色为 logo 区域）
5. **fig1** - 只有背景的局部图
6. **fig2** - 只有 logo 前景的局部图
7. **lena_new** - 最终融合结果（调整大小为 512×512）

按任意键关闭所有窗口。

## 🔧 参数说明

| 参数 | 值 | 说明 |
|------|-----|------|
| 二值化阈值 | 220 | 控制 logo 前景提取精度 |
| 输出尺寸 | 512×512 | 最终显示图像大小 |

## 💡 应用场景

- 图像水印添加
- Logo 融合
- 图像合成
- ROI 区域处理
- 掩码操作练习

## ⚠️ 注意事项

1. **图片路径**：确保 `picture` 文件夹与脚本在同一目录
2. **图片名称**：确认图片名为 `lena03.png` 和 `OpenCV-logo.png`
3. **阈值调整**：可根据 logo 背景颜色调整二值化阈值
4. **图片大小**：确保 logo 尺寸不大于 Lena 图片

## 🐛 常见问题

### Q: 提示图片找不到？
A: 检查 `picture` 文件夹是否存在，图片名称是否正确。

### Q: 显示效果不理想？
A: 尝试调整二值化阈值（当前为 220），或检查 logo 背景颜色。

### Q: ROI 区域超出范围？
A: 确保 logo 尺寸小于 Lena 图片。

## 📝 版本历史

### v1.0.0
- 实现基础 logo 融合功能
- 支持 ROI 提取和掩码操作
- 完成图像按位运算和加法融合

## 👨‍💻 作者

- **GitHub**: [@y1733133864](https://github.com/y1733133864)

---

**OpenCV 图像处理 · Logo 融合实战** 🎨

```
