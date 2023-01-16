function solution(users, emoticons) {
  const getDiscountPrice = (discount, price) => (price * (10 - discount)) / 10;

  const totalPrice = [];

  const setSum = (discount, price) => {
    return (sum, index) => {
      if (index + 1 > discount) return sum;
      return sum + getDiscountPrice(discount, price);
    };
  };

  const getTotalSum = (discountSum, i) => {
    if (i === emoticons.length) {
      totalPrice.push(discountSum);
      return;
    }
    getTotalSum(discountSum.map(setSum(1, emoticons[i])), i + 1);
    getTotalSum(discountSum.map(setSum(2, emoticons[i])), i + 1);
    getTotalSum(discountSum.map(setSum(3, emoticons[i])), i + 1);
    getTotalSum(discountSum.map(setSum(4, emoticons[i])), i + 1);
  };

  getTotalSum([0, 0, 0, 0], 0);

  let answer = [0, 0];
  totalPrice.forEach(prices => {
    const result = [0, 0];
    users.forEach(([want, maxPrice]) => {
      want = parseInt((want + 9) / 10);
      if (prices[want - 1] >= maxPrice) {
        result[0]++;
      } else {
        result[1] += prices[want - 1];
      }
    });
    if (answer[0] < result[0]) {
      answer = result;
    } else if (answer[0] === result[0] && answer[1] < result[1]) {
      answer = result;
    }
  });

  return answer;
}
