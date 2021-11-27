from asyncio.windows_events import NULL
import chess
import asyncio

def analyseScores(move_dictionary):
    total = 0
    for key,value in move_dictionary.items():
        if value != 'None':
            total = total + int(value) 
    max_key = max(move_dictionary, key=move_dictionary.get)
    best_score = move_dictionary[max_key]
    print("Best Score: ", best_score)
    mean = total / len(move_dictionary)
    print("Mean Score: " , mean)
    return mean, best_score



async def explainableAI(color,engine ,board, user_moves, generated_moves,simulation):
    print("user" ,user_moves)
    print("generated" ,generated_moves)
    # info = await engine.analyse(board, chess.engine.Limit(depth=10))
    # if color == "white":
    #     print(info["score"].white().score()/100)
    # else:
    #     print(info["score"].black().score()/100)
    # print(color)
    moves_scores_dictionary = {}
    for el in list(board.legal_moves):
        copy_board = board.copy()
        copy_board.push(el)
        info = await engine.analyse(copy_board, chess.engine.Limit(depth=10))
        if color == "white":
            # print(str(el) + ": " +  str(info["score"].white().score()))
            moves_scores_dictionary[str(el)] = str(info["score"].white().score())
        else:
            # print(str(el) + ": " +  str(info["score"].black().score()))
            moves_scores_dictionary[str(el)] = str(info["score"].black().score())
    if(simulation):
        board.push(generated_moves)
    else:
        board.push_san(user_moves)
    uci_user_moves = board.pop()
    print(moves_scores_dictionary)
    if(str(uci_user_moves) in moves_scores_dictionary):
        user_move_score  = moves_scores_dictionary[str(uci_user_moves)]
        mean_score , best_score = analyseScores(moves_scores_dictionary)
