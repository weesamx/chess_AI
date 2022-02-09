import asyncio
import chess
import chess.engine
import chess.svg
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from retreiveData.retrieveData import *
from explainMoves.explainMoves import *

# async def main() -> None:
#     transport, engine = await chess.engine.popen_uci(r"C:\Users\Sam\source\repos\chess_AI\src\stockfish_14_win_x64_avx2\stockfish_14_x64_avx2.exe")

#     board = chess.Board()
#     while not board.is_game_over():
#         result = await engine.play(board, chess.engine.Limit(time=0.1))
#         board.push(result.move)
#     await engine.quit()
pygame.init()
width = 1280
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Engine")


sample_game_movesets = ['e4 ', 'e5 ', 'Nf3 ', 'd6 ', 'd4 ', 'Bg4 ', 'h3 ', 'Be6 ',
                        'Nc3 ', 'f6 ', 'Be3 ', 'g5 ', 'g4 ', 'h5 ', 'gxh5 ', 'Rxh5 ', 'Nxe5 ', 'fxe5 ',
                        'Qxh5+ ', 'Bf7 ', 'Bxg5 ', 'Be7 ', 'Bxe7 ', 'Qxe7 ', 'Qh8 ', 'Nc6 ', 'Nd5 ',
                        'Bxd5 ', 'exd5 ', 'Nxd4 ', 'Qxg8+ ', 'Qf8 ', 'Qxf8+ ', 'Kxf8 ', 'O-O-O ', 'Re8 ',
                        'c3 ', 'Nf3 ', 'Be2 ', 'e4 ', 'Bxf3 ', 'exf3 ', 'Rde1 ', 'Rxe1+ ', 'Rxe1 ',
                        'Kf7 ', 'b4 ', 'Kf6 ', 'Re3 ']

chessboard = pygame.image.load(r'./src/chessPieces/ChessBoard.png').convert_alpha()
King = pygame.image.load(r'./src/chessPieces/Chess_klt60.png').convert_alpha()
king = pygame.image.load(r'./src/chessPieces/Chess_kdt60.png').convert_alpha()
Knight = pygame.image.load(r'./src/chessPieces/Chess_nlt60.png').convert_alpha()
knight = pygame.image.load(r'./src/chessPieces/Chess_ndt60.png').convert_alpha()
Rook = pygame.image.load(r'./src/chessPieces/Chess_rlt60.png').convert_alpha()
rook = pygame.image.load(r'./src/chessPieces/Chess_rdt60.png').convert_alpha()
Queen = pygame.image.load(r'./src/chessPieces/Chess_qlt60.png').convert_alpha()
queen = pygame.image.load(r'./src/chessPieces/Chess_qdt60.png').convert_alpha()
Bishop = pygame.image.load(r'./src/chessPieces/Chess_blt60.png').convert_alpha()
bishop = pygame.image.load(r'./src/chessPieces/Chess_bdt60.png').convert_alpha()
Pawn = pygame.image.load(r'./src/chessPieces/Chess_plt60.png').convert_alpha()
pawn = pygame.image.load(r'./src/chessPieces/Chess_pdt60.png').convert_alpha()


def draw(piece, col, rank, board):
    if piece == 'K':
        # if board.turn == chess.WHITE :
        #     if board.is_check() :
        #         pygame.draw.circle(screen, RED, (rank + 30, col + 30), 30)
        screen.blit(King, (rank, col))
    elif piece == 'k':
        # if board.turn == chess.BLACK :
        #     if board.is_check() :
        #         pygame.draw.circle(screen, RED, (rank + 30, col + 30), 30)
        screen.blit(king, (rank, col))
    elif piece == 'Q':
        screen.blit(Queen, (rank, col))
    elif piece == 'q':
        screen.blit(queen, (rank, col))
    elif piece == 'R':
        screen.blit(Rook, (rank, col))
    elif piece == 'r':
        screen.blit(rook, (rank, col))
    elif piece == 'N':
        screen.blit(Knight, (rank, col))
    elif piece == 'n':
        screen.blit(knight, (rank, col))
    elif piece == 'B':
        screen.blit(Bishop, (rank, col))
    elif piece == 'b':
        screen.blit(bishop, (rank, col))
    elif piece == 'P':
        screen.blit(Pawn, (rank, col))
    elif piece == 'p':
        screen.blit(pawn, (rank, col))


