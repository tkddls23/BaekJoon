function checkTree(str) {
  let root = (str.length + 1) / 2 - 1;
  let left = str.substring(0, root),
    right = str.substring(root + 1);
  if (str[root] === '1') {
    return checkTree(left) && checkTree(right);
  } else {
    if (left.indexOf('1') == -1 && right.indexOf('1') == -1) return true;
    else return false;
  }
}

function makeTree(n) {
  const strN = n.toString(2);
  let treeHeight = 1;
  while (2 ** treeHeight - 1 < strN.length) {
    treeHeight++;
  }
  let paddStrN =
    new Array(2 ** treeHeight - 1 - strN.length).fill(0).join('') + strN;
  return checkTree(paddStrN) ? 1 : 0;
}

function solution(numbers) {
  return numbers.map(makeTree);
}
