function solution(e, starts) {
  const divisors = Array(e + 1).fill(0);
  for (let i = 1; i <= e; i++) {
    for (let j = 1; j <= e / i; j++) {
      divisors[i * j]++;
    }
  }

  const minDivisors = Array(e + 1).fill(0);
  minDivisors[e] = e;
  for (let i = e - 1; i >= 1; i--) {
    if (divisors[i] >= divisors[minDivisors[i + 1]]) {
      minDivisors[i] = i;
      continue;
    }
    minDivisors[i] = minDivisors[i + 1];
  }

  const answer = starts.map(start => minDivisors[start]);
  return answer;
}
