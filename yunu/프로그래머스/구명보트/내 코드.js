function solution(people, limit) {
  const peopleTable = {};
  for (let i = 40; i <= 240; i++) {
    peopleTable[i] = 0;
  }
  people.forEach(p => {
    peopleTable[p]++;
  });

  let answer = 0;
  let count = people.length;
  while (count > 0) {
    let weightLimit = limit;
    let peopleLimit = 2;
    for (let weight = limit; weight >= 40 && peopleLimit > 0; ) {
      if (peopleTable[weight] === 0) {
        weight--;
        continue;
      }
      peopleTable[weight]--;
      count--;
      weight = weightLimit - weight;
      weightLimit = weight;
      peopleLimit--;
    }
    answer++;
  }

  return answer;
}

console.log(solution([70, 50, 80, 50], 100));
console.log(solution([70, 50, 80], 100));
