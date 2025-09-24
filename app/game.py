from random import choice
from typing import Tuple

# Movimentos válidos
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


class GameManager:
    def __init__(self):
        self.history = []

    def play(self, player_move: str):
        computer = get_computer_move()
        result = determine_winner(player_move, computer)
        self.history.append({
            "jogador": player_move,
            "computador": computer,
            "resultado": result
        })
        return self.history[-1]

    def get_stats(self):
        wins = {"jogador": 0, "computador": 0, "empate": 0}
        for match in self.history:
            wins[match["resultado"]] += 1
        return wins
