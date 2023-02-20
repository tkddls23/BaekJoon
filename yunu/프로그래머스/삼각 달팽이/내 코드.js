function solution(n) {
  const arr = [];
  for (let i = 1; i <= n; i++) {
    arr.push(Array(i).fill(null));
  }
  const dir = [
    [1, 0],
    [0, 1],
    [-1, -1],
  ];
  let x = 0;
  let y = 0;
  let num = 1;
  while (!arr[x][y]) {
    arr[x][y] = num++;
    for (let [dirX, dirY] of [...dir]) {
      const nextX = x + dirX;
      const nextY = y + dirY;
      if (
        nextX >= 0 &&
        nextY >= 0 &&
        nextX < n &&
        nextY < n &&
        arr[nextX][nextY] === null
      ) {
        x = nextX;
        y = nextY;
        break;
      }
      dir.push(dir.shift());
    }
  }

  return arr.reduce((prev, curr) => {
    prev.push(...curr);
    return prev;
  }, []);
}

console.log(solution(3));
console.log(solution(4));
console.log(solution(5));
console.log(solution(6));
