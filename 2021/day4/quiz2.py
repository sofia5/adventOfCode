def initBoards(boardsData):
    boards = []
    for boardData in boardsData:
        boardRows = boardData.split('\n')
        board = []
        for boardRow in boardRows:
            board.append(boardRow.strip().split(' '))
        boards.append({"board": board, "won": False})
    return boards


def markNumber(board: list, drawnNumber: str):
    for rowIndex, boardRow in enumerate(board):
        for colIndex, boardNumber in enumerate(boardRow):
            if boardNumber == drawnNumber:
                board[rowIndex][colIndex] = '-1'
                boardProps = {"board": board, "row": rowIndex, "col": colIndex}
                return boardProps
    return {}


def checkIfBingo(board: list, row: int, col: int):
    bingoRow = True
    bingoCol = True
    boardData = board.get("board")

    for rowIndex, boardRow in enumerate(boardData):
        if not bingoRow and not bingoCol:
            return None
        for colIndex, boardNumber in enumerate(boardRow):
            if rowIndex == row and boardNumber != '-1':
                bingoRow = False
            if colIndex == col and boardNumber != '-1':
                bingoCol = False

    if not bingoRow and not bingoCol:
        return None
    else:
        return board


def markAsWinner(board):
    board["won"] = True
    return board


def sumOfUnmarked(bingoBoard: list):
    summedNumbers = 0
    for row in bingoBoard:
        for number in row:
            if number != '-1':
                summedNumbers += int(number)
    return summedNumbers


def main():
    with open('input.txt', 'r') as f:
        input = f.read().replace('  ', ' ')

    drawnNumbers = input.split('\n\n')[0].split(',')
    boards = initBoards(input.split('\n\n')[1:])
    bingoBoard = None
    latestWinner = None

    for drawnNumber in drawnNumbers:
        for board in boards:
            if not board.get("won"):
                boardProps = markNumber(board.get("board"), drawnNumber)
                if boardProps != {}:
                    board["board"] = boardProps.get("board")
                    bingoBoard = checkIfBingo(
                        board, boardProps.get('row'), boardProps.get('col'))
                    if bingoBoard != None:
                        board = markAsWinner(board)
                        latestWinner = [board, int(drawnNumber)]

    print('Last bingo: ', latestWinner)
    summedNumbers = sumOfUnmarked(latestWinner[0].get("board"))
    print(summedNumbers * latestWinner[1])


if __name__ == "__main__":
    main()
