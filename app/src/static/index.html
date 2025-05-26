<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>大橙子英文学习</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
    <style>
        :root {
            --primary-color: #FF8C00;
            --secondary-color: #f8f9fc;
            --accent-color: #f6c23e;
            --success-color: #1cc88a;
            --danger-color: #e74a3b;
            --dark-color: #5a5c69;
        }
        
        body {
            font-family: 'Nunito', 'Segoe UI', Roboto, Arial, sans-serif;
            background-color: #f8f9fc;
        }
        
        .navbar {
            background-color: white;
            box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
        }
        
        .navbar-brand {
            font-weight: 700;
            color: var(--primary-color);
        }
        
        .sidebar {
            min-height: calc(100vh - 56px);
            background: linear-gradient(180deg, var(--primary-color) 10%, #E67300 100%);
            box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
        }
        
        .sidebar-link {
            color: rgba(255, 255, 255, 0.8);
            font-weight: 600;
            padding: 1rem;
            border-radius: 0.35rem;
            transition: all 0.2s;
        }
        
        .sidebar-link:hover, .sidebar-link.active {
            color: white;
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        .sidebar-link i {
            margin-right: 0.5rem;
        }
        
        .content {
            padding: 1.5rem;
        }
        
        .card {
            border: none;
            border-radius: 0.35rem;
            box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.1);
            margin-bottom: 1.5rem;
        }
        
        .card-header {
            background-color: white;
            border-bottom: 1px solid #e3e6f0;
            font-weight: 700;
            color: var(--dark-color);
        }
        
        .word-card {
            transition: transform 0.2s;
            cursor: pointer;
            height: 100%;
        }
        
        .word-card:hover {
            transform: translateY(-5px);
        }
        
        .word-image {
            height: 150px;
            object-fit: cover;
        }
        
        .btn-primary {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
        }
        
        .btn-primary:hover {
            background-color: #E67300;
            border-color: #E67300;
        }
        
        .login-container, .register-container {
            max-width: 450px;
            margin: 2rem auto;
        }
        
        .quiz-card {
            max-width: 600px;
            margin: 0 auto;
        }
        
        .quiz-image {
            max-height: 250px;
            object-fit: contain;
        }
        
        .upload-preview {
            max-height: 200px;
            max-width: 100%;
            margin-top: 1rem;
        }
        
        .audio-control {
            width: 100%;
        }
        
        .category-badge {
            background-color: var(--primary-color);
            color: white;
            font-size: 0.8rem;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
        }
        
        .result-card {
            border-left: 4px solid;
        }
        
        .result-card.correct {
            border-left-color: var(--success-color);
        }
        
        .result-card.incorrect {
            border-left-color: var(--danger-color);
        }
        
        @media (max-width: 768px) {
            .sidebar {
                min-height: auto;
            }
        }
    </style>
</head>
<body>
    <div id="app">
        <!-- 导航栏 -->
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">大橙子英文学习</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item" v-if="!isLoggedIn">
                            <a class="nav-link" href="#" @click="showLogin">登录</a>
                        </li>
                        <li class="nav-item" v-if="!isLoggedIn">
                            <a class="nav-link" href="#" @click="showRegister">注册</a>
                        </li>
                        <li class="nav-item dropdown" v-if="isLoggedIn">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
                                {{ currentUser.username }}
                            </a>
                            <ul class="dropdown-menu dropdown-menu-end">
                                <li><a class="dropdown-item" href="#" @click="logout">退出登录</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container-fluid">
            <div class="row">
                <!-- 侧边栏 -->
                <div class="col-md-3 col-lg-2 d-md-block sidebar collapse">
                    <div class="position-sticky pt-3">
                        <ul class="nav flex-column">
                            <li class="nav-item">
                                <a class="nav-link sidebar-link" :class="{ active: currentPage === 'home' }" href="#" @click="changePage('home')">
                                    <i class="bi bi-house-door"></i> 首页
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link sidebar-link" :class="{ active: currentPage === 'upload' }" href="#" @click="changePage('upload')">
                                    <i class="bi bi-cloud-upload"></i> 上传单词
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link sidebar-link" :class="{ active: currentPage === 'mywords' }" href="#" @click="changePage('mywords')">
                                    <i class="bi bi-journal-text"></i> 我的单词
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link sidebar-link" :class="{ active: currentPage === 'quiz' }" href="#" @click="changePage('quiz')">
                                    <i class="bi bi-pencil-square"></i> 测验
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link sidebar-link" :class="{ active: currentPage === 'history' }" href="#" @click="changePage('history')">
                                    <i class="bi bi-clock-history"></i> 测验历史
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- 主内容区 -->
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 content">
                    <!-- 登录页面 -->
                    <div v-if="currentPage === 'login'" class="login-container">
                        <div class="card">
                            <div class="card-header">
                                <h5 class="mb-0">用户登录</h5>
                            </div>
                            <div class="card-body">
                                <div class="alert alert-danger" v-if="loginError">{{ loginError }}</div>
                                <form @submit.prevent="login">
                                    <div class="mb-3">
                                        <label for="username" class="form-label">用户名</label>
                                        <input type="text" class="form-control" id="username" v-model="loginForm.username" required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="password" class="form-label">密码</label>
                                        <input type="password" class="form-control" id="password" v-model="loginForm.password" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary w-100">登录</button>
                                </form>
                                <div class="text-center mt-3">
                                    <p>还没有账号？ <a href="#" @click="showRegister">立即注册</a></p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 注册页面 -->
                    <div v-if="currentPage === 'register'" class="register-container">
                        <div class="card">
                            <div class="card-header">
                                <h5 class="mb-0">用户注册</h5>
                            </div>
                            <div class="card-body">
                                <div class="alert alert-danger" v-if="registerError">{{ registerError }}</div>
                                <form @submit.prevent="register">
                                    <div class="mb-3">
                                        <label for="reg-username" class="form-label">用户名</label>
                                        <input type="text" class="form-control" id="reg-username" v-model="registerForm.username" required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="reg-email" class="form-label">邮箱</label>
                                        <input type="email" class="form-control" id="reg-email" v-model="registerForm.email" required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="reg-password" class="form-label">密码</label>
                                        <input type="password" class="form-control" id="reg-password" v-model="registerForm.password" required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="reg-confirm-password" class="form-label">确认密码</label>
                                        <input type="password" class="form-control" id="reg-confirm-password" v-model="registerForm.confirmPassword" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary w-100">注册</button>
                                </form>
                                <div class="text-center mt-3">
                                    <p>已有账号？ <a href="#" @click="showLogin">立即登录</a></p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 首页 -->
                    <div v-if="currentPage === 'home'">
                        <div class="d-flex justify-content-between align-items-center mb-4">
                            <h2>英语单词学习</h2>
                            <div class="d-flex">
                                <select class="form-select me-2" v-model="selectedCategory" @change="loadPresetWords">
                                    <option value="">所有类别</option>
                                    <option value="animals">动物</option>
                                    <option value="food">食物</option>
                                    <option value="daily">日常用品</option>
                                    <option value="nature">自然</option>
                                    <option value="transport">交通</option>
                                </select>
                                <button class="btn btn-outline-primary" @click="loadPresetWords">刷新</button>
                            </div>
                        </div>

                        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4">
                            <div class="col" v-for="word in presetWords" :key="word.id">
                                <div class="card word-card" @click="playAudio(word)">
                                    <img :src="getImageUrl(word.image_path)" class="card-img-top word-image" :alt="word.english">
                                    <div class="card-body">
                                        <h5 class="card-title">{{ word.english }}</h5>
                                        <p class="card-text">{{ word.chinese }}</p>
                                        <span class="category-badge" v-if="word.category">{{ word.category }}</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <nav class="mt-4">
                            <ul class="pagination justify-content-center">
                                <li class="page-item" :class="{ disabled: currentPresetPage === 1 }">
                                    <a class="page-link" href="#" @click.prevent="changePage('home', currentPresetPage - 1)">上一页</a>
                                </li>
                                <li class="page-item" v-for="page in presetTotalPages" :key="page" :class="{ active: currentPresetPage === page }">
                                    <a class="page-link" href="#" @click.prevent="changePage('home', page)">{{ page }}</a>
                                </li>
                                <li class="page-item" :class="{ disabled: currentPresetPage === presetTotalPages }">
                                    <a class="page-link" href="#" @click.prevent="changePage('home', currentPresetPage + 1)">下一页</a>
                                </li>
                            </ul>
                        </nav>
                    </div>

                    <!-- 上传单词页面 -->
                    <div v-if="currentPage === 'upload'">
                        <div class="card">
                            <div class="card-header">
                                <h5 class="mb-0">上传新单词</h5>
                            </div>
                            <div class="card-body">
                                <div class="alert alert-success" v-if="uploadSuccess">{{ uploadSuccess }}</div>
                                <div class="alert alert-danger" v-if="uploadError">{{ uploadError }}</div>
                                <form @submit.prevent="uploadWord">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <div class="mb-3">
                                                <label for="english" class="form-label">英文单词</label>
                                                <input type="text" class="form-control" id="english" v-model="uploadForm.english" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="chinese" class="form-label">中文翻译</label>
                                                <input type="text" class="form-control" id="chines
(Content truncated due to size limit. Use line ranges to read in chunks)
