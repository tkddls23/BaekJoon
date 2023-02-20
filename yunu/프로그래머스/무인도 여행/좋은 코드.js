function solution(maps) {
  maps = maps.map(row => [...row]);

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  const getDays = (x, y) => {
    let res = parseInt(maps[x][y]);
    maps[x][y] = 'X';
    for (let i = 0; i < 4; i++) {
      const nextX = x + dx[i];
      const nextY = y + dy[i];
      if (
        nextX < 0 ||
        nextY < 0 ||
        nextX >= maps.length ||
        nextY >= maps[0].length
      )
        continue;
      if (maps[nextX][nextY] === 'X') continue;
      res += getDays(nextX, nextY);
    }
    return res;
  };

  const answer = [];

  for (let i = 0; i < maps.length; i++) {
    for (let j = 0; j < maps[0].length; j++) {
      if (maps[i][j] === 'X') continue;
      answer.push(getDays(i, j));
    }
  }

  return answer.length === 0 ? [-1] : answer.sort((a, b) => a - b);
}

console.log(solution(['X591X', 'X1X5X', 'X231X', '1XXX1']));
