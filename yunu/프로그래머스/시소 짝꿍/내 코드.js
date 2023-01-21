function solution(weights) {
  const cases = [4 / 3, 3 / 2, 2];

  const dict = {};
  weights.forEach(weight => {
    if (!dict[weight]) dict[weight] = 1;
    else dict[weight]++;
  });

  let answer = 0;
  Object.keys(dict)
    .sort((a, b) => parseInt(a) - parseInt(b))
    .forEach(weight => {
      weight = parseInt(weight);
      answer += (dict[weight] * (dict[weight] - 1)) / 2;
      cases.forEach(num => {
        if (dict[weight * num]) {
          answer += dict[weight] * dict[weight * num];
        }
      });
    });

  return answer;
}

console.log(solution([100, 180, 360, 100, 270]));
