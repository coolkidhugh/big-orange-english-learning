# 英语学习网页应用部署指南

## 项目概述

这是一个功能完善的英语学习网页应用，具有以下特点：

1. 图片、英文单词和发音展示
2. 用户注册和登录系统
3. 图片、英文单词和音频上传功能
4. 测验功能（看图写英文/看中文写英文）
5. 测验历史记录

## 技术栈

- 后端：Flask + SQLAlchemy + MySQL
- 前端：HTML + CSS + JavaScript (Vue.js)
- 部署：GitHub + Render

## 本地开发环境设置

1. 克隆仓库
```bash
git clone https://github.com/yourusername/english-learning-app.git
cd english-learning-app
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置数据库
```bash
# 默认配置使用MySQL
# 数据库配置在src/main.py中
```

4. 导入示例数据
```bash
python -m src.seed_data
```

5. 运行应用
```bash
python -m src.main
```

6. 访问应用
```
http://localhost:5000
```

## 部署说明

### GitHub部署

1. 创建GitHub仓库
2. 推送代码到仓库
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/english-learning-app.git
git push -u origin main
```

### Render部署

1. 在Render上创建新的Web Service
2. 连接到GitHub仓库
3. 选择"Python"作为环境
4. 设置构建命令：`pip install -r requirements.txt`
5. 设置启动命令：`cd src && python main.py`
6. 添加环境变量（如需要）
7. 点击"Create Web Service"

## 使用指南

### 用户注册与登录

1. 点击右上角的"注册"按钮
2. 填写用户名、邮箱和密码
3. 提交注册表单
4. 使用注册的用户名和密码登录

### 浏览单词

1. 在首页可以浏览预设的英语单词和图片
2. 可以按类别筛选单词
3. 点击单词卡片可以播放发音（如果有）

### 上传单词

1. 点击侧边栏的"上传单词"
2. 填写英文单词和中文翻译
3. 上传对应的图片
4. 可选择上传音频文件
5. 点击"上传单词"按钮提交

### 进行测验

1. 点击侧边栏的"测验"
2. 选择测验类型（看图写英文/看中文写英文）
3. 设置题目数量
4. 选择是否包含自己上传的单词
5. 点击"开始测验"
6. 完成测验后可以查看得分和详细结果

### 查看历史记录

1. 点击侧边栏的"测验历史"
2. 查看过去的测验记录和得分
