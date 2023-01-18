function solution(info, edges) {
  const graph = {};
  edges.forEach(([start, end]) => {
    if (!graph[start]) graph[start] = [end];
    else graph[start].push(end);
  });

  let answer = 0;
  const stack = [{ sheep: 1, wolf: 0, nodes: graph[0] }];
  while (stack.length) {
    const { sheep, wolf, nodes } = stack.pop();
    if (sheep <= wolf) continue;
    answer = Math.max(answer, sheep);
    for (let i = 0; i < nodes.length; i++) {
      if (info[nodes[i]] === 0) {
        stack.push({
          sheep: sheep + 1,
          wolf,
          nodes: [
            ...nodes.filter((_, index) => i !== index),
            ...(graph[nodes[i]] || []),
          ],
        });
      } else {
        stack.push({
          sheep,
          wolf: wolf + 1,
          nodes: [
            ...nodes.filter((_, index) => i !== index),
            ...(graph[nodes[i]] || []),
          ],
        });
      }
    }
  }

  return answer;
}

console.log(
  solution(
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [
      [0, 1],
      [1, 2],
      [1, 4],
      [0, 8],
      [8, 7],
      [9, 10],
      [9, 11],
      [4, 3],
      [6, 5],
      [4, 6],
      [8, 9],
    ]
  )
);

console.log(
  solution(
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [
      [0, 1],
      [0, 2],
      [1, 3],
      [1, 4],
      [2, 5],
      [2, 6],
      [3, 7],
      [4, 8],
      [6, 9],
      [9, 10],
    ]
  )
);

console.log(
  solution(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [
      [0, 1],
      [0, 2],
      [1, 3],
      [1, 4],
      [2, 5],
      [2, 6],
      [3, 7],
      [3, 8],
      [4, 9],
      [4, 10],
      [5, 11],
      [5, 12],
      [6, 13],
      [6, 14],
      [7, 15],
      [7, 16],
    ]
  )
);
