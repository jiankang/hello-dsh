# hello-dsh

一个用于验证 Git / GitHub 工作流的测试项目。

## 内容

- `hello.py` — 一个打印问候语的小脚本
- `test_hello.py` — 对应的单元测试

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

## 环境

本仓库用于确认：本地提交、远程推送、CI 之外的基本协作流程均可正常工作。
