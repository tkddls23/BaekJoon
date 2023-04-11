function solution(queue1, queue2) {
  // const sum = (...num) => num.reduce((acc, cur) => acc + cur, 0); // 이렇게 하면 런타임 에러 발생
  const sum = nums => nums.reduce((acc, cur) => acc + cur, 0);
  const total1 = sum(queue1);
  const total2 = sum(queue2);
  if ((total1 + total2) % 2 !== 0) return -1;

  const targetSum = (total1 + total2) / 2;
  const queue = [...queue1, ...queue2, ...queue1];
  let start = 0;
  let end = queue1.length;
  let currSum = total1;
  let count = 0;
  while (start <= end) {
    if (currSum < targetSum) {
      if (end >= queue.length) break;
      currSum += queue[end++];
    } else if (currSum > targetSum) {
      if (start >= queue.length) break;
      currSum -= queue[start++];
    } else if (currSum === targetSum) {
      return count;
    }
    count++;
  }

  return -1;
}
