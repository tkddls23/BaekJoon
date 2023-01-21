function solution(scores) {
  const wanhoScore = scores[0];
  let currMaxScore = 0;
  let answer = 1;

  scores.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]));

  for (let i = 0; i < scores.length; i++) {
    if (scores[i][1] < currMaxScore) {
      if (scores[i] == wanhoScore) return -1;
    } else {
      currMaxScore = Math.max(scores[i][1], currMaxScore);
      if (scores[i][0] + scores[i][1] > wanhoScore[0] + wanhoScore[1])
        answer += 1;
    }
  }

  return answer;
}

console.log(
  solution([
    [2, 2],
    [1, 4],
    [3, 2],
    [3, 2],
    [2, 1],
  ])
);

console.log(
  solution([
    [5, 1],
    [5, 0],
    [4, 1],
    [3, 2],
    [2, 3],
    [1, 4],
    [0, 5],
  ])
);

// console.log(solution([[0, 1]]));
