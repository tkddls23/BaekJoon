function solution(n, m, x, y, r, c, k) {
  const dir = { d: [1, 0], l: [0, -1], r: [0, 1], u: [-1, 0] };
  let answer = '';
  let curr = k;

  const isPossible = (n, m, x, y, r, c, k) => {
    const res = Math.abs(x - r) + Math.abs(y - c);
    return !(x < 1 || x > n || y < 1 || y > m || res > k || res % 2 !== k % 2);
  };

  if (!isPossible(n, m, x, y, r, c, k)) return 'impossible';

  while (answer.length < k) {
    for (const key in dir) {
      if (isPossible(n, m, x + dir[key][0], y + dir[key][1], r, c, curr - 1)) {
        answer += key;
        x += dir[key][0];
        y += dir[key][1];
        curr -= 1;
        break;
      }
    }
  }
  return answer;
}

console.log(solution(3, 4, 2, 3, 3, 1, 5));
console.log(solution(2, 2, 1, 1, 2, 2, 2));
console.log(solution(3, 3, 1, 2, 3, 3, 4));
