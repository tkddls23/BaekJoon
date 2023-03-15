function solution(sticker) {
  const n = sticker.length;

  if (n <= 3) {
    return Math.max(...sticker);
  }

  const dp0 = Array(n).fill(0);
  const dp1 = Array(n).fill(0);

  dp0[0] = sticker[0];
  dp0[2] = dp0[0] + sticker[2];
  dp1[1] = sticker[1];
  dp1[2] = sticker[2];

  let max = Math.max(dp0[0], dp0[2], dp1[1]);
  for (let i = 3; i < n; i++) {
    if (i < n - 1) {
      dp0[i] = sticker[i] + Math.max(dp0[i - 2], dp0[i - 3]);
    }
    dp1[i] = sticker[i] + Math.max(dp1[i - 2], dp1[i - 3]);
    max = Math.max(max, dp0[i], dp1[i]);
  }

  return max;
}
