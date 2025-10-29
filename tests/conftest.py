
import sys
import os
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app

# Garante que o Python encontre a pasta 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

