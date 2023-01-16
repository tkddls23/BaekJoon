function solution(cap, n, deliveries, pickups) {
  const deliveryHouses = deliveries.reduce((prev, curr, index) => {
    for (let i = 0; i < curr; i++) prev.push(index + 1);
    return prev;
  }, []);
  const pickupHouses = pickups.reduce((prev, curr, index) => {
    for (let i = 0; i < curr; i++) prev.push(index + 1);
    return prev;
  }, []);

  let answer = 0;
  let deliveryLength = deliveryHouses.length - 1;
  let pickupLength = pickupHouses.length - 1;
  while (deliveryLength >= 0 || pickupLength >= 0) {
    const delivery = deliveryLength < 0 ? 0 : deliveryHouses[deliveryLength];
    const pickup = pickupLength < 0 ? 0 : pickupHouses[pickupLength];
    answer += Math.max(delivery, pickup) * 2;
    deliveryLength -= cap;
    pickupLength -= cap;
  }
  return answer;
}

console.log(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]));
console.log(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]));
