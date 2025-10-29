
import pytest

@pytest.mark.asyncio
async def test_listar_medicos(client):
    response = await client.get("/medicos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
