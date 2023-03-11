class MinHeap {
  constructor() {
    this._data = [];
  }

  _upheap(index) {
    if (index === 0) {
      return;
    }
    const parent = Math.floor((index - 1) / 2);
    if (this._data[index][0] < this._data[parent][0]) {
      [this._data[index], this._data[parent]] = [
        this._data[parent],
        this._data[index],
      ];
      this._upheap(parent);
    }
  }

  _downheap(index) {
    const left = 2 * index + 1;
    if (left < this._data.length) {
      let selected = left;
      const right = 2 * index + 2;
      if (
        right < this._data.length &&
        this._data[selected][0] > this._data[right][0]
      ) {
        selected = right;
      }
      if (this._data[selected][0] < this._data[index][0]) {
        [this._data[selected], this._data[index]] = [
          this._data[index],
          this._data[selected],
        ];
        this._downheap(selected);
      }
    }
  }

  isEmpty() {
    return this._data.length === 0;
  }

  peek() {
    return [this._data[0][0], this._data[0][1]];
  }

  add(key, value) {
    this._data.push([key, value]);
    this._upheap(this._data.length - 1);
  }

  remove() {
    [this._data[0], this._data[this._data.length - 1]] = [
      this._data[this._data.length - 1],
      this._data[0],
    ];
    this._data.pop();
    this._downheap(0);
  }
}

function solution(numbers) {
  const size = numbers.length;
  const answer = new Array(size).fill(-1);
  const unSolved = new MinHeap();
  for (let index = 0; index < size; index++) {
    const number = numbers[index];
    while (!unSolved.isEmpty()) {
      const [comp, index] = unSolved.peek();
      if (comp < number) {
        answer[index] = number;
        unSolved.remove();
      } else {
        break;
      }
    }
    unSolved.add(number, index);
  }
  return answer;
}

console.log(solution([2, 3, 3, 5]));
console.log(solution([9, 1, 5, 3, 6, 2]));

/*
function solution(numbers) {
  const stack = [];
  return numbers.reduce((prev, curr, i) => {
    while (stack && numbers[stack[stack.length - 1]] < curr) {
      prev[stack.pop()] = curr;
    }
    stack.push(i);
    return prev;
  }, Array(numbers.length).fill(-1));
}
*/
