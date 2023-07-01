'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        return str('friends')
    elif to_member in social_graph[from_member]['following']:
        return str('follower')
    elif from_member in social_graph[to_member]['following']:
        return str('followed by')
    else:
        return str('no relationship')
    
    
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass


def tic_tac_toe(board):
    if len(board) == 3:
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != "":
                return str(row[0])
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
                return str(board[0][col])
        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != "":
            return str(board[1][1])
        else:
            return str("NO WINNER")
    
    elif len(board) == 4:
        for row in board:
            if row[0] == row[1] == row[2] == row[3] and row[0] != "":
                return str(row[0])
        for col in range(4):
            if board[0][col] == board[1][col] == board[2][col] == board[3][col] and board[0][col] != "":
                return str(board[0][col])
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] and board[1][1] != "":
            return str(board[1][1])
        elif board[0][3] == board[1][2] == board[2][1] == board[3][0] and board[2][1] != "":
            return str(board[2][1])
        else:
            return str("NO WINNER")
        
    elif len(board) == 5:
        for row in board:
            if row[0] == row[1] == row[2] == row[3] == row[4] and row[0] != "":
                return str(row[0])
        for col in range(5):
            if board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] and board[0][col] != "":
                return str(board[0][col])
        if (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] or board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]) and board[2][2] != "":
            return str(board[2][2])
        else:
            return str("NO WINNER")
        
    elif len(board) == 6:
        for row in board:
            if row[0] == row[1] == row[2] == row[3] == row[4] == row[5] and row[0] != "":
                return str(row[0])
        for col in range(6):
            if board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] == board[5][col] and board[0][col] != "":
                return str(board[0][col])
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == board[5][5] and board[2][2] != "":
            return str(board[2][2])
        elif board[0][5] == board[1][4] == board[2][3] == board[3][2] == board[4][1] == board[5][0] and board[2][3] != "":
            return str(board[2][3])
        else:
            return str("NO WINNER")
    
    
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def eta(first_stop, second_stop, route_map):
    tupls = [a for a in route_map.keys()]
    element1 = [b for b,c in tupls]
    element2 = [c for b,c in tupls]
    total_time = 0
    for index, i in enumerate(element1):
        if i == first_stop:
            while True:
                if element2[index] != second_stop:
                    time_mins = int(route_map[element1[index],element2[index]]['travel_time_mins'])
                    total_time += time_mins
                    index = (index + 1) % len(element1)
                    continue
                    
                else:
                    fstop_mins = int(route_map[element1[index],element2[index]]['travel_time_mins'])
                    return int(total_time + fstop_mins)
                    break
    
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass