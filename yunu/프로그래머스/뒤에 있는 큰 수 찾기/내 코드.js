function solution(numbers) {
  const stack = [];
  return numbers
    .reverse()
    .map(number => {
      while (true) {
        if (!stack.length) {
          stack.push(number);
          return -1;
        }
        if (number < stack[stack.length - 1]) {
          stack.push(number);
          return stack[stack.length - 2];
        } else {
          stack.pop();
        }
      }
    })
    .reverse();
}
