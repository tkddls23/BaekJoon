function solution(m, n, startX, startY, balls) {
  const distance = (x1, y1, x2, y2) => (x1 - x2) ** 2 + (y1 - y2) ** 2;

  return balls.map(([ballX, ballY]) => {
    const cases = [
      [-ballX, ballY],
      [ballX, -ballY],
      [m + (m - ballX), ballY],
      [ballX, n + (n - ballY)],
    ].filter(
      ([x, y]) =>
        (startX - ballX) / (startY - ballY) !== (startX - x) / (startY - y) ||
        distance(startX, startY, x, y) < distance(ballX, ballY, x, y)
    );
    return Math.min(
      ...cases.map(([foldX, foldY]) => distance(startX, startY, foldX, foldY))
    );
  });
}
