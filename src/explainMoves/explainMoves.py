import chess
import asyncio

async def explainableAI(color,engine ,board, user_moves, generated_moves):
    print("user" ,user_moves)
    print("generated" ,generated_moves)
    info = await engine.analyse(board, chess.engine.Limit(depth=20))
    if color == "white":
        print(info["score"].white())
    else:
        print(info["score"].black())
    
    pass