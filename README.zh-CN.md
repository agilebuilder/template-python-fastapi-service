# <%= projectName %>

<% var pkg = packageDir.charAt(0) === '<' ? snakeCase(projectName) : packageDir -%>
<%= description %>

基于 FastAPI + SQLAlchemy 2.x（asyncio）+ Pydantic v2 的异步 API 服务，src 布局，pyproject.toml（hatchling）管理依赖与打包。

## 技术栈

- Python <%= pythonVersion %>
- FastAPI（Web 框架）+ Uvicorn（ASGI 服务器）
- SQLAlchemy 2.x 异步 ORM（默认 SQLite + aiosqlite，可切换其他数据库）
- Pydantic v2 + pydantic-settings（数据校验与配置管理）
- pytest + pytest-asyncio + httpx AsyncClient（异步测试）
- Ruff（lint 与格式化）

## 目录结构

```
├── src/<%= pkg %>/          # Python 包
│   ├── main.py             # 应用入口：create_app() 工厂、uvicorn 启动
│   ├── api/                # 路由层
│   │   ├── router.py       # 路由聚合
│   │   └── routes/         # health / items 示例路由
│   ├── core/               # 配置（pydantic-settings）
│   ├── db/                 # 异步引擎与会话管理
│   ├── models/             # SQLAlchemy ORM 模型
│   ├── schemas/            # Pydantic 请求/响应模型
│   └── services/           # 业务逻辑层
├── tests/                  # pytest + httpx AsyncClient 示例测试
├── pyproject.toml          # 项目元数据、依赖、pytest/ruff 配置
└── .env.example            # 环境变量示例
```

## 使用本模板创建项目

```bash
ag create --git-url <仓库地址> --target <目录>
```

### 模板变量

| 变量名 | 说明 | 默认值 |
| --- | --- | --- |
| projectName | 项目名称（分发名） | demo-api |
| packageDir | Python 包目录名 | 由 projectName 自动转为 snake_case |
| description | 项目描述 | 一个 FastAPI 服务 |
| author | 作者 | （空） |
| port | 服务端口 | 8000 |
| pythonVersion | Python 版本（3.11 / 3.12） | 3.12 |

## 快速开始

```bash
# 创建虚拟环境并安装依赖（含 dev 依赖）
python -m venv .venv
source .venv/Scripts/activate    # Windows Git Bash；macOS/Linux 用 source .venv/bin/activate
pip install -e ".[dev]"

# 准备环境变量（可选，均有默认值）
cp .env.example .env

# 启动开发服务器（自动建表，默认端口 <%= port %>）
uvicorn <%= pkg %>.main:app --reload --port <%= port %>
```

启动后访问：

- 健康检查：http://localhost:<%= port %>/health
- 交互式文档：http://localhost:<%= port %>/docs

也可以直接运行模块启动：

```bash
python -m <%= pkg %>.main
```

## 常用命令

```bash
# 运行测试
pytest

# lint 检查 / 自动修复
ruff check .
ruff check --fix .

# 格式化
ruff format .
```

## 配置说明

配置集中在 `src/<%= pkg %>/core/config.py`，通过环境变量或 `.env` 文件覆盖：

| 环境变量 | 说明 | 默认值 |
| --- | --- | --- |
| APP_NAME | 应用名称 | <%= projectName %> |
| DEBUG | 调试模式 | false |
| DATABASE_URL | 数据库连接串 | sqlite+aiosqlite:///./app.db |
| PORT | 服务端口 | <%= port %> |
