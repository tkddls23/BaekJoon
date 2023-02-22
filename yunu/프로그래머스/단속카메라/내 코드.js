function solution(routes) {
  routes.sort((a, b) => a[0] - b[0]);

  let answer = 0;
  let curr = -30001;
  for (const [start, end] of routes) {
    if (curr < start) {
      curr = end;
      answer++;
    } else if (curr >= end) {
      curr = end;
    }
  }

  return answer;
}
