from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from app.game import MOVES, validate_move, get_computer_move, determine_winner

app = FastAPI(title="Jokenpô API", version="0.1.0")

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

    computer = get_computer_move()
    result = determine_winner(move, computer)

    return PlayResult(jogador=move, computador=computer, resultado=result)