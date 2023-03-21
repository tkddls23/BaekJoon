function solution(sticker) {
  const n = sticker.length;

  if (n <= 3) {
    return Math.max(...sticker);
  }

  const dp1 = Array(n).fill(0);
  const dp2 = Array(n).fill(0);

  dp1[0] = sticker[0];
  dp1[1] = dp1[0];
  for (let i = 2; i < n - 1; i++) {
    dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
  }

  dp2[1] = sticker[1];
  for (let i = 2; i < n; i++) {
    dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
  }

  return Math.max(dp1[n - 2], dp2[n - 1]);
}
