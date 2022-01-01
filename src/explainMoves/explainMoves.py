from asyncio.windows_events import NULL
import chess
import asyncio


def analyseScores(move_dictionary):
    total = 0
    for key, value in move_dictionary.items():
        if value != 'None':
            total = total + int(value)
    mean = total / len(move_dictionary)
    print("Mean Score: ", mean)
    return mean


def TextGeneration(board, uci_user_moves, color):
    start_square = uci_user_moves[:2]
    end_square = uci_user_moves[-2:]
    # print(start_square)
    # print(end_square)
    copy_board = board.copy()
    bool_color = copy_board.turn

    before_base_baord = chess.BaseBoard(copy_board.board_fen())
    copy_board.push_uci(uci_user_moves)
    after_base_baord = chess.BaseBoard(copy_board.board_fen())
    moved_piece_type = after_base_baord.piece_type_at(
        chess.parse_square(end_square))
    moved_piece_name = chess.piece_name(moved_piece_type).capitalize()
    if color == "white":
        opponent_color = "black"
    else:
        opponent_color = "white"

    # Control Centre Text
    centre_squares = ["e4", "e5", "d4", "d5"]
    if end_square in centre_squares:
        print(color.capitalize(), moved_piece_name,
              "controls centre tile", end_square)

    # Attacks a square
    end_attack_square = after_base_baord.attacks(
        chess.parse_square(end_square))
    for end_squares in end_attack_square:
        end_piece = after_base_baord.piece_at(
            chess.parse_square(chess.square_name(end_squares)))
        if end_piece != None:
            end_piece_type = end_piece.piece_type
            end_piece_name = chess.piece_name(end_piece_type).capitalize()
            if end_piece.color != bool_color:
                # print(bool_color)
                # print(piece.color)
                # print(chess.square_name(squares))
                print(color.capitalize(), moved_piece_name, "at", end_square, "threatens",
                      opponent_color.capitalize(), end_piece_name, "at", chess.square_name(end_squares))
            # Defends a square
            if end_piece.color == bool_color and end_piece_type != chess.KING:
                # Defend iff piece is attacked
                # Strengthen iff piece is not attacked
                print(color.capitalize(), moved_piece_name, "at", end_square, "defends",
                      color.capitalize(), end_piece_name, " at",  chess.square_name(end_squares))

    # start_attack_square = before_base_baord.attacks(chess.parse_square(start_square))
    # #Check for user's hanging pieces
    # for start_squares in start_attack_square:
    #     start_piece = before_base_baord.piece_at(chess.parse_square(chess.square_name(start_squares)))
    #     if start_piece != None:
    #         start_piece_type = start_piece.piece_type
    #         start_piece_name = chess.piece_name(start_piece_type).capitalize()
    #         #Defends a square
    #         if start_piece.color == bool_color and start_piece_type != chess.KING:
    #             enemy_attackers = before_base_baord.attackers(not bool_color, chess.parse_square(chess.square_name(start_squares)))
    #             # print(list(enemy_attackers))
    #             # print(start_piece_name)
    #             if list(enemy_attackers):
    #                 #originally defended piece at start square might be hanging after moving
    #                 #has an attacker
    #                 user_attackers = after_base_baord.attackers(bool_color, chess.parse_square(chess.square_name(start_squares)))
    #                 if not list(user_attackers):
    #                     #no one defending piece that was originaly defended
    #                     print(color.capitalize() , start_piece_name , "at" , chess.square_name(start_squares), "is hanging")
    #                 # for i in user_attackers:
    #                 #     print(chess.square_name(i))
    #                 # print(list(user_attackers))

    # check if any piece in board is hanging
    piece_type_list = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.QUEEN]
    for piece_type in piece_type_list:
        pieces_square_set = after_base_baord.pieces(piece_type, bool_color)
        for square in list(pieces_square_set):
            piece = after_base_baord.piece_at(square)
            if piece != None:
                piece_name = chess.piece_name(piece.piece_type).capitalize()
                enemy_attackers = after_base_baord.attackers(
                    not bool_color, square)
                user_attackers = after_base_baord.attackers(bool_color, square)
                # print(chess.square_name(square))
                if list(enemy_attackers) and not list(user_attackers):
                    print(color.capitalize(), piece_name, "at",
                          chess.square_name(square), "is hanging")

    # Absolute pins (pinning a piece against opponents king)

    # Discovered attacks

    # Forks

    # Pawn stacking / doubled pawn (bad)


async def explainableAI(color, engine, board, user_moves, generated_moves, simulation):
    print("user", user_moves)
    print("generated", generated_moves)
    board.push(generated_moves)
    uci_generated_moves = board.pop()
    if(simulation):
        board.push(generated_moves)
    else:
        board.push_san(user_moves)
    uci_user_moves = board.pop()
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
            moves_scores_dictionary[str(el)] = str(
                info["score"].white().score())
        else:
            # print(str(el) + ": " +  str(info["score"].black().score()))
            moves_scores_dictionary[str(el)] = str(
                info["score"].black().score())

    print(moves_scores_dictionary)
    if(str(uci_user_moves) in moves_scores_dictionary):
        user_move_score = moves_scores_dictionary[str(uci_user_moves)]
        best_score = moves_scores_dictionary[str(uci_generated_moves)]
        print("Best move score", best_score)
        print("User move score", user_move_score,
              "User move: ", str(uci_user_moves))
        mean_score = analyseScores(moves_scores_dictionary)

        if best_score.isnumeric() and user_move_score.isnumeric():

            # evaluate if usermove is good or bad
            if int(best_score) - int(user_move_score) > 100:
                # bad move
                pass
            else:
                # good move
                pass
            TextGeneration(board, str(uci_user_moves), color)
