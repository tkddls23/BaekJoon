function solution(book_time) {
  const convertTimeToInt = time => {
    const [h, m] = time.split(':');
    return parseInt(h) * 60 + parseInt(m);
  };

  const timeTable = Array(convertTimeToInt('24:10')).fill(0);

  for (const [start, end] of book_time) {
    timeTable[convertTimeToInt(start)]++;
    timeTable[convertTimeToInt(end) + 10]--;
  }

  let minRoom = -Infinity;
  for (let i = 0; i < timeTable.length - 1; i++) {
    timeTable[i + 1] += timeTable[i];
    minRoom = Math.max(minRoom, timeTable[i]);
  }

  return minRoom;
}
