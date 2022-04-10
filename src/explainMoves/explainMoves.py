import chess

def analyseScores(move_dictionary):
    total = 0
    for key, value in move_dictionary.items():
        if value != 'None':
            total = total + int(value)
    mean = total / len(move_dictionary)
    print("Mean Score: ", mean)
    return mean


def BadTextGeneration(board, uci_user_moves, color):
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



def GoodTextGeneration(board, uci_user_moves, color):
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



def TextGeneration(board, uci_user_moves, color):
    listofWords = []
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
        listofWords.append(color.capitalize() + " " + moved_piece_name + " controls centre tile " + end_square)
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
                listofWords.append(color.capitalize() + " " + moved_piece_name + " at " + end_square + " threatens " +
                      opponent_color.capitalize()+ " " + end_piece_name + " at " + chess.square_name(end_squares))
                print(color.capitalize(), moved_piece_name, "at", end_square, "threatens",
                      opponent_color.capitalize(), end_piece_name, "at", chess.square_name(end_squares))
            # Defends a square
            if end_piece.color == bool_color and end_piece_type != chess.KING:
                # Defend iff piece is attacked
                # Strengthen iff piece is not attacked
                listofWords.append(color.capitalize() + " " + moved_piece_name+ " at "+ end_square+ " defends "+
                      color.capitalize() + " " + end_piece_name + " at "+  chess.square_name(end_squares))
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
                    listofWords.append(color.capitalize() + " " + piece_name + " at " +
                          chess.square_name(square)+ " is hanging")
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
                                        listofWords.append(color.capitalize() + " " + moved_piece_name +  " at " + chess.square_name(
                                            square) + " absolute pins " + opponent_color.capitalize()+ " " + between_piece_name + " at "+ chess.square_name(between_square))
                                        print(color.capitalize(), moved_piece_name, "at", chess.square_name(
                                            square), "absolute pins", opponent_color.capitalize(), between_piece_name, "at", chess.square_name(between_square))
                                    else:
                                        is_ray_square_attacked = after_base_baord.is_attacked_by(
                                            not bool_color, ray_square)
                                        if not is_ray_square_attacked and between_piece_type != chess.KING:
                                            listofWords.append(color.capitalize() + " " + moved_piece_name + " at " + chess.square_name(square) + " pins " + opponent_color.capitalize(
                                            ) + " " + between_piece_name + " at " + chess.square_name(between_square) + " with " + opponent_color.capitalize()+ " " + ray_piece_name + " at " + chess.square_name(ray_square))
                                            print(color.capitalize(), moved_piece_name, "at", chess.square_name(square), "pins", opponent_color.capitalize(
                                            ), between_piece_name, "at", chess.square_name(between_square), "with", opponent_color.capitalize(), ray_piece_name, "at", chess.square_name(ray_square))
                                        else:
                                            knight_bishop = [
                                                chess.KNIGHT, chess.BISHOP]
                                            if ray_piece.piece_type in knight_bishop and piece_type in knight_bishop:
                                                listofWords.append(color.capitalize() + " " + moved_piece_name + " at " + chess.square_name(square) + " pins " + opponent_color.capitalize(
                                                ) + " " + between_piece_name + " at " + chess.square_name(between_square) + " with " + opponent_color.capitalize()+ " " + ray_piece_name + " at " + chess.square_name(ray_square))
                                                print(color.capitalize(), moved_piece_name, "at", chess.square_name(square), "pins", opponent_color.capitalize(
                                                ), between_piece_name, "at", chess.square_name(between_square), "with", opponent_color.capitalize(), ray_piece_name, "at", chess.square_name(ray_square))
                                            elif int(ray_piece.piece_type) >= int(moved_piece_type):
                                                listofWords.append(color.capitalize() + " " + moved_piece_name + " at " + chess.square_name(square) + " pins "+ opponent_color.capitalize(
                                                ) + " " + between_piece_name + " at " + chess.square_name(between_square) + " with " + opponent_color.capitalize() + " " + ray_piece_name + " at " + chess.square_name(ray_square))
                                                print(color.capitalize(), moved_piece_name, "at", chess.square_name(square), "pins", opponent_color.capitalize(
                                                ), between_piece_name, "at", chess.square_name(between_square), "with", opponent_color.capitalize(), ray_piece_name, "at", chess.square_name(ray_square))

    # Discovered attacks

    # Forks

    # Pawn stacking / doubled pawn (bad)
    return listofWords
