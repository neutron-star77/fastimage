# FastImage 图床 — 完整搭建指南

> 本文件遵循 CodeBuddy skill 规范，可被 CodeBuddy 自动读取。

## 项目概况

| 项 | 说明 |
|----|------|
| 目标 | 用 GitHub + jsDelivr 自建免费无限量图床 |
| 上传方式 | PicGo 桌面客户端 |
| 管理页面 | 纯 HTML/JS，部署在 GitHub Pages |
| 项目目录 | `F:\AI\projects\fastimage` |
| GitHub 仓库 | `neutron-star77/fastimage`（public） |
| CDN 地址 | `https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main/` |
| 管理页面地址 | `https://neutron-star77.github.io/fastimage/` |

## 已完成

1. git 仓库初始化 + 关联远程 origin
2. mp-engineering 配置 — CLAUDE.md, docs/agents/, docs/adr/
3. 管理页面 docs/index.html（浏览/上传/删除/搜索/统计/Lightbox）
4. PicGo 配置指南 — PicGo-Setup-Guide.md
5. PicGo v3.0.2 安装包已下载（不入 git）
6. README.md + .gitignore

## 待完成步骤

### 步骤 1：推送代码

```powershell
cd "F:\AI\projects\fastimage"
git add -A
git commit -m "init: FastImage 图床项目初始化"
git branch -M main
git push -u origin main
```

### 步骤 2：启用 GitHub Pages

1. 打开 https://github.com/neutron-star77/fastimage/settings/pages
2. Source: Deploy from a branch
3. Branch: main / Folder: /docs
4. Save

### 步骤 3：创建 GitHub Token

1. https://github.com/settings/personal-access-tokens/new
2. Repository: Only neutron-star77/fastimage
3. Permissions: Contents = Read and write
4. 复制 Token

### 步骤 4：安装配置 PicGo

1. 运行 `F:\AI\projects\fastimage\PicGo-3.0.2-x64.exe`
2. 图床设置 → GitHub：
   - 仓库: neutron-star77/fastimage
   - 分支: main
   - Token: 步骤3的Token
   - 自定义域名: https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main
3. 安装插件 picgo-plugin-rename-file，格式: {year}/{month}/{md5}.{extName}
4. 设为默认图床

### 步骤 5：验证

1. PicGo 拖一张图上传
2. 打开 https://neutron-star77.github.io/fastimage/ 输入Token登录
3. 看到图片网格即成功

## CDN 链接格式

```
https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main/2026/08/哈希值.png
```

## 注意事项

- 单文件上限 100MB（jsDelivr 50MB）
- 仓库必须 public
- Token 存浏览器 localStorage
- GitHub API 限速 5000次/小时

## 故障排除

| 问题 | 解决 |
|------|------|
| 页面打不开 | 检查 Pages 设置 main /docs |
| 登录失败 | 检查 Token 权限 Contents Read and Write |
| 上传失败 | 检查 Token 过期 / 仓库名 |
| CDN 404 | 检查文件路径 / purge 缓存 |
| 缓存旧 | https://purge.jsdelivr.net/gh/neutron-star77/fastimage@main/路径 |
