function solution(common) {
  const [f1, f2, e2, e1] = [common[0], common[1], common.at(-2), common.at(-1)];
  if (f1 + e1 === f2 + e2) {
    return common.at(-1) + (f2 - f1);
  }
  return common.at(-1) * (f2 / f1);
}
