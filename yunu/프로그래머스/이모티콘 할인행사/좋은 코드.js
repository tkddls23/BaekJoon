function solution(users, emoticons) {
  const sales = [10, 20, 30, 40];
  let cases = [[]];
  for (let i = 0; i < emoticons.length; i++) {
    const newCases = [];
    for (let prevCase of cases) {
      sales.forEach(sale => newCases.push([...prevCase, sale]));
    }
    cases = newCases;
  }
  let answer = [0, 0];
  for (let saleCase of cases) {
    const candidate = [0, 0];
    for (let [ratio, costThreshold] of users) {
      let cost = saleCase.reduce((c, sale, i) => {
        return c + (sale >= ratio ? (emoticons[i] * (100 - sale)) / 100 : 0);
      }, 0);
      if (cost >= costThreshold) candidate[0]++;
      else candidate[1] += cost;
    }
    if (
      candidate[0] > answer[0] ||
      (candidate[0] === answer[0] && candidate[1] > answer[1])
    )
      answer = candidate;
  }
  return answer;
}
