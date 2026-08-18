# ⚡ FastImage

基于 GitHub + jsDelivr 的免费无限量图床。

## 架构

```
PicGo 客户端 → GitHub 仓库 → jsDelivr CDN → 公网访问
                  ↑
          管理页面 (GitHub Pages)
```

| 组件 | 方案 |
|------|------|
| 图片存储 | GitHub 仓库 `neutron-star77/fastimage`（public） |
| CDN 加速 | jsDelivr `https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main/` |
| 上传工具 | PicGo v3 桌面客户端 |
| 管理页面 | 纯 HTML/JS，部署在 GitHub Pages |
| 文件路径 | `YYYY/MM/hash.ext` |
| 缓存刷新 | 上传/删除后自动 purge jsDelivr |

## 快速开始

### 1. 配置 PicGo 上传

参考 [PicGo 配置指南](./PicGo-Setup-Guide.md)

### 2. 访问管理页面

部署 GitHub Pages 后访问：
```
https://neutron-star77.github.io/fastimage/
```

### 3. CDN 链接格式

```
https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main/2026/08/xxxx.png
```

## 目录结构

```
/
├── docs/
│   ├── index.html          # 管理页面（GitHub Pages）
│   ├── agents/              # mp-engineering 配置
│   └── adr/                 # 架构决策记录
├── CLAUDE.md                # Agent 配置
├── README.md
├── PicGo-Setup-Guide.md     # PicGo 配置指南
└── 2026/                    # 图片存储（按年/月）
    └── 08/
        └── a1b2c3d4.png
```

## 技术选型

- **GitHub**: 免费 public 仓库，无限存储
- **jsDelivr**: 免费 CDN，全球加速，自动 HTTPS
- **PicGo**: 开源图片上传客户端，支持 GitHub 图床
- **纯前端管理页面**: 无后端，Token 存浏览器 localStorage，GitHub API 操作仓库

## 限制

- GitHub 单文件上限 100MB（jsDelivr 缓存上限 50MB）
- GitHub API 限速：认证用户 5000 次/小时
- jsDelivr 缓存延迟：上传后自动 purge 可消除
