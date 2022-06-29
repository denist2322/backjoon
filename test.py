import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split()))for _ in range(9)]

def search(row, col, value):
  #1 같은 행에서 열 원소가 겹치는지 확인
  for i in range(9):
    if(sudoku[row][i] == value):
      return False
  #2 같은 열에서 행 원소가 겹치는지 확인
  for i in range(9):
    if(sudoku[i][col] == value):
      return False
  # 3 작은 사각형 내에서 원소가 겹치는지 확인
  rowFirst = (row // 3) * 3;
  colFirst = (col // 3) * 3;
  
  for i in range(rowFirst, rowFirst+3):
     for j in range(colFirst, colFirst+3):
       if(sudoku[i][j] == value):
         return False  
  return True

def DFS(row, col):
  if col == 9 :
    DFS(row+1,0)
    return
  
  if row == 9 :
    for val in sudoku:
        print(" ".join(map(str,val)))
    exit()

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
        

DFS(0, 0)        
    
        
        
                    
            
    