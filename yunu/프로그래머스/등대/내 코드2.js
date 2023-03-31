function solution(n, lighthouse) {
  const graph = {};
  lighthouse.forEach(([v1, v2]) => {
    if (!graph[v1]) graph[v1] = [v2];
    else graph[v1].push(v2);
    if (!graph[v2]) graph[v2] = [v1];
    else graph[v2].push(v1);
  });

  const visited = Array(n + 1).fill(false);
  const tree = {};
  const getTree = node => {
    const child = graph[node].filter(el => !visited[el]);
    tree[node] = [...child];
    visited[node] = true;
    if (child.length === 0) return;
    child.forEach(el => getTree(el));
  };

  getTree(1);

  const cache = Array(n + 1).fill([-1, -1]);

  const getMinLightHouse = node => {
    if (cache[node][0] !== -1 || cache[node][1] !== -1) return cache[node];
    if (tree[node].length === 0) {
      cache[node] = [0, 1];
      return cache[node];
    }
    cache[node] = [0, 1];
    return tree[node]
      .map(el => getMinLightHouse(el))
      .reduce((acc, cur) => {
        acc[0] += cur[1];
        acc[1] += Math.min(...cur);
        return acc;
      }, cache[node]);
  };

  return Math.min(...getMinLightHouse(1, graph[1]));
}

// console.log(
//   solution(8, [
//     [1, 2],
//     [1, 3],
//     [1, 4],
//     [1, 5],
//     [5, 6],
//     [5, 7],
//     [5, 8],
//   ])
// );
console.log(
  solution(10, [
    [4, 1],
    [5, 1],
    [5, 6],
    [7, 6],
    [1, 2],
    [1, 3],
    [6, 8],
    [2, 9],
    [9, 10],
  ])
);
