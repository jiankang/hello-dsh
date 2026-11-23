# Contributing

这是一个用于验证 Git / GitHub 工作流的小项目，欢迎随手提改动。

## 环境要求

只需 Python 3.10 或更高版本，无需安装任何第三方依赖。

```bash
python3 --version
```

## 本地开发流程

```bash
# 1. 从 main 拉一个分支
git switch main
git pull
git switch -c fix/some-change

# 2. 改代码，然后跑测试
python3 -m unittest -v
python3 hello.py

# 3. 提交
git add -A
git commit -m "Your change in one line"

# 4. 推送并开 PR
git push -u origin fix/some-change
gh pr create --fill
```

## 提交信息约定

采用 [Conventional Commits](https://www.conventionalcommits.org/) 的简化形式：

```
<type>: <subject>
```

常用 `type`：

| type | 用途 |
| --- | --- |
| `feat` | 新增功能 |
| `fix` | 修复问题 |
| `docs` | 只改文档 |
| `test` | 只改测试 |
| `chore` | 构建、配置、依赖等杂项 |

示例：`feat: add greet option for custom separator`

## 代码风格

- 遵循 PEP 8，缩进 4 个空格
- 公共函数写 docstring，带类型注解
- 新增行为必须配套 `unittest` 测试

## 测试要求

CI 会在 Python 3.10 / 3.11 / 3.12 / 3.13 上跑 `.github/workflows/test.yml`。合并前请确认：

- [ ] 本地 `python3 -m unittest -v` 全部通过
- [ ] `python3 hello.py` 输出正常
- [ ] GitHub Actions 变绿

## 行为准则

保持友善、就事论事。人身攻击、骚扰和歧视性言论一律不接受。

## 许可

提交贡献即表示你同意以本仓库的 [MIT License](LICENSE) 发布你的改动。
