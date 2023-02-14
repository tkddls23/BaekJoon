function solution(a) {
  if (a.length < 2) return 0;

  const cache = {};
  a.forEach((el, idx) => {
    if (!cache[el]) {
      if (idx > 0) cache[el] = [idx, 2];
      else cache[el] = [idx, 1];
    } else {
      const [i, length] = cache[el];
      if (length % 2) {
        const increase = idx === i + 1 ? 0 : Math.min(3, idx - i);
        cache[el] = [idx, length + increase];
      } else {
        const increase = Math.min(2, idx - i);
        cache[el] = [idx, length + increase];
      }
    }
  });

  let maxLength = 0;
  Object.keys(cache).forEach(key => {
    const [i, length] = cache[key];
    if (length % 2) {
      if (i === a.length - 1) maxLength = Math.max(maxLength, length - 1);
      else maxLength = Math.max(maxLength, length + 1);
    } else {
      maxLength = Math.max(maxLength, length);
    }
  });

  return maxLength;
}

/*
// 런타임 에러 나는 코드
function solution(a) {
  if (a.length < 2) return 0;

  const cache = {};

  a.forEach((el, idx) => {
    if (!cache[el]) {
      if (idx > 0) cache[el] = [idx, 2];
      else cache[el] = [idx, 1];
    } else {
      const [i, length] = cache[el];
      if (length % 2) {
        if (idx > i + 2) {
          cache[el] = [idx, length + 3];
        } else if (idx > i + 1) {
          cache[el] = [idx, length + 2];
        } else {
          cache[el] = [idx, length];
        }
      } else {
        if (idx > i + 1) {
          cache[el] = [idx, length + 2];
        } else {
          cache[el] = [idx, length + 1];
        }
      }
    }
  });

  Object.keys(cache).forEach(key => {
    const [i, length] = cache[key];
    if (length % 2) {
      if (i === a.length - 1) cache[key] = length - 1;
      else cache[key] = length + 1;
    } else {
      cache[key] = length;
    }
  });

  return Math.max(...Object.values(cache));
}
*/

// console.log(solution([0]));
console.log(solution([5, 2, 3, 3, 5, 3]));
console.log(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]));
