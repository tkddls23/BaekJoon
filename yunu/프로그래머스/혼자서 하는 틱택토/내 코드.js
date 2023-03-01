function solution(board) {
  const victoryMask = [
    [
      [0, 0],
      [0, 1],
      [0, 2],
    ],
    [
      [1, 0],
      [1, 1],
      [1, 2],
    ],
    [
      [2, 0],
      [2, 1],
      [2, 2],
    ],
    [
      [0, 0],
      [1, 0],
      [2, 0],
    ],
    [
      [0, 1],
      [1, 1],
      [2, 1],
    ],
    [
      [0, 2],
      [1, 2],
      [2, 2],
    ],
    [
      [0, 0],
      [1, 1],
      [2, 2],
    ],
    [
      [0, 2],
      [1, 1],
      [2, 0],
    ],
  ];

  const countOX = board => {
    const strBoard = board.join('');
    const comma = 9 - strBoard.replaceAll('.', '').length;
    const O = strBoard.replaceAll('X', '').length - comma;
    const X = 9 - comma - O;
    return [O, X];
  };

  const [countO, countX] = countOX(board);

  if (!(countO === countX + 1 || countO === countX)) return 0;

  const boardArr = board.map(row => [...row]);

  let victoryO = 0;
  let victoryX = 0;

  for (const mask of victoryMask) {
    let victoryLine = '';
    for (const [y, x] of mask) {
      victoryLine += boardArr[y][x];
    }
    if (victoryLine === 'OOO') {
      victoryO++;
    }
    if (victoryLine === 'XXX') {
      victoryX++;
    }
  }

  if (victoryO >= 1 && victoryX >= 1) return 0;

  if (countO === countX && victoryX >= 1) return 1;

  if (countO > countX && victoryO >= 1) return 1;

  if (victoryO === 0 && victoryX === 0) return 1;

  return 0;
}
