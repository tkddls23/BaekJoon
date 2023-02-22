function solution(n, edge) {
  const graph = {};
  edge.forEach(([v1, v2]) => {
    if (!graph[v1]) graph[v1] = [v2];
    else graph[v1].push(v2);
    if (!graph[v2]) graph[v2] = [v1];
    else graph[v2].push(v1);
  });

  const visited = Array(n + 1).fill(false);
  const dist = Array(n + 1).fill(0);
  visited[1] = true;
  dist[1] = 0;
  const queue = [1];
  while (queue.length) {
    const prev = queue.shift();
    for (const next of graph[prev]) {
      if (visited[next]) continue;
      visited[next] = true;
      dist[next] = dist[prev] + 1;
      queue.push(next);
    }
  }

  let maxDist = 0;
  for (let i = 1; i < dist.length; i++) {
    maxDist = Math.max(maxDist, dist[i]);
  }

  return dist.filter(v => v === maxDist).length;
}

// // 다익스트라 풀이인데 시간이 오래 걸린다.
// function solution(n, edge) {

//   const queue = {
//       arr: Array(5000000).fill(null),
//       front: 0,
//       rear: 0,
//       push(data) {
//           this.rear = (this.rear + 1) % 5000000;
//           this.arr[this.rear] = data;
//       },
//       shift() {
//           this.front = (this.front + 1) % 5000000;
//           return this.arr[this.front];
//       },
//       isEmpty() {
//           return this.rear === this.front;
//       }
//   }

//   const graph = {};
//   edge.forEach(([v1, v2]) => {
//       if (!graph[v1]) graph[v1] = [v2];
//       else graph[v1].push(v2);
//       if (!graph[v2]) graph[v2] = [v1];
//       else graph[v2].push(v1);
//   });

//   const dist = Array(n + 1).fill(Infinity);
//   dist[1] = 0;
//   queue.push(1);
//   while (!queue.isEmpty()) {
//       const prev = queue.shift();
//       for (const next of graph[prev]) {
//           if (dist[next] < dist[prev] + 1) continue;
//           dist[next] = dist[prev] + 1;
//           queue.push(next);
//       }
//   }

//   let maxDist = 0;
//   for (let i = 1; i < dist.length; i++) {
//       if (dist[i] === Infinity) continue;
//       maxDist = Math.max(maxDist, dist[i]);
//   }

//   return dist.filter(v => v === maxDist).length;
// }
