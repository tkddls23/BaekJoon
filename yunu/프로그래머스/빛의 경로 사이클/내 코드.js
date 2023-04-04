function solution(grid) {
  // 오른쪽, 아래, 왼쪽, 위
  const dirY = [0, 1, 0, -1];
  const dirX = [1, 0, -1, 0];

  const visited = grid.map(row =>
    [...row].map(() => [false, false, false, false])
  );

  const getDir = (y, x, dir) => {
    switch (grid[y][x]) {
      case 'S':
        return dir;
      case 'L':
        return (dir + 3) % 4;
      case 'R':
        return (dir + 1) % 4;
    }
  };

  const getY = y => {
    if (y >= grid.length) {
      return 0;
    } else if (y < 0) {
      return grid.length - 1;
    }
    return y;
  };

  const getX = x => {
    if (x >= grid[0].length) {
      return 0;
    } else if (x < 0) {
      return grid[0].length - 1;
    }
    return x;
  };

  const isCycle = (y, x, dir) => {
    visited[y][x][dir] = true;
    let count = 1;
    let nextY = getY(y + dirY[dir]);
    let nextX = getX(x + dirX[dir]);
    let nextDir = getDir(nextY, nextX, dir);
    while (!visited[nextY][nextX][nextDir]) {
      visited[nextY][nextX][nextDir] = true;
      count++;
      nextY = getY(nextY + dirY[nextDir]);
      nextX = getX(nextX + dirX[nextDir]);
      nextDir = getDir(nextY, nextX, nextDir);
    }
    if (y === nextY && x === nextX && dir === nextDir) {
      return count;
    }
  };

  const answer = [];
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      for (let k = 0; k < 4; k++) {
        if (visited[i][j][k]) continue;
        const count = isCycle(i, j, k);
        if (count) {
          answer.push(count);
        }
      }
    }
  }

  return answer.sort((a, b) => b - a);
}

console.log(solution(['SL', 'LR']));
console.log(solution(['S']));
console.log(solution(['R', 'R']));
