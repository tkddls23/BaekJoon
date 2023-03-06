function solution(sequence) {
  const n = sequence.length;

  let pulse = Array.from({ length: n }, (_, i) => (i % 2 === 0 ? 1 : -1));
  let reverse = Array.from({ length: n }, (_, i) => (i % 2 === 0 ? -1 : 1));

  let pulseMax = sequence[0] * pulse[0];
  const pulseDp = [sequence[0] * pulse[0]];
  for (let i = 1; i < n; i++) {
    const prev = pulseDp[pulseDp.length - 1];
    const curr = sequence[i] * pulse[i];
    pulseDp.push(Math.max(prev + curr, curr));
    pulseMax = Math.max(pulseMax, Math.max(prev + curr, curr));
  }

  let reverseMax = sequence[0] * reverse[0];
  const reverseDp = [sequence[0] * reverse[0]];
  for (let i = 1; i < n; i++) {
    const prev = reverseDp[reverseDp.length - 1];
    const curr = sequence[i] * reverse[i];
    reverseDp.push(Math.max(prev + curr, curr));
    reverseMax = Math.max(reverseMax, Math.max(prev + curr, curr));
  }

  return Math.max(pulseMax, reverseMax);
}
