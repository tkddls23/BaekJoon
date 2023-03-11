function solution(keymap, targets) {
  const alphaTable = {};
  keymap.forEach(map => {
    for (let i = 0; i < map.length; i++) {
      if (!alphaTable[map[i]]) alphaTable[map[i]] = i + 1;
      else alphaTable[map[i]] = Math.min(alphaTable[map[i]], i + 1);
    }
  });

  return targets.map(target => {
    let count = 0;
    for (const alpha of target) {
      if (!alphaTable[alpha]) return -1;
      count += alphaTable[alpha];
    }
    return count;
  });
}
