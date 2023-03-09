function solution(maps) {
  const minRoute = (maps, start, end) => {
    const routes = Array.from(Array(maps.length), () =>
      Array(maps[0].length).fill(Infinity)
    );
    const dx = [1, 0, -1, 0];
    const dy = [0, 1, 0, -1];
    const [startX, startY] = start;
    const [endX, endY] = end;
    routes[startX][startY] = 0;
    const queue = [[startX, startY]];
    while (queue.length) {
      const [x, y] = queue.shift();
      if (x === endX && y === endY) return routes[x][y];
      for (let i = 0; i < 4; i++) {
        const nextX = x + dx[i];
        const nextY = y + dy[i];
        if (nextX < 0 || nextX >= maps.length) continue;
        if (nextY < 0 || nextY >= maps[0].length) continue;
        if (maps[nextX][nextY] === 'X') continue;
        if (routes[x][y] + 1 >= routes[nextX][nextY]) continue;
        routes[nextX][nextY] = routes[x][y] + 1;
        queue.push([nextX, nextY]);
      }
    }
    return -1;
  };

  const point = {};
  for (let i = 0; i < maps.length; i++) {
    for (let j = 0; j < maps[0].length; j++) {
      if (maps[i][j] === 'S') point['start'] = [i, j];
      if (maps[i][j] === 'L') point['lever'] = [i, j];
      if (maps[i][j] === 'E') point['end'] = [i, j];
    }
  }

  maps = maps.map(row => [...row]);

  const startToLever = minRoute(maps, point['start'], point['lever']);
  if (startToLever === -1) return -1;

  const leverToEnd = minRoute(maps, point['lever'], point['end']);
  if (leverToEnd === -1) return -1;

  return startToLever + leverToEnd;
}

console.log(solution(['SOOOL', 'XXXXO', 'OOOOO', 'OXXXX', 'OOOOE']));
console.log(solution(['LOOXS', 'OOOOX', 'OOOOO', 'OOOOO', 'EOOOO']));
