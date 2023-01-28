function solution(maps) {
  const visited = Array.from(Array(maps.length), () =>
    Array(maps[0].length).fill(false)
  );

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  const getDays = (x, y) => {
    let res = parseInt(maps[x][y]);
    visited[x][y] = true;
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
      if (visited[nextX][nextY]) continue;
      res += getDays(nextX, nextY);
    }
    return res;
  };

  const answer = [];

  for (let i = 0; i < maps.length; i++) {
    for (let j = 0; j < maps[0].length; j++) {
      if (maps[i][j] === 'X' || visited[i][j]) continue;
      answer.push(getDays(i, j));
    }
  }

  return answer.length === 0 ? [-1] : answer.sort((a, b) => a - b);
}
