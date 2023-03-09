function solution(n, m, section) {
  let count = 0;
  let start = -1;
  for (let i = 0; i < section.length; i++) {
    if (start === -1) {
      start = section[i] - 1;
      count++;
    } else if (section[i] - start > m) {
      i--;
      start = -1;
    }
  }

  return count;
}
