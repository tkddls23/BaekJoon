function solution(edges, target) {
  const graph = {};
  edges.forEach(([parent, child]) => {
    if (!graph[parent]) graph[parent] = { child: [child], turn: 0 };
    else graph[parent]['child'].push(child);
  });

  Object.keys(graph).forEach(parent => {
    graph[parent]['child'].sort((a, b) => a - b);
  });

  const targetMinMax = {};
  target.forEach((sum, index) => {
    targetMinMax[index + 1] = [parseInt((sum + 2) / 3), sum];
  });

  const targetTable = {};
  const targetOrder = [];
  const targetVisited = Array(target.length).fill(false);
  let isComplete = target.reduce(
    (prev, curr) => (curr === 0 ? prev + 1 : prev),
    0
  );
  while (isComplete < target.length) {
    let node = 1;
    while (graph[node]) {
      const turn = graph[node]['turn']++ % graph[node]['child'].length;
      node = graph[node]['child'][turn];
    }
    if (!targetTable[node]) targetTable[node] = 1;
    else targetTable[node]++;
    if (targetTable[node] > targetMinMax[node][1]) return [-1];
    else if (
      !targetVisited[node] &&
      targetTable[node] <= targetMinMax[node][1] &&
      targetTable[node] >= targetMinMax[node][0]
    ) {
      isComplete++;
      targetVisited[node] = true;
    }
    targetOrder.push(node);
  }

  const getMinArr = (len, num) => {
    const res = [];
    while (len > 0) {
      for (let i = 1; i <= 3; i++) {
        if ((num - i) / (len - 1) > 3) continue;
        len--;
        num -= i;
        res.push(i);
        break;
      }
    }
    return res;
  };

  const targetAnswer = {};
  for (const node in targetTable) {
    targetAnswer[node] = {
      arr: getMinArr(targetTable[node], target[+node - 1]),
      turn: 0,
    };
  }

  return targetOrder.map(node => {
    const turn = targetAnswer[node]['turn']++;
    return targetAnswer[node]['arr'][turn];
  });
}

console.log(
  solution(
    [
      [2, 4],
      [1, 2],
      [6, 8],
      [1, 3],
      [5, 7],
      [2, 5],
      [3, 6],
      [6, 10],
      [6, 9],
    ],
    [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
  )
);
console.log(
  solution(
    [
      [1, 2],
      [1, 3],
    ],
    [0, 7, 3]
  )
);
console.log(
  solution(
    [
      [1, 3],
      [1, 2],
    ],
    [0, 7, 1]
  )
);
