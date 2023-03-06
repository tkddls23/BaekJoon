function solution(sequence) {
  const n = sequence.length;

  let pulseSeq = sequence.map((el, i) => el * (i % 2 === 0 ? 1 : -1));
  let reverseSeq = sequence.map((el, i) => el * (i % 2 === 0 ? -1 : 1));

  let maxSum = Math.max(pulseSeq[0], reverseSeq[0]);
  const pulseDp = [pulseSeq[0]];
  const reverseDp = [reverseSeq[0]];
  for (let i = 1; i < n; i++) {
    const currPulse = Math.max(pulseDp[i - 1] + pulseSeq[i], pulseSeq[i]);
    const currReverse = Math.max(
      reverseDp[i - 1] + reverseSeq[i],
      reverseSeq[i]
    );
    pulseDp.push(currPulse);
    reverseDp.push(currReverse);
    maxSum = Math.max(maxSum, currPulse, currReverse);
  }

  return maxSum;
}
