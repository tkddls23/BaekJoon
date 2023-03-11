function solution(scores) {
  const n = scores.length;
  const wanho = scores[0];

  const peerMaxTable = scores.reduce((prev, [work, peer]) => {
    if (!prev[work]) prev[work] = peer;
    else prev[work] = Math.max(prev[work], peer);
    return prev;
  }, {});

  const peerMinTable = {};
  let prevMax = -1;
  Object.keys(peerMaxTable)
    .sort((a, b) => +b - +a)
    .forEach(work => {
      if (peerMaxTable[work] > prevMax) {
        peerMinTable[work] = prevMax;
        prevMax = peerMaxTable[work];
      } else {
        peerMinTable[work] = prevMax;
      }
    });

  const bonusPeer = [];
  for (let i = 0; i < n; i++) {
    if (scores[i][1] >= peerMinTable[scores[i][0]]) {
      bonusPeer.push(scores[i]);
    }
  }

  const rankPeer = bonusPeer
    .map(([work, peer]) => [work + peer, work, peer])
    .sort((a, b) => b[0] - a[0]);

  let rank = 0;
  let count = 0;
  let prev = -1;
  for (let i = 0; i < rankPeer.length; i++) {
    count++;
    if (prev !== rankPeer[i][0]) {
      rank = count;
      prev = rankPeer[i][0];
    }
    if (rankPeer[i][1] === wanho[0] && rankPeer[i][2] === wanho[1]) {
      return rank;
    }
  }

  return -1;
}

console.log(
  solution([
    [2, 2],
    [1, 4],
    [3, 2],
    [3, 2],
    [2, 1],
  ])
);

// console.log(
//   solution([
//     [0, 2],
//     [0, 4],
//     [0, 3],
//     [0, 3],
//     [1, 3],
//   ])
// );

// console.log(solution([[0, 1]]));

/**
테스트 1 〉	통과 (0.11ms, 33.4MB)
테스트 2 〉	통과 (0.12ms, 33.5MB)
테스트 3 〉	통과 (0.12ms, 33.4MB)
테스트 4 〉	실패 (0.13ms, 33.5MB)
테스트 5 〉	통과 (0.13ms, 33.4MB)
테스트 6 〉	통과 (0.13ms, 33.4MB) -> -1
테스트 7 〉	통과 (0.14ms, 33.4MB)
테스트 8 〉	통과 (0.28ms, 33.5MB)
테스트 9 〉	통과 (0.31ms, 33.5MB) -> -1
테스트 10 〉	통과 (0.33ms, 33.5MB)
테스트 11 〉	실패 (0.57ms, 33.6MB)
테스트 12 〉	통과 (0.56ms, 33.5MB)
테스트 13 〉	통과 (0.99ms, 33.8MB) -> -1
테스트 14 〉	통과 (0.95ms, 33.8MB)
테스트 15 〉	통과 (3.85ms, 36.5MB) -> -1
테스트 16 〉	통과 (3.94ms, 36.6MB)
테스트 17 〉	통과 (6.40ms, 37.8MB)
테스트 18 〉	통과 (6.53ms, 38.1MB)
테스트 19 〉	통과 (37.22ms, 46.6MB) -> -1
테스트 20 〉	통과 (38.08ms, 46MB) -> -1
테스트 21 〉	통과 (45.41ms, 70.8MB)
테스트 22 〉	실패 (68.56ms, 57.1MB)
테스트 23 〉	통과 (74.32ms, 57.3MB) -> -1
테스트 24 〉	실패 (22.52ms, 58.5MB)
테스트 25 〉	통과 (117.75ms, 78.9MB)

테스트 1 〉	통과 (0.11ms, 33.4MB)
테스트 2 〉	통과 (0.13ms, 33.4MB)
테스트 3 〉	통과 (0.13ms, 33.6MB)
테스트 4 〉	통과 (0.14ms, 33.6MB)
테스트 5 〉	통과 (0.14ms, 33.4MB)
테스트 6 〉	실패 (0.21ms, 33.4MB) -> -1
테스트 7 〉	통과 (0.22ms, 33.4MB)
테스트 8 〉	실패 (0.28ms, 33.5MB)
테스트 9 〉	실패 (0.38ms, 33.5MB) -> -1
테스트 10 〉	통과 (0.31ms, 33.6MB)
테스트 11 〉	실패 (0.95ms, 33.7MB)
테스트 12 〉	통과 (0.58ms, 33.5MB)
테스트 13 〉	실패 (1.71ms, 34MB) -> -1
테스트 14 〉	통과 (0.96ms, 33.8MB)
테스트 15 〉	실패 (8.29ms, 37.6MB) -> -1
테스트 16 〉	실패 (24.52ms, 36.5MB)
테스트 17 〉	통과 (15.26ms, 39.6MB)
테스트 18 〉	통과 (7.42ms, 37.7MB)
테스트 19 〉	실패 (60.36ms, 55.8MB) -> -1
테스트 20 〉	실패 (43.19ms, 48.1MB) -> -1
테스트 21 〉	통과 (44.68ms, 71MB)
테스트 22 〉	실패 (117.65ms, 67MB)
테스트 23 〉	실패 (89.33ms, 63.4MB) -> -1
테스트 24 〉	통과 (94.06ms, 81.9MB)
테스트 25 〉	통과 (144.67ms, 82.6MB)
 */
