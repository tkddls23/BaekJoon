function solution(n, lost, reserve) {
  const students = Array(n + 2).fill(1);
  [students[0], students[n + 1]] = [0, 0];

  lost.forEach(l => {
    students[l]--;
  });

  reserve.forEach(r => {
    students[r]++;
  });

  let answer = 0;
  for (let i = 1; i < students.length - 1; i++) {
    if (students[i] >= 1) answer++;
    else if (students[i] === 0) {
      if (students[i - 1] >= 2) {
        students[i] = 1;
        students[i - 1]--;
        answer++;
      } else if (students[i + 1] >= 2) {
        students[i] = 1;
        students[i + 1]--;
        answer++;
      }
    }
  }

  return answer;
}
