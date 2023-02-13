function solution(n, build_frame) {
  const town = [];
  for (let i = 0; i <= n + 2; i++) {
    town.push([]);
    for (let j = 0; j <= n; j++) {
      town[i].push({ 0: false, 1: false }); // 기둥, 보
    }
  }

  const checkTown = town => {
    for (let i = 1; i < town.length; i++) {
      for (let j = 0; j < town[i].length; j++) {
        if (town[i][j][0]) {
          if (j === 0) continue;
          if (town[i][j - 1][0]) continue;
          if (town[i][j][1] || town[i - 1][j][1]) continue;
          return false;
        }
        if (town[i][j][1]) {
          if (j === 0) return false;
          if (town[i][j - 1][0] || town[i + 1][j - 1][0]) continue;
          if (town[i - 1][j][1] && town[i + 1][j][1]) continue;
          return false;
        }
      }
    }
    return true;
  };

  build_frame.forEach(([x, y, a, b]) => {
    town[x + 1][y][a] = !!b;
    if (!checkTown(town)) town[x + 1][y][a] = !b;
  });

  let answer = [];
  for (let i = 0; i < town.length; i++) {
    for (let j = 0; j < town[i].length; j++) {
      if (town[i][j][0]) answer.push([i - 1, j, 0]);
      if (town[i][j][1]) answer.push([i - 1, j, 1]);
    }
  }

  answer.sort((a, b) => a[0] - b[0]);

  return answer;
}

console.log(
  solution(5, [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 0, 1],
    [2, 2, 1, 1],
    [5, 0, 0, 1],
    [5, 1, 0, 1],
    [4, 2, 1, 1],
    [3, 2, 1, 1],
    [2, 1, 0, 0],
  ])
);

console.log(
  solution(5, [
    [0, 0, 0, 1],
    [2, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 1, 1, 1],
    [2, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 0, 1],
  ])
);
