function solution(n, m, x, y, r, c, k) {
  const dir = { d: [1, 0], l: [0, -1], r: [0, 1], u: [-1, 0] };

  const getMinLength = (x1, y1, x2, y2) => {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
  };

  const getMinRoute = (x1, y1, x2, y2) => {
    const ud = x2 - x1 < 0 ? 'u'.repeat(x1 - x2) : 'd'.repeat(x2 - x1);
    const lr = y2 - y1 < 0 ? 'l'.repeat(y1 - y2) : 'r'.repeat(y2 - y1);
    return ud + lr > lr + ud ? lr + ud : ud + lr;
  };

  if ((k - getMinLength(x, y, r, c)) % 2 === 1) return 'impossible';
  if (getMinLength(x, y, r, c) > k) return 'impossible'; // 이 경우를 계속 빼먹음

  const route = [];
  while (route.length < k) {
    for (const key in dir) {
      const [dirX, dirY] = dir[key];
      const nextX = x + dirX;
      const nextY = y + dirY;
      if (nextX <= 0 || nextX > n || nextY <= 0 || nextY > m) continue;
      if (route.length + 1 + getMinLength(nextX, nextY, r, c) > k) continue;
      route.push(key);
      x = nextX;
      y = nextY;
      break;
    }
    if (route.length + getMinLength(x, y, r, c) === k) {
      route.push(getMinRoute(x, y, r, c));
      break;
    }
  }

  return route.join('');
}

console.log(solution(3, 4, 2, 3, 3, 1, 5));
console.log(solution(2, 2, 1, 1, 2, 2, 2));
console.log(solution(3, 3, 1, 2, 3, 3, 4));
