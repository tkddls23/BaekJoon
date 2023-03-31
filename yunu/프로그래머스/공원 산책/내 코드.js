function solution(park, routes) {
  const dir = {
    N: [-1, 0],
    S: [1, 0],
    W: [0, -1],
    E: [0, 1],
  };
  const getStartYX = () => {
    for (let i = 0; i < park.length; i++)
      for (let j = 0; j < park[0].length; j++)
        if (park[i][j] === 'S') return [i, j];
  };
  const isBlock = (sy, sx, ey, ex) => {
    [sy, ey] = [sy, ey].sort((a, b) => a - b);
    [sx, ex] = [sx, ex].sort((a, b) => a - b);
    for (let i = sy; i <= ey; i++)
      for (let j = sx; j <= ex; j++) if (park[i][j] === 'X') return true;
    return false;
  };
  let [y, x] = getStartYX();
  for (const route of routes) {
    const [op, n] = route.split(' ');
    const [dirY, dirX] = dir[op].map(el => el * Number(n));
    const nextY = y + dirY;
    const nextX = x + dirX;
    if (
      nextY < 0 ||
      nextY >= park.length ||
      nextX < 0 ||
      nextX >= park[0].length
    ) {
      continue;
    }
    if (isBlock(y, x, nextY, nextX)) {
      continue;
    }
    y = nextY;
    x = nextX;
  }

  return [y, x];
}

// console.log(solution(['XXX', 'XSX', 'XXX'], ['E 1'])); // [1,1]
console.log(solution(['XXX', 'XSX', 'XXX'], ['W 1'])); // [1,1]
console.log(solution(['XXX', 'XSX', 'XXX'], ['S 1'])); // [1,1]
console.log(solution(['XXX', 'XSX', 'XXX'], ['N 1'])); // [1,1]

console.log(solution(['SOXOO', 'OOOOO', 'OOOOO', 'OOOOO', 'OOOOO'], ['E 3'])); // [0, 0]
console.log(solution(['SOOOX', 'OOOOO', 'OOOOO', 'OOOOO', 'OOOOO'], ['E 3'])); // [0, 3]
console.log(solution(['XOOOS', 'OOOOO', 'OOOOO', 'OOOOO', 'OOOOO'], ['W 3'])); // [0, 1]
console.log(solution(['OOXOS', 'OOOOO', 'OOOOO', 'OOOOO', 'OOOOO'], ['W 3'])); // [0, 4]
console.log(solution(['SOOOO', 'OOOOO', 'XOOOO', 'OOOOO', 'OOOOO'], ['S 3'])); // [0, 0]
console.log(solution(['SOOOO', 'OOOOO', 'OOOOO', 'OOOOO', 'XOOOO'], ['S 3'])); // [3, 0]
console.log(solution(['OOOOO', 'OOOOO', 'XOOOO', 'OOOOO', 'SOOOO'], ['N 3'])); // [4, 0]
console.log(solution(['XOOOO', 'OOOOO', 'OOOOO', 'OOOOO', 'SOOOO'], ['N 3'])); // [1, 0]
