function solution(numbers) {
  const toBinary = num => num.toString(2);

  const getTreeInfo = tree => {
    if (tree.length === 1) return { isTree: true, root: tree };
    const rootIndex = (tree.length - 1) / 2;
    const root = tree[rootIndex];
    const leftTreeInfo = getTreeInfo(tree.substr(0, rootIndex));
    const rightTreeInfo = getTreeInfo(tree.substr(rootIndex + 1));
    if (!leftTreeInfo.isTree || !rightTreeInfo.isTree)
      return { isTree: false, root };
    if (root === '0') {
      if (leftTreeInfo.root === '1' || rightTreeInfo.root === '1')
        return { isTree: false, root };
    }
    return { isTree: true, root };
  };

  return numbers.map(num => {
    const binary = toBinary(num).split('').reverse().join('');
    let rootIndex = 1;
    let childLength = rootIndex;
    let leftTreeInfo = getTreeInfo(binary.substr(0, childLength));
    let rightTreeInfo;
    while (rootIndex < binary.length) {
      rightTreeInfo = getTreeInfo(
        binary.substr(rootIndex + 1, childLength).padEnd(childLength, '0')
      );
      if (!rightTreeInfo.isTree) return 0;
      const root = binary[rootIndex];
      if (root === '0') {
        if (leftTreeInfo.root === '1' || rightTreeInfo.root === '1') return 0;
      }
      leftTreeInfo = { isTree: true, root };
      rootIndex = 2 * childLength + 1;
      childLength = rootIndex;
    }
    return 1;
  });
}

console.log(solution([7, 42, 5]));
console.log(solution([63, 111, 95]));
