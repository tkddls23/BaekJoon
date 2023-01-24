class Table {
  count = 0;
  _table = new Array(50)
    .fill(0)
    .map(() => new Array(50).fill(0).map(() => ({})));
  getCell(r, c) {
    return this._table[r - 1][c - 1];
  }
  setCell(r, c, value) {
    this._table[r - 1][c - 1] = value;
  }
  update(...params) {
    if (params[2] != null) {
      const [r, c, value] = params;
      const cell = this.getCell(r, c);
      cell.value = value;
    } else {
      const [value1, value2] = params;
      this._table.forEach(row => {
        row.forEach(cell => {
          if (cell && cell.value === value1) cell.value = value2;
        });
      });
    }
  }

  replaceCell(cell1, cell2) {
    this._table = this._table.map(row =>
      row.map(cell => (cell === cell1 ? cell2 : cell))
    );
  }

  merge(r1, c1, r2, c2) {
    const cell1 = this.getCell(r1, c1);
    const cell2 = this.getCell(r2, c2);
    if (cell1.value == null) {
      this.replaceCell(cell1, cell2);
    } else {
      this.replaceCell(cell2, cell1);
    }
  }

  unmerge(r, c) {
    const cell = this.getCell(r, c);
    this._table = this._table.map(row => {
      return row.map(c => (c == cell ? {} : c));
    });
    this.setCell(r, c, cell);
  }

  print(r, c) {
    return this.getCell(r, c).value || 'EMPTY';
  }
}

function solution(commands) {
  const table = new Table();
  const answer = [];
  commands.forEach(line => {
    const [command, ...params] = line.split(' ');
    const result = table[command.toLowerCase()](...params);
    if (result) answer.push(result);
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
