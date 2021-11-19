import chess
import asyncio

async def explainableAI(color,engine ,board, user_moves, generated_moves):
    print("user" ,user_moves)
    print("generated" ,generated_moves)
    # info = await engine.analyse(board, chess.engine.Limit(depth=10))
    # if color == "white":
    #     print(info["score"].white().score()/100)
    # else:
    #     print(info["score"].black().score()/100)
    print(color)
    for el in list(board.legal_moves):
        copy_board = board.copy()
        copy_board.push(el)
        info = await engine.analyse(copy_board, chess.engine.Limit(depth=10))
        if color == "white":
            print(str(el) + ": " +  str(info["score"].white().score()))
        else:
            print(str(el) + ": " +  str(info["score"].black().score()))

    pass