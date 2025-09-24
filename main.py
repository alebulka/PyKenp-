from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from app.game import MOVES, validate_move, get_computer_move, determine_winner, GameManager

app = FastAPI(title="Jokenpô API", version="0.1.0")

# instância global para gerenciar estatísticas
game_manager = GameManager()


class PlayResult(BaseModel):
    jogador: str
    computador: str
    resultado: str


@app.get("/", tags=["status"])
async def root():
    return {"mensagem": "Bem-vindo ao Jokenpô API!", "version": app.version}


@app.get("/play", response_model=PlayResult, tags=["game"])
async def play(move: str = Query(..., description="Movimento do jogador: pedra, papel ou tesoura")):
    move = move.lower().strip()
    if not validate_move(move):
        raise HTTPException(status_code=400, detail="Movimento inválido. Use 'pedra', 'papel' ou 'tesoura'.")

    # usa o GameManager para registrar a partida
    partida = game_manager.play(move)

    return PlayResult(**partida)


@app.get("/stats", tags=["game"])
async def stats():
    return game_manager.get_stats()