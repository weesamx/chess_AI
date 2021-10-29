import asyncio
import chess
import chess.engine
import chess.svg
from retreiveData.retrieveData import *
from explainMoves.explainMoves import *

# async def main() -> None:
#     transport, engine = await chess.engine.popen_uci(r"C:\Users\Sam\source\repos\chess_AI\src\stockfish_14_win_x64_avx2\stockfish_14_x64_avx2.exe")

#     board = chess.Board()
#     while not board.is_game_over():
#         result = await engine.play(board, chess.engine.Limit(time=0.1))
#         board.push(result.move)
#     await engine.quit()

username = "weesam7"
matchMoves = get_most_recent_games(username)
color = getColor(username)
async def main() -> None:
    transport, engine = await chess.engine.popen_uci(r"C:\Users\Sam\source\repos\chess_AI\src\stockfish_14_win_x64_avx2\stockfish_14_x64_avx2.exe")
    board = chess.Board()
    while input() != "end" and matchMoves:
        nextMove = matchMoves.pop(0).strip()
        if (color == "white" and board.turn) or (color =="black" and not board.turn):
            result = await engine.play(board, chess.engine.Limit(time=0.1))
            board.push_san(nextMove)
            await explainableAI(color, engine, board, nextMove, result)
        else:
            board.push_san(nextMove)
        print(board)

    await engine.quit()

# asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())


