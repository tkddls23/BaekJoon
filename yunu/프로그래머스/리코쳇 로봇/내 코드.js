function solution(board) {
  const getR = board => {
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[0].length; j++) {
        if (board[i][j] === 'R') return [i, j];
      }
    }
    return [-1, -1];
  };
  const getLast = (board, y1, x1, y2, x2) => {
    const dy = y2 - y1;
    const dx = x2 - x1;
    let nextY = y2 + dy;
    let nextX = x2 + dx;
    while (true) {
      if (
        nextY < 0 ||
        nextY >= board.length ||
        nextX < 0 ||
        nextX >= board[0].length
      ) {
        break;
      }
      if (board[nextY][nextX] === 'D') {
        break;
      }
      nextY += dy;
      nextX += dx;
    }
    return [nextY - dy, nextX - dx];
  };
  // board = board.map(row => [...row]);
  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];
  const visited = board.map(row => [...row].map(() => false));
  const [ry, rx] = getR(board);
  visited[ry][rx] = true;
  const queue = [[ry, rx, 0]];
  while (queue.length) {
    const [y, x, length] = queue.shift();
    if (board[y][x] === 'G') return length;
    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];
      if (
        nextY < 0 ||
        nextY >= board.length ||
        nextX < 0 ||
        nextX >= board[0].length
      ) {
        continue;
      }
      if (board[nextY][nextX] === 'D') {
        continue;
      }
      const [lastY, lastX] = getLast(board, y, x, nextY, nextX);
      if (visited[lastY][lastX]) continue;
      visited[lastY][lastX] = true;
      queue.push([lastY, lastX, length + 1]);
    }
  }

  return -1;
}

console.log(solution(['...D..R', '.D.G...', '....D.D', 'D....D.', '..D....']));
console.log(solution(['.D.R', '....', '.G..', '...D']));
