from httpx import AsyncClient


async def test_create_and_get_item(client: AsyncClient) -> None:
    response = await client.post("/api/v1/items", json={"name": "键盘", "description": "机械键盘"})
    assert response.status_code == 201
    created = response.json()
    assert created["name"] == "键盘"
    assert created["id"] > 0

    response = await client.get(f"/api/v1/items/{created['id']}")
    assert response.status_code == 200
    assert response.json()["description"] == "机械键盘"


async def test_list_items(client: AsyncClient) -> None:
    await client.post("/api/v1/items", json={"name": "鼠标"})
    await client.post("/api/v1/items", json={"name": "显示器"})

    response = await client.get("/api/v1/items")
    assert response.status_code == 200
    assert [item["name"] for item in response.json()] == ["鼠标", "显示器"]


async def test_get_item_not_found(client: AsyncClient) -> None:
    response = await client.get("/api/v1/items/999")
    assert response.status_code == 404


async def test_create_item_validation_error(client: AsyncClient) -> None:
    response = await client.post("/api/v1/items", json={"name": ""})
    assert response.status_code == 422
