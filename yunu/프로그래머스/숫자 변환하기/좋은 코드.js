function solution(x, y, n) {
  const dp = Array(y + 1).fill(-1);
  dp[x] = 0;
  for (let i = x; i <= y; i++) {
    if (dp[i] === -1) continue;
    for (const num of [i + n, i * 2, i * 3]) {
      if (num > y) continue;
      if (dp[num] === -1) dp[num] = dp[i] + 1;
    }
  }
  return dp[y];
}

console.log(solution(10, 40, 5));
console.log(solution(10, 40, 30));
console.log(solution(2, 5, 4));

// function solution(x, y, n) {
//   const dp = Array(y + 1).fill(-1);
//   dp[x] = 0;
//   for (let i = x; i <= y; i++) {
//     if (dp[i] === -1) continue;
//     for (const num of [n, 2, 3]) {
//       const nextNum = num === n ? i + num : i * num;
//       if (nextNum > y) continue;
//       if (dp[nextNum] === -1 || dp[nextNum] > dp[i] + 1)
//         dp[nextNum] = dp[i] + 1;
//     }
//   }
//   return dp[y];
// }
