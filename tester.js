const sumMatrixRegion = (matrix, [topLeftCol, topLeftRow], [botRightCol, botRightRow]) => {
  let sum = 0
  
  for (let row = topLeftRow; row <= botRightRow; row += 1) {
    for (let col = topLeftCol; col <= botRightCol; col += 1) {
      sum += matrix[row][col]
    }
  }
  
  return sum
}
​
const inputMatrix = [
  [1, 2, 3, 4], 
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]
​
const sum = sumMatrixRegion(inputMatrix, [1, 1], [3, 2]) 
