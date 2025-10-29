
import pytest

@pytest.mark.asyncio
async def test_listar_consultas(client):
    response = await client.get("/consultas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