def show(FEN, board):
    screen.blit(chessboard, (0, 0))
    col = 0
    rank = 0
    for fen in FEN:
        if fen == '/':
            col = col + 1
            rank = 0
        elif fen in ('1', '2', '3', '4', '5', '6', '7', '8'):
            rank = rank + int(fen)
        elif fen in ('K', 'k', 'Q', 'q', 'R', 'r', 'N', 'n', 'B', 'b', 'P', 'p'):
            draw(fen, col*60, rank*60, board)
            rank = rank + 1
        if col == 7 and rank == 8:
            break




username = "weesam7"
matchMoves = get_most_recent_games(username)
print(matchMoves)
color = getColor(username)


# async def main() -> None:
#     # screen = pygame.display.set_mode((480, 480))
#     # pygame.display.set_caption("Chess Engine")
#     transport, engine = await chess.engine.popen_uci(r"./src/stockfish_14_win_x64_avx2/stockfish_14_x64_avx2.exe")
#     board = chess.Board()
#     no_moves = 0

#     # show(board.fen(),board)
#     while matchMoves:
#         # ev = pygame.event.get()
#         # for event in ev:
#         #     if event.type == MOUSEBUTTONDOWN:
#         userinput = input()
#         if userinput == "s":
#             copy_board = board.copy()
#             print("Input Depth to simulate")
#             depth = int(input())
#             if depth < 1:
#                 print("Invalid Depth")
#             else:
#                 for i in range(depth):
#                     result = await engine.play(copy_board, chess.engine.Limit(time=0.1))
#                     await explainableAI(color, engine, copy_board, 0, result.move, 1)
#                     copy_board.push(result.move)
#                     print(copy_board)
#                     print(copy_board.fen())
#         else:
#             nextMove = matchMoves.pop(0).strip()
#             no_moves = no_moves + 1
#             if (color == "white" and board.turn) or (color == "black" and not board.turn):
#                 result = await engine.play(board, chess.engine.Limit(time=0.1))
#                 await explainableAI(color, engine, board, nextMove, result.move, 0)
#                 board.push_san(nextMove)
#             else:
#                 board.push_san(nextMove)

#         print(board)
#         print(board.fen())
#         # else:
#         #     #simulate game with two chess engines
#         #     nextMove = matchMoves.pop(0).strip()
#         #     #user's turn to move
#         #     if (color == "white" and board.turn) or (color =="black" and not board.turn):
#         #         result = await engine.play(board, chess.engine.Limit(time=0.1))
#         #         board.push(result.move)
#         #         await explainableAI(color, engine, board, nextMove, result)
#         #     else:
#         #         board.push_san(nextMove)
#         # if color == "white":
#         #     print(board)
#         # else:
#         #     print(board.mirror())
#         # show(board.fen(),board)

#     await engine.quit()

# asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
# asyncio.run(main())
# # pygame.quit()
# # quit()


async def main() -> None:
    # screen = pygame.display.set_mode((width, height))
    # pygame.display.set_caption("Chess Engine")
    transport, engine = await chess.engine.popen_uci(r"./src/stockfish_14_win_x64_avx2/stockfish_14_x64_avx2.exe")
    board = chess.Board()
    no_moves = 0
    wordList = []
    show(board.fen(),board)
    print(board.fen())
    while matchMoves:
        ev = pygame.event.get()
        for event in ev:
            if event.type == MOUSEBUTTONDOWN:
                nextMove = matchMoves.pop(0).strip()
                no_moves = no_moves + 1
                if (color == "white" and board.turn) or (color == "black" and not board.turn):
                    result = await engine.play(board, chess.engine.Limit(time=0.1))
                    wordList = await explainableAI(color, engine, board, nextMove, result.move, 0)
                    board.push_san(nextMove)
                else:
                    board.push_san(nextMove)
            screen.fill((220,220,220))

            myfont = pygame.font.SysFont("monospace", 15)

            # render text
            # label = myfont.render("Some text!", 1, (0,0,0))
            # screen.blit(label, (100, 100))


            show(board.fen(),board)
            for i in range(len(wordList)):
                label = myfont.render(wordList[i], 1, (0,0,0))
                screen.blit(label, (500, i* 50))
            pygame.display.update()

            # print(board)
            # print(board.fen())
        # else:
        #     #simulate game with two chess engines
        #     nextMove = matchMoves.pop(0).strip()
        #     #user's turn to move
        #     if (color == "white" and board.turn) or (color =="black" and not board.turn):
        #         result = await engine.play(board, chess.engine.Limit(time=0.1))
        #         board.push(result.move)
        #         await explainableAI(color, engine, board, nextMove, result)
        #     else:
        #         board.push_san(nextMove)
        # if color == "white":
        #     print(board)
        # else:
        #     print(board.mirror())
        # show(board.fen(),board)

    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())
pygame.quit()
quit()
