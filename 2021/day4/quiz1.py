def initBoards(boardsData):
    boards = []
    for boardData in boardsData:
        boardRows = boardData.split('\n')
        board = []
        for boardRow in boardRows:
            board.append(boardRow.strip().split(' '))
        boards.append(board)
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

    for rowIndex, boardRow in enumerate(board):
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
    bingo = False
    bingoBoard = None
    latestNumber = 0

    for drawnNumber in drawnNumbers:
        i = 0
        while not bingo and i < len(boards):
            for board in boards:
                boardProps = markNumber(board, drawnNumber)
                board = boardProps.get("board")
                if boardProps != {}:
                    bingoBoard = checkIfBingo(
                        board, boardProps.get('row'), boardProps.get('col'))
                    if bingoBoard != None:
                        print('bingo: ', bingoBoard)
                        bingo = True
                        latestNumber = int(drawnNumber)
                        summedNumbers = sumOfUnmarked(bingoBoard)
                        print(summedNumbers, latestNumber,
                              summedNumbers * latestNumber)
            i += 1


if __name__ == "__main__":
    main()
