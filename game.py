from random import choice
from typing import Tuple

# Movimento válidos
MOVES = ("pedra", "papel", "tesoura")


def validate_move(move: str) -> bool:
    """Retorna True se o movimento for válido."""
    return isinstance(move, str) and move in MOVES


def get_computer_move() -> str:
    """Escolhe aleatoriamente o movimento do computador."""
    return choice(MOVES)


def determine_winner(player: str, computer: str) -> str:
    """Determina o vencedor: 'jogador', 'computador' ou 'empate'."""
    if player == computer:
        return "empate"

    # mapas que indicam o que cada movimento vence
    wins = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra",
    }

    if wins.get(player) == computer:
        return "jogador"
    return "computador"