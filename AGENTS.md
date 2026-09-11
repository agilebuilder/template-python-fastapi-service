# AGENTS.md — AI 编码代理导航指南

<% var pkg = packageDir.charAt(0) === '<' ? snakeCase(projectName) : packageDir -%>
本项目是基于 FastAPI + SQLAlchemy 2.x（asyncio）+ Pydantic v2 的异步 API 服务，src 布局。

## 项目结构

- `src/<%= pkg %>/main.py`：应用入口。`create_app()` 工厂函数创建 FastAPI 实例，lifespan 中自动建表；`main()` 用 uvicorn 启动。
- `src/<%= pkg %>/api/router.py`：路由聚合。新路由模块在 `api/routes/` 下创建后，在这里 `include_router`。
- `src/<%= pkg %>/api/routes/`：HTTP 路由层。只做参数解析、调用 service、返回响应，不写业务逻辑。
- `src/<%= pkg %>/core/config.py`：`Settings`（pydantic-settings），所有配置从这里读取，不要散落读环境变量。
- `src/<%= pkg %>/db/session.py`：异步引擎与 `async_session_factory`；`get_session` 是 FastAPI 依赖，路由通过 `Depends(get_session)` 获取会话。
- `src/<%= pkg %>/models/`：SQLAlchemy ORM 模型，统一继承 `models/base.py` 的 `Base`。
- `src/<%= pkg %>/schemas/`：Pydantic v2 请求/响应模型，与 ORM 模型分离。
- `src/<%= pkg %>/services/`：业务逻辑与数据库操作，路由与会话在这里交汇。
- `tests/`：pytest 测试。`conftest.py` 用内存 SQLite 覆盖 `get_session` 依赖，`client` fixture 提供 httpx AsyncClient。

## 约定

- 包内部一律使用相对导入（如 `from ..core.config import settings`）；包外（tests）用绝对导入 `<%= pkg %>.xxx`。
- 全链路异步：路由、service、DB 操作都是 `async def`，不要混入同步 SQLAlchemy 调用。
- 所有代码带类型注解；新增 ORM 模型需在 `models/__init__.py` 导出，保证建表时元数据完整。
- 请求体用 `schemas/` 中的 Pydantic 模型校验；响应用 `response_model` 声明。
- 提交代码前跑 `ruff check --fix . && ruff format .` 和 `pytest`，保持绿灯。

## 常用命令

```bash
pip install -e ".[dev]"          # 安装依赖（含 dev）
uvicorn <%= pkg %>.main:app --reload --port <%= port %>   # 开发启动
python -m <%= pkg %>.main        # 直接运行模块启动
pytest                           # 运行测试
ruff check .                     # lint
ruff format .                    # 格式化
```
