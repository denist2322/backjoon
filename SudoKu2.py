sudoku = []

def search(row, col, value):
  return True

def DFS(row, col):
  if col == 9 :
    DFS(row+1,0)
    return
  
  if row == 9 :
    print(sudoku)
    exit

  if(sudoku[row][col] == 0):
    # 검사는 행, 열, 사각형 각각 9번씩 필요함
    for i in range(1,10):
      if search(row, col, i):
        sudoku[row][col] = i
        DFS(row, col+1)
        
    # 세가지 모두 부합할 경우 도 있음
    sudoku[row][col] = 0
    return
      
  DFS(row, col+1)   
