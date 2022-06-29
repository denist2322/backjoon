sudoku = []

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
       