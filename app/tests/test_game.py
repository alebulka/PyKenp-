import pytest
from app.game import validate_move, get_computer_move, determine_winner, GameManager

# Teste 1: validar movimentos válidos
def test_validate_move_valid():
    assert validate_move("pedra")
    assert validate_move("papel")
    assert validate_move("tesoura")

# Teste 2: validar movimentos inválidos
def test_validate_move_invalid():
    assert not validate_move("lagarto")
    assert not validate_move("spock")

# Teste 3: verificar vencedor
def test_determine_winner():
    assert determine_winner("pedra", "tesoura") == "jogador"
    assert determine_winner("tesoura", "pedra") == "computador"
    assert determine_winner("papel", "papel") == "empate"

# Teste 4: get_computer_move retorna um movimento válido
def test_get_computer_move():
    move = get_computer_move()
    assert move in ["pedra", "papel", "tesoura"]

# Teste 5: GameManager armazena histórico corretamente
def test_game_manager_history():
    gm = GameManager()
    gm.play("pedra")
    assert len(gm.history) == 1
    assert gm.history[0]["jogador"] == "pedra"
