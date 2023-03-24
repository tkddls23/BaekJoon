function solution(sizes) {
  const row = [];
  const col = [];
  sizes.forEach(size => {
    if (size[0] > size[1]) {
      row.push(size[0]);
      col.push(size[1]);
    } else {
      row.push(size[1]);
      col.push(size[0]);
    }
  });

  return Math.max(...row) * Math.max(...col);
}
