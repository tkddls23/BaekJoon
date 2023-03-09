function solution(commands) {
  const table = [];

  for (let r = 0; r < 51; r++) {
    table.push([]);
    for (let c = 0; c < 51; c++) {
      table[r].push({ value: undefined, num: 51 * r + c, isMerged: false });
    }
  }

  const updateByRC = (r, c, value) => {
    const num = table[r][c]['num'];
    for (let i = 1; i < 51; i++) {
      for (let j = 1; j < 51; j++) {
        if (table[i][j]['num'] === num) {
          table[i][j]['value'] = value;
        }
      }
    }
  };
  const updateByValue = (before, after) => {
    for (let i = 1; i < 51; i++) {
      for (let j = 1; j < 51; j++) {
        if (table[i][j]['value'] === before) {
          table[i][j]['value'] = after;
        }
      }
    }
  };
  const merge = (r1, c1, r2, c2) => {
    if (r1 === r2 && c1 === c2) return;
    if (table[r1][c1]['isMerged'] && table[r2][c2]['isMerged']) {
      const num1 = table[r1][c1]['num'];
      const num2 = table[r2][c2]['num'];
      const value1 = table[r1][c1]['value'];
      const value2 = table[r2][c2]['value'];
      for (let i = 1; i < 51; i++) {
        for (let j = 1; j < 51; j++) {
          if (table[i][j]['num'] === num1 || table[i][j]['num'] === num2) {
            table[i][j]['num'] = num1;
            table[i][j]['value'] = value1 || value2;
          }
        }
      }
    } else if (table[r1][c1]['isMerged']) {
      table[r2][c2]['num'] = table[r1][c1]['num'];
      const value1 = table[r1][c1]['value'];
      const value2 = table[r2][c2]['value'];
      for (let i = 1; i < 51; i++) {
        for (let j = 1; j < 51; j++) {
          if (table[i][j]['num'] === table[r1][c1]['num']) {
            table[i][j]['value'] = value1 || value2;
          }
        }
      }
    } else if (table[r2][c2]['isMerged']) {
      table[r1][c1]['num'] = table[r2][c2]['num'];
      const value1 = table[r1][c1]['value'];
      const value2 = table[r2][c2]['value'];
      for (let i = 1; i < 51; i++) {
        for (let j = 1; j < 51; j++) {
          if (table[i][j]['num'] === table[r2][c2]['num']) {
            table[i][j]['value'] = value1 || value2;
          }
        }
      }
    } else {
      table[r2][c2]['num'] = table[r1][c1]['num'];
      const value1 = table[r1][c1]['value'];
      const value2 = table[r2][c2]['value'];
      table[r1][c1]['value'] = value1 || value2;
      table[r2][c2]['value'] = value1 || value2;
    }
    table[r1][c1]['isMerged'] = true;
    table[r2][c2]['isMerged'] = true;
  };
  const unmerge = (r, c) => {
    if (!table[r][c]['isMerged']) return;
    const value = table[r][c]['value'];
    const num = table[r][c]['num'];
    for (let i = 1; i < 51; i++) {
      for (let j = 1; j < 51; j++) {
        if (table[i][j]['num'] === num) {
          table[i][j]['num'] = 51 * i + j;
          table[i][j]['value'] = undefined;
          table[i][j]['isMerged'] = false;
        }
      }
    }
    table[r][c]['value'] = value;
  };
  const print = (r, c) => {
    return table[r][c]['value'] || 'EMPTY';
  };

  const answer = [];
  commands.forEach(commandStr => {
    const commandArr = commandStr.split(' ');
    const command = commandArr[0];
    if (command === 'UPDATE') {
      if (commandArr.length === 4) {
        const [_, r, c, value] = commandArr;
        updateByRC(+r, +c, value);
      } else {
        const [_, value1, value2] = commandArr;
        updateByValue(value1, value2);
      }
    } else if (command === 'MERGE') {
      const [_, r1, c1, r2, c2] = commandArr;
      merge(+r1, +c1, +r2, +c2);
    } else if (command === 'UNMERGE') {
      const [_, r, c] = commandArr;
      unmerge(+r, +c);
    } else {
      const [_, r, c] = commandArr;
      answer.push(print(+r, +c));
    }
  });

  return answer;
}

console.log(
  solution([
    'UPDATE 1 1 menu',
    'UPDATE 1 2 category',
    'UPDATE 2 1 bibimbap',
    'UPDATE 2 2 korean',
    'UPDATE 2 3 rice',
    'UPDATE 3 1 ramyeon',
    'UPDATE 3 2 korean',
    'UPDATE 3 3 noodle',
    'UPDATE 3 4 instant',
    'UPDATE 4 1 pasta',
    'UPDATE 4 2 italian',
    'UPDATE 4 3 noodle',
    'MERGE 1 2 1 3',
    'MERGE 1 3 1 4',
    'UPDATE korean hansik',
    'UPDATE 1 3 group',
    'UNMERGE 1 4',
    'PRINT 1 3',
    'PRINT 1 4',
  ])
);

console.log(
  solution([
    'UPDATE 1 1 a',
    'UPDATE 1 2 b',
    'UPDATE 2 1 c',
    'UPDATE 2 2 d',
    'MERGE 1 1 1 2',
    'MERGE 2 2 2 1',
    'MERGE 2 1 1 1',
    'PRINT 1 1',
    'UNMERGE 2 2',
    'PRINT 1 1',
  ])
);
