function solution(lottos, win_nums) {
  const winLottos = Array(45).fill(false);
  const myLottos = Array(45).fill(false);
  const lottosTable = [6, 6, 5, 4, 3, 2, 1];

  win_nums.forEach(n => {
    winLottos[n - 1] = true;
  });

  let lostLottos = 0;
  lottos.forEach(n => {
    if (n === 0) lostLottos++;
    else myLottos[n - 1] = true;
  });

  let minResult = 0;
  for (let i = 0; i < 45; i++) {
    if (winLottos[i] && myLottos[i]) minResult++;
  }

  return [lottosTable[minResult + lostLottos], lottosTable[minResult]];
}
