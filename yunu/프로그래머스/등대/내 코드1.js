function solution(n, lighthouse) {
  const graph = {};
  lighthouse.forEach(([v1, v2]) => {
    if (!graph[v1]) graph[v1] = [v2];
    else graph[v1].push(v2);
    if (!graph[v2]) graph[v2] = [v1];
    else graph[v2].push(v1);
  });

  const getLeaf = graph =>
    Object.keys(graph).filter(key => graph[key].length === 1);

  const visited = Array(n + 1).fill(false);
  const lighted = Array(n + 1).fill(false);
  const leafs = getLeaf(graph);
  const queue = leafs;
  leafs.forEach(leaf => (visited[leaf] = true));
  while (queue.length) {
    const curr = queue.shift();
    for (const next of graph[curr]) {
      if (visited[next]) continue;
      visited[next] = true;
      lighted[next] = !lighted[curr];
      queue.push(next);
    }
  }

  return lighted.filter(v => v).length;
}
