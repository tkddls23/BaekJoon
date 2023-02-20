function solution(s) {
  const popTop = stack => {
    if (stack.length < 3) return false;
    if ('110' === stack.slice(stack.length - 3, stack.length).join('')) {
      stack.pop();
      stack.pop();
      stack.pop();
      return true;
    }
    return false;
  };

  return s.map(str => {
    const strArr = [...str].reverse();
    let count = 0;
    const stack = [];
    while (strArr.length) {
      const next = strArr.pop();
      stack.push(next);
      if (next === '1') continue;
      if (popTop(stack)) count++;
    }
    const total = '110'.repeat(count);
    str = stack.join('');
    const index = str.lastIndexOf('0');
    if (index !== -1) {
      return str.substring(0, index + 1) + total + str.substring(index + 1);
    }
    return total + str;
  });
}

console.log(solution(['1110', '100111100', '0111111010']));
console.log(solution(['1100111011101001']));
