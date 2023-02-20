function solution(weights) {
  weights.sort((a, b) => b - a);
  const cache = {};
  let cnt = 0;
  for (let n of weights) {
    let m;
    if (cache[n]) {
      cnt += cache[n];
    }
    if (((m = (n * 3) / 2), cache[m])) {
      cnt += cache[m];
    }
    if (((m = n * 2), cache[m])) {
      cnt += cache[m];
    }
    if (((m = (n * 4) / 3), cache[m])) {
      cnt += cache[m];
    }

    if (!cache[n]) cache[n] = 1;
    else cache[n]++;
  }

  return cnt;
}

console.log(solution([100, 180, 360, 100, 270]));
