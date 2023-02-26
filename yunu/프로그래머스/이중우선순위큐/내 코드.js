function solution(operations) {
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

  const pq = new Heap();

  for (const operation of operations) {
    const [o, n] = operation.split(' ');
    if (o === 'I') {
      const num = parseInt(n);
      pq.push(num);
    } else {
      if (pq.isEmpty()) continue;
      if (n === '-1') {
        const sorted = [];
        while (!pq.isEmpty()) {
          sorted.push(pq.pop());
        }
        sorted.pop();
        while (sorted.length) {
          pq.push(sorted.pop());
        }
      } else pq.pop();
    }
  }

  if (pq.isEmpty()) return [0, 0];
  const sorted = [];
  while (!pq.isEmpty()) {
    sorted.push(pq.pop());
  }
  return [sorted[0], sorted[sorted.length - 1]];
}
