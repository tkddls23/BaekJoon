function solution(nums) {
  const primeArr = Array(3000).fill(true);
  for (let i = 2; i < 3000; i++) {
    if (!primeArr[i]) continue;
    for (let j = i * i; j < 3000; j += i) {
      primeArr[j] = false;
    }
  }

  const isPrime = num => {
    let i = 2;
    while (i * i <= num) {
      if (num % i++) continue;
      return false;
    }
    return true;
  };

  let answer = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (isPrime(nums[i] + nums[j] + nums[k])) answer++;
        // if (primeArr[nums[i] + nums[j] + nums[k]])
        //     answer++;
      }
    }
  }

  return answer;
}
