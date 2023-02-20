function solution(s) {
  return s.map(str => {
    let left = '',
      count1 = 0,
      count110 = 0;
    for (const c of str) {
      if (c === '1') count1++;
      else if (count1 >= 2) {
        count1 -= 2;
        count110++;
      } else {
        left += count1 > 0 ? '10' : '0';
        count1 = 0;
      }
    }
    return left + '110'.repeat(count110) + '1'.repeat(count1);
  });
}

console.log(solution(['1110', '100111100', '0111111010']));
console.log(solution(['1100111011101001']));
