function solution(picks, minerals) {
  const mineralTable = {
    diamond: 25,
    iron: 5,
    stone: 1,
  };

  const sum = (...num) => num.reduce((acc, cur) => acc + cur, 0);

  const splitMinerals = minerals => {
    const result = [];
    for (let i = 0; i < Math.min(minerals.length, sum(...picks) * 5); i++) {
      if (i % 5 === 0) {
        result.push([minerals[i]]);
      } else {
        result.at(-1).push(minerals[i]);
      }
    }
    return result;
  };

  const splitedMinerals = splitMinerals(minerals);

  const sortedMinerals = splitedMinerals.sort(
    (a, b) =>
      sum(...a.map(el => mineralTable[el])) -
      sum(...b.map(el => mineralTable[el]))
  );

  const getTired = (pick, mineral) =>
    Math.ceil(mineralTable[mineral] / 5 ** (2 - pick));

  let answer = 0;
  outer: for (let i = 0; i < picks.length; i++) {
    for (let j = 0; j < picks[i]; j++) {
      answer += sortedMinerals
        .pop()
        .reduce((acc, cur) => acc + getTired(i, cur), 0);
      if (sortedMinerals.length === 0) {
        break outer;
      }
    }
  }

  return answer;
}

console.log(
  solution(
    [1, 3, 2],
    [
      'diamond',
      'diamond',
      'diamond',
      'iron',
      'iron',
      'diamond',
      'iron',
      'stone',
    ]
  )
);
