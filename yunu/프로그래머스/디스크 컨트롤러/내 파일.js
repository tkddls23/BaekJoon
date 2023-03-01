class Heap {
  arr;
  constructor() {
    this.arr = [null];
  }
  push(data) {
    const { arr } = this;
    arr.push(data);
    let child = arr.length - 1,
      parent = Math.floor(child / 2);
    while (child !== 1 && arr[parent] < arr[child]) {
      [arr[child], arr[parent]] = [arr[parent], arr[child]];
      child = Math.floor(child / 2);
      parent = Math.floor(parent / 2);
    }
  }
  pop() {
    const { arr } = this;
    if (this.isEmpty()) return;
    [arr[1], arr[arr.length - 1]] = [arr[arr.length - 1], arr[1]];
    let root = arr.pop(),
      last = arr[1],
      parent = 1,
      child = 2;
    while (child <= arr.length - 1) {
      if (child < arr.length - 1 && arr[child] < arr[child + 1]) {
        child++;
      }
      if (last >= arr[child]) break;
      [arr[parent], arr[child]] = [arr[child], arr[parent]];
      parent = child;
      child *= 2;
    }
    return root;
  }
  isEmpty() {
    return this.arr.length === 1;
  }
}

function solution(jobs) {
  const jobMap = {};
  jobs.forEach(([time, length]) => {
    if (jobMap[time]) jobMap[time].push(length);
    else jobMap[time] = [length];
  });

  let currTime = 0;
  const heap = new Heap();
  Object.keys(jobMap)
    .sort((a, b) => a - b)
    .forEach(time => {
      while (currTime < time) currTime += heap.pop();
      jobMap[time].forEach(length => heap.push(length));
      currTime += heap.pop();
    });

  var answer = 0;
  return answer;
}
