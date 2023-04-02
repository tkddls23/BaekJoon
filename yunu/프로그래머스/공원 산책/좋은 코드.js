function solution(park, routes) {
  const dirs = { E: [0, 1], W: [0, -1], S: [1, 0], N: [-1, 0] };
  let [x, y] = [0, 0];
  for (let i = 0; i < park.length; i++) {
    if (park[i].includes('S')) {
      [x, y] = [i, park[i].indexOf('S')];
      break;
    }
  }

  routes.forEach(route => {
    const [r, n] = route.split(' ');
    let [nx, ny] = [x, y];
    // 로봇의 충돌 여부를 깔끔하게 구현
    let cnt = 0;
    while (cnt < n) {
      [nx, ny] = [nx + dirs[r][0], ny + dirs[r][1]];
      if (!park[nx] || !park[nx][ny] || park[nx][ny] === 'X') break;
      cnt++;
    }
    if (cnt == n) [x, y] = [nx, ny];
  });
  return [x, y];
}
