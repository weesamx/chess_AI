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

    # check if any piece in board is hanging
    hanging_piece_list = [chess.PAWN, chess.KNIGHT,
                          chess.BISHOP, chess.ROOK, chess.QUEEN]
    user_hanging_list = []
    # enemy_hanging_list = []
    for piece_type in hanging_piece_list:
        user_pieces_square_set = after_base_baord.pieces(
            piece_type, bool_color)
        for square in user_pieces_square_set:
            piece = after_base_baord.piece_at(square)
            if piece != None:
                piece_name = chess.piece_name(piece.piece_type).capitalize()
                enemy_attackers = after_base_baord.attackers(
                    not bool_color, square)
                user_attackers = after_base_baord.attackers(bool_color, square)
                # print(chess.square_name(square))
                if list(enemy_attackers) and not list(user_attackers):
                    user_hanging_list.append(square)
                    print(color.capitalize(), piece_name, "at",
                          chess.square_name(square), "is hanging")

    # Pins
    pins_list = [chess.BISHOP, chess.ROOK, chess.QUEEN]
    if moved_piece_type in pins_list:
        for square in end_attack_square:
            piece = after_base_baord.piece_at(
                chess.parse_square(chess.square_name(square)))
            if piece != None and piece.color != bool_color:
                square_set_ray = chess.SquareSet.ray(
                    square, chess.parse_square(end_square))
                piece_type = piece.piece_type
                piece_name = chess.piece_name(piece_type).capitalize()
                for ray_square in square_set_ray:
                    ray_piece = after_base_baord.piece_at(
                        chess.parse_square(chess.square_name(ray_square)))
                    piece_count = 0
                    if ray_piece != None and ray_piece.color != bool_color:
                        squares_between_piece_and_user_piece = chess.SquareSet.between(
                            ray_square, chess.parse_square(end_square))
                        ray_piece_type = ray_piece.piece_type
                        ray_piece_name = chess.piece_name(
                            ray_piece_type).capitalize()
                        # print(squares_between_piece_and_user_piece)
                        # print("-----")
                        if list(squares_between_piece_and_user_piece):
                            for between_square in squares_between_piece_and_user_piece:
                                between_piece = after_base_baord.piece_at(
                                    chess.parse_square(chess.square_name(between_square)))
                                if between_piece != None and between_piece.color != bool_color:
                                    between_piece_type = between_piece.piece_type
                                    between_piece_name = chess.piece_name(
                                        between_piece_type).capitalize()
                                    piece_count = piece_count + 1
                            if piece_count == 1:
                                if square not in user_hanging_list:
                                    if ray_piece.piece_type == chess.KING:
                                        # Absolute pin
                                        print(color.capitalize(), moved_piece_name, "at", chess.square_name(
                                            square), "absolute pins", opponent_color.capitalize(), between_piece_name, "at", chess.square_name(between_square))
                                    else:
                                        is_ray_square_attacked = after_base_baord.is_attacked_by(
                                            not bool_color, ray_square)
                                        if not is_ray_square_attacked and between_piece_type != chess.KING:
                                            print(color.capitalize(), moved_piece_name, "at", chess.square_name(square), "pins", opponent_color.capitalize(
                                            ), between_piece_name, "at", chess.square_name(between_square), "with", opponent_color.capitalize(), ray_piece_name, "at", chess.square_name(ray_square))
                                        else:
                                            knight_bishop = [
                                                chess.KNIGHT, chess.BISHOP]
                                            if ray_piece.piece_type in knight_bishop and piece_type in knight_bishop:
                                                print(color.capitalize(), moved_piece_name, "at", chess.square_name(square), "pins", opponent_color.capitalize(
                                                ), between_piece_name, "at", chess.square_name(between_square), "with", opponent_color.capitalize(), ray_piece_name, "at", chess.square_name(ray_square))
                                            elif int(ray_piece.piece_type) >= int(moved_piece_type):
                                                print(color.capitalize(), moved_piece_name, "at", chess.square_name(square), "pins", opponent_color.capitalize(
                                                ), between_piece_name, "at", chess.square_name(between_square), "with", opponent_color.capitalize(), ray_piece_name, "at", chess.square_name(ray_square))

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
