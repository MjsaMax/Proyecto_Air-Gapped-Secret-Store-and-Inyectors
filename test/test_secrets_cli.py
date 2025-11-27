import pytest
import sys
from unittest import mock
from pathlib import Path

# Configuramos el path para importar secrets_cli
sys.path.append(str(Path(__file__).parent.parent / "secrets"))
import secrets_cli

TEST_PASSPHRASE = "ContraSecreto"
TEST_SECRET_ID = "Test_SecretoID"
TEST_SECRET_VALUE = "Contenido_Secreto"

def test_end_to_end_encryption_decryption(setup_storage_dir):
    """Almacena el secreto y verifica que se recupera exactamente el mismo valor."""
    secrets_cli.store_secret(TEST_SECRET_ID, TEST_SECRET_VALUE, TEST_PASSPHRASE)
    retrieved_value = secrets_cli.get_secret(TEST_SECRET_ID, TEST_PASSPHRASE)
    assert retrieved_value == TEST_SECRET_VALUE
    assert (setup_storage_dir / f"{TEST_SECRET_ID}.enc").is_file()

def test_decryption_fails_with_wrong_passphrase(setup_storage_dir, capsys):
    """Verifica que el sistema falle y emita error con passphrase incorrecto."""
    secrets_cli.store_secret(TEST_SECRET_ID, TEST_SECRET_VALUE, TEST_PASSPHRASE)
    with mock.patch('sys.exit') as mock_exit:
        secrets_cli.get_secret(TEST_SECRET_ID, "PASS_INCORRECTO")
        mock_exit.assert_called_once_with(1)
        errorCapturado = capsys.readouterr()
        assert "Password inválido al desencriptar" in errorCapturado.err

def test_secret_is_injected_into_subprocess_env(setup_storage_dir):
    """Verifica que el secreto es pasado al subproceso como variable de entorno."""
    secrets_cli.store_secret(TEST_SECRET_ID, TEST_SECRET_VALUE, TEST_PASSPHRASE)
    with mock.patch('subprocess.run') as mock_run, \
        mock.patch('sys.exit'):
        test_command = ["echo", "test"]
        secrets_cli.run_with_env(TEST_SECRET_ID, TEST_PASSPHRASE, test_command)
        mock_run.assert_called_once()
        env_passed = mock_run.call_args[1]['env']
        expected_env_var = TEST_SECRET_ID.upper()
        assert env_passed[expected_env_var] == TEST_SECRET_VALUE
        assert mock_run.call_args[0][0] == "echo test"

def test_list_secrets_shows_all_ids(setup_storage_dir, capsys):
    """Verifica que la función list muestre todos los IDs almacenados."""
    secrets_cli.store_secret("SECRETO_A", "v1", TEST_PASSPHRASE)
    secrets_cli.store_secret("SECRETO_B", "v2", TEST_PASSPHRASE)
    secrets_cli.list_secrets(None)
    listCapturado = capsys.readouterr()
    assert "Secretos disponibles:" in listCapturado.err
    assert "- SECRETO_A" in listCapturado.err
    assert "- SECRETO_B" in listCapturado.err
