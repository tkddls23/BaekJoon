function solution(cap, n, deliveries, pickups) {
  let answer = 0;

  let deliveryCount = 0;
  let pickupCount = 0;
  let index = n - 1;

  for (let i = n - 1; i >= 0; i--) {
    deliveryCount += deliveries[i];
    pickupCount += pickups[i];

    while (deliveryCount > cap || pickupCount > cap) {
      deliveryCount -= cap;
      pickupCount -= cap;
      answer += 2 * (index + 1);
      index = i;
    }
  }
  if (deliveryCount > 0 || pickupCount > 0) {
    answer += 2 * (index + 1);
  }

  return answer;
}

console.log(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]));
console.log(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]));
