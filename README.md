# hello-dsh

[![Tests](https://github.com/jiankang/hello-dsh/actions/workflows/test.yml/badge.svg)](https://github.com/jiankang/hello-dsh/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个用于验证 Git / GitHub 工作流的测试项目。

## 内容

| 文件 | 说明 |
| --- | --- |
| `hello.py` | 一个打印问候语的小脚本 |
| `test_hello.py` | 对应的单元测试 |
| `.github/workflows/test.yml` | CI：在多个 Python 版本上自动跑测试 |
| `CONTRIBUTING.md` | 贡献指南 |
| `LICENSE` | MIT 许可证 |

## 运行

```bash
python3 hello.py
```

输出：

```
Hello, DeepSeek Harness!
```

## 测试

```bash
python3 -m unittest -v
```

## 持续集成

每次向 `main` 推送或发起 PR，都会触发 GitHub Actions，在 Python 3.10 / 3.11 / 3.12 / 3.13 上分别执行单元测试和脚本冒烟测试。状态见页面顶部的徽章。

## 环境

只需 Python 3.10 及以上，无第三方依赖。

## 许可

[MIT](LICENSE)
