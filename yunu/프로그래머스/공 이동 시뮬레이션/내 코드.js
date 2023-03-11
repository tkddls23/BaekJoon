function solution(n, m, x, y, queries) {
  const boundary = [x, y, x, y];

  for (const [command, dx] of queries.reverse()) {
    const [x1, y1, x2, y2] = boundary;
    switch (command) {
      case 0:
        if (y1 === 0) boundary[1] = y1;
        else {
          boundary[1] = y1 + dx;
          if (boundary[1] > m - 1) return 0;
        }
        boundary[3] = y2 + dx > m - 1 ? m - 1 : y2 + dx;
        break;
      case 1:
        if (y2 === m - 1) boundary[3] = y2;
        else {
          boundary[3] = y2 - dx;
          if (boundary[3] < 0) return 0;
        }
        boundary[1] = y1 - dx >= 0 ? y1 - dx : 0;
        break;
      case 2:
        if (x1 === 0) boundary[0] = x1;
        else {
          boundary[0] = x1 + dx;
          if (boundary[0] > n - 1) return 0;
        }
        boundary[2] = x2 + dx > n - 1 ? n - 1 : x2 + dx;
        break;
      case 3:
        if (x2 === n - 1) boundary[2] = x2;
        else {
          boundary[2] = x2 - dx;
          if (boundary[2] < 0) return 0;
        }
        boundary[0] = x1 - dx >= 0 ? x1 - dx : 0;
    }
  }

  return BigInt(
    (boundary[2] - boundary[0] + 1) * (boundary[3] - boundary[1] + 1)
  );
}

// console.log(
//   solution(2, 2, 0, 0, [
//     [2, 1],
//     [0, 1],
//     [1, 1],
//     [0, 1],
//     [2, 1],
//   ])
// );

console.log(
  solution(2, 5, 0, 1, [
    [3, 1],
    [2, 2],
    [1, 1],
    [2, 3],
    [0, 1],
    [2, 1],
  ])
);