async def TradingText(board, uci_user_moves, color,engine):
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
    piece = before_base_baord.piece_type_at(
        chess.parse_square(end_square))
    
    takenByUser = []
    takenByEnemy = []
    listofMove = []
    listofBoard = []
    listofWords = []
    if(piece != None):
        #piece is taken by move
        # listofMove.append(uci_user_moves)
        takenByUser.append(piece)
        listofBoard.append(copy_board.copy())
        while True:
            print("Precalculate")
            result = await engine.play(copy_board, chess.engine.Limit(nodes = 10000))
            print("Calculating if trade is possible")
            copy_board.push(result.move)
            uci_user_move = copy_board.pop()
            base_board = chess.BaseBoard(copy_board.board_fen())
            end_square_move = str(uci_user_move)[-2:]
            if(base_board.piece_at(chess.parse_square(end_square_move)) != None):
                print("takes")
                listofMove.append(str(uci_user_move))
                listofBoard.append(copy_board)
                print(base_board.piece_at(chess.parse_square(end_square_move)))
                if(copy_board.turn):
                    takenByUser.append(base_board.piece_type_at(chess.parse_square(end_square_move)))
                else:
                    takenByEnemy.append(base_board.piece_type_at(chess.parse_square(end_square_move)))      
                copy_board.push(result.move)

            else:
                listofMove.append(str(uci_user_move))    
                listofBoard.append(copy_board)
                copy_board.push(result.move)
                break
    takenByUserPieceName = []
    takenByEnemyPieceName = []
    for i in range(len(takenByUser)):
        takenByUserPieceName.append(chess.piece_name(takenByUser[i]).capitalize())
        if takenByUser[i] == 2:
            takenByUser[i] == 3
    for i in range(len(takenByEnemy)):
        takenByEnemyPieceName.append(chess.piece_name(takenByEnemy[i]).capitalize())
        if takenByEnemy[i] == 2:
            takenByEnemy[i] == 3
    if(sum(takenByEnemy) == 0 and sum(takenByUser) == 0):
        return listofWords
    else:
        if(sum(takenByUser) > sum(takenByEnemy)):
            #good trade
            listofWords.append("A good trade")
        elif(sum(takenByUser) < sum(takenByEnemy)):
            #bad trade
            listofWords.append("A bad trade")
        else:
            #equal trade
            listofWords.append("An equal trade")
            pass
        listofWords.append("You capture pieces of ")
        listofWords.append(' '.join(takenByUserPieceName))
        listofWords.append("Enemy captures pieces of ")
        listofWords.append(' '.join(takenByEnemyPieceName))
        print(takenByUser)
        print(takenByEnemy)
        print(listofMove)
        listofWords.append("By following the best moves possible for both sides")
        listofWords.append(' '.join(listofMove))
    return listofWords
    
async def explainableAI(color, engine, board, user_moves, generated_moves, simulation):
    print("user", user_moves)
    print("generated", generated_moves)
    wordList = []
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
        info = await engine.analyse(copy_board, chess.engine.Limit(nodes = 10000))
        # if color == "white":
            # print(str(el) + ": " +  str(info["score"].white().score()))
        moves_scores_dictionary[str(el)] = str(
            info["score"].white().score())
        # else:
        #     # print(str(el) + ": " +  str(info["score"].black().score()))
        #     moves_scores_dictionary[str(el)] = str(
        #         info["score"].black().score())

    print(moves_scores_dictionary)
    if(str(uci_user_moves) in moves_scores_dictionary):
        user_move_score = moves_scores_dictionary[str(uci_user_moves)]
        best_score = moves_scores_dictionary[str(uci_generated_moves)]
        print("Best move score", best_score)
        print("User move score", user_move_score,
              "User move: ", str(uci_user_moves))
        # mean_score = analyseScores(moves_scores_dictionary)
        if best_score.lstrip('-').isnumeric() and user_move_score.lstrip('-').isnumeric():
            # evaluate if usermove is good or bad
            wordList.append("Board CentiPawn Score")
            wordList.append(user_move_score)
            if int(best_score) - int(user_move_score) > 100:
                # bad move
                wordList.append("Move is a bad move")
                wordList = wordList + TextGeneration(board, str(uci_user_moves), color)
                tradingList = await TradingText(board, str(uci_user_moves),color,engine)
                if(len(tradingList) != 0):
                    wordList.append("----------")
                    wordList = wordList + tradingList
    
                print("Best Move Explanation")
                wordList.append("Best Move (" + str(uci_generated_moves) +  ") Explanation")
                wordList = wordList + TextGeneration(board, str(uci_generated_moves),color)
            else:
                # good move
                wordList.append("Move is a good move")
                wordList = wordList + TextGeneration(board, str(uci_user_moves), color)
                tradingList = await TradingText(board, str(uci_user_moves),color,engine)
                if(len(tradingList) != 0):
                    wordList.append("----------")
                    wordList = wordList + tradingList
            # print("before")
            # wordList = wordList + TextGeneration(board, str(uci_user_moves), color)
            # print("after")
            # await TradingText(board, str(uci_user_moves),color,engine)

            # print("Best Move Explanation")
            # wordList.append("Best Move (" + str(uci_generated_moves) +  ") Explanation")
            # wordList = wordList + TextGeneration(board, str(uci_generated_moves),color)
    return wordList