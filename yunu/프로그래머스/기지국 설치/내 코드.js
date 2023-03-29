function solution(n, stations, w) {
  stations.push(n + w + 1);

  const apartLength = [];
  let curr = 0;
  stations.forEach(s => {
    if (s - w - curr - 1 > 0) {
      apartLength.push(s - w - curr - 1);
    }
    curr = s + w;
  });

  const getMinStations = length => {
    return Math.ceil(length / (2 * w + 1));
  };

  return apartLength.reduce((acc, length) => acc + getMinStations(length), 0);
}
