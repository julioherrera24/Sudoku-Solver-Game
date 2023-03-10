board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bd):
    find = findEmpty(bd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bd, i, (row, col)):
            bd[row][col] = i

            if solve(bd):
                return True

            bd[row][col] = 0

    return False


def valid(bd, num, pos):
    # Check row
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bd[i][j] == num and (i,j) != pos:
                return False

    return True

def printBoard(bd):

  for i in range(len(bd)):
    
    #Seperates board after every 3rd row into different sections
    if i % 3 == 0 and i != 0:
      print("---------------------")

    #for every pos in the row
    for j in range(len(bd[0])):
      #check if its the 3rd element in the row
      if j % 3 == 0 and j != 0:
        print("| ", end = "")
      
      #once were at the last pos of row, print newline to move to next row
      if j == 8:
        print(bd[i][j])
      #print current pos & stay on same row
      else:
        print(str(bd[i][j]) + " ", end = "")

def findEmpty(bd):
  for i in range(len(bd)):
    #check every row in board
    for j in range(len(bd[0])):
      #check if pos is empty
      if bd[i][j] == 0:
        #return a tuple of pos that is empty(row, col)
        return (i, j)


printBoard(board)