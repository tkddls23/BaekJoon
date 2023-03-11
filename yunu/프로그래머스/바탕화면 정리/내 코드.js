function solution(wallpaper) {
  const N = wallpaper.length;
  const M = wallpaper[0].length;

  const drag = [N, M, 0, 0];

  wallpaper.forEach((row, i) => {
    [...row].forEach((col, j) => {
      if (col === '#') {
        drag[0] = Math.min(drag[0], i);
        drag[1] = Math.min(drag[1], j);
        drag[2] = Math.max(drag[2], i + 1);
        drag[3] = Math.max(drag[3], j + 1);
      }
    });
  });

  return drag;
}
