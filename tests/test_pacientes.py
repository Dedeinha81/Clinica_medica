
import pytest

@pytest.mark.asyncio
async def test_listar_pacientes(client):
    response = await client.get("/pacientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
