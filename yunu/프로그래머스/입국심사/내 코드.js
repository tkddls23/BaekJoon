function solution(n, times) {
  times.sort((a, b) => a - b);

  const canCheck = time => {
    let res = 0;
    times.forEach(t => {
      res += parseInt(time / t);
    });
    return res >= n;
  };

  let low = 1;
  let high = Math.max(...times) * n;
  while (low + 1 < high) {
    const mid = parseInt((low + high) / 2);
    if (canCheck(mid)) high = mid;
    else low = mid;
  }

  return high;
}

console.log(solution(6, [7, 10]));
