function solution(n, build_frame) {
  let frames = [];

  const isFrame = (x, y, a) => {
    return frames.some(([fx, fy, fa]) => fx === x && fy === y && fa === a);
  };

  const checkFrame = frames => {
    for (const [x, y, a] of frames) {
      if (a === 0) {
        if (
          y !== 0 &&
          !isFrame(x, y - 1, 0) &&
          !isFrame(x - 1, y, 1) &&
          !isFrame(x, y, 1)
        )
          return false;
      } else {
        if (
          !isFrame(x, y - 1, 0) &&
          !isFrame(x + 1, y - 1, 0) &&
          !(isFrame(x - 1, y, 1) && isFrame(x + 1, y, 1))
        )
          return false;
      }
    }
    return true;
  };

  build_frame.forEach(([x, y, a, b]) => {
    if (b) {
      frames.push([x, y, a]);
      if (!checkFrame(frames)) frames.pop();
    } else {
      frames = frames.filter(
        ([fx, fy, fa]) => fx !== x || fy !== y || fa !== a
      );
      if (!checkFrame(frames)) frames.push([x, y, a]);
    }
  });

  return frames.sort((a, b) =>
    a[0] === b[0] ? (a[1] === b[1] ? a[2] - b[2] : a[1] - b[1]) : a[0] - b[0]
  );
}

console.log(
  solution(5, [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 0, 1],
    [2, 2, 1, 1],
    [5, 0, 0, 1],
    [5, 1, 0, 1],
    [4, 2, 1, 1],
    [3, 2, 1, 1],
    [2, 1, 0, 0],
  ])
);

console.log(
  solution(5, [
    [0, 0, 0, 1],
    [2, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 1, 1, 1],
    [2, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 0, 1],
  ])
);
