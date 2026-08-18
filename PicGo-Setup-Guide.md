# PicGo 配置指南

## 1. 安装 PicGo

运行 `F:\AI\projects\fastimage\PicGo-3.0.2-x64.exe` 安装。

## 2. 创建 GitHub Token

1. 打开 https://github.com/settings/personal-access-tokens/new
2. Token name: `fastimage-upload`
3. Expiration: 选 1 年或自定义
4. Repository access: Only select repositories → `neutron-star77/fastimage`
5. Permissions → Repository permissions → Contents: Read and write
6. 生成后复制 Token

## 3. 配置 PicGo GitHub 图床

打开 PicGo → 图床设置 → GitHub 图床：

| 设置项 | 值 |
|--------|-----|
| 仓库名 | `neutron-star77/fastimage` |
| 分支名 | `main` |
| Token | 粘贴你刚才创建的 Token |
| 存储路径 | 留空（自动按 年/月/ 创建） |
| 自定义域名 | `https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main` |

## 4. 安装重命名插件

PicGo 默认用原文件名上传。要实现「年/月/哈希命名」，需要安装重命名插件：

1. PicGo → 插件设置 → 搜索 `rename-file`
2. 安装 `picgo-plugin-rename-file`
3. 在插件设置中配置重命名格式：
   ```
   {year}/{month}/{md5}.{extName}
   ```

> 如果 `picgo-plugin-rename-file` 不可用，备选方案：
> - `picgo-plugin-super-prefix`（支持日期+哈希前缀）
> - 或在 PicGo 的「上传前重命名」中手动改文件名

## 5. 验证

1. 拖一张测试图片到 PicGo
2. 检查 GitHub 仓库是否出现 `2026/08/xxxxxxxx.png` 文件
3. 访问 `https://cdn.jsdelivr.net/gh/neutron-star77/fastimage@main/2026/08/xxxxxxxx.png` 确认 CDN 可用
4. 打开管理页面（GitHub Pages 部署后）查看图片

## 6. jsDelivr 缓存刷新

PicGo 上传后，jsDelivr CDN 可能有缓存延迟。管理页面内置了上传/删除后自动刷新缓存的逻辑。

如需手动刷新某个图片的缓存：
```
https://purge.jsdelivr.net/gh/neutron-star77/fastimage@main/路径/文件名.png
```
