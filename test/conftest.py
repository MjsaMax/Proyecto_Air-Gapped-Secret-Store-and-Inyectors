import shutil
import tempfile
import pytest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "secrets"))
import secrets_cli

@pytest.fixture
def setup_storage_dir(monkeypatch):
    temp_dir = Path(tempfile.mkdtemp())
    # Redirigir storage_dir al directorio temporal
    monkeypatch.setattr(secrets_cli, "STORAGE_DIR", temp_dir)
    yield temp_dir
    shutil.rmtree(temp_dir)
