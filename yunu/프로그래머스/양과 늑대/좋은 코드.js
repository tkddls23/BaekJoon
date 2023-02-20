// 바킹독 풀이
function solution(info, edges) {
  const left = Array(20).fill(-1);
  const right = Array(20).fill(-1);

  edges.forEach(([parent, child]) => {
    if (left[parent] === -1) left[parent] = child;
    else right[parent] = child;
  });

  let answer = 0;
  const visited = Array(1 << 17).fill(0);
  const solve = state => {
    if (visited[state]) return;
    visited[state] = 1;

    let wolf = 0;
    let total = 0;

    for (let i = 0; i < info.length; i++) {
      if (state & (1 << i)) {
        total++;
        wolf += info[i];
      }
    }
    if (2 * wolf >= total) return;
    answer = Math.max(answer, total - wolf);

    for (let i = 0; i < info.length; i++) {
      if (!(state & (1 << i))) continue;
      if (left[i] !== -1) solve(state | (1 << left[i]));
      if (right[i] !== -1) solve(state | (1 << right[i]));
    }
  };
  solve(1);
  return answer;
}

// 바킹독 풀이에서 left, right를 보기 좋게 바꿈
function solution(info, edges) {
  const graph = {};
  edges.forEach(([start, end]) => {
    if (!graph[start]) graph[start] = [end];
    else graph[start].push(end);
  });

  let answer = 0;
  const visited = Array(1 << 17).fill(0);
  const solve = (state, wolf, total) => {
    if (visited[state]) return;
    visited[state] = 1;

    if (2 * wolf >= total) return;
    answer = Math.max(answer, total - wolf);

    for (let i = 0; i < info.length; i++) {
      if (!(state & (1 << i))) continue;
      for (const next of graph[i] || []) {
        solve(state | (1 << next), wolf + info[next], total + 1);
      }
    }
  };

  solve(1, 0, 1);
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
