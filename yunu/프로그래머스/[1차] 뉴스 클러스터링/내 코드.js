function solution(str1, str2) {
  const getMultiSet = str => {
    const set = {};
    for (let i = 0; i < str.length - 1; i++) {
      const multi = (str[i] + str[i + 1]).toLowerCase();
      if (/[a-z]{2}/.test(multi)) {
        set[multi] = !set[multi] ? 1 : set[multi] + 1;
      }
    }
    return set;
  };

  const union = (multiSet1, multiSet2) => {
    const unionSet = { ...multiSet1 };
    Object.keys(multiSet2).forEach(key => {
      if (unionSet[key]) {
        unionSet[key] = Math.max(unionSet[key], multiSet2[key]);
      } else {
        unionSet[key] = multiSet2[key];
      }
    });
    return unionSet;
  };

  const intersection = (multiSet1, multiSet2) => {
    const interSet = { ...multiSet1 };
    Object.keys(interSet).forEach(key => {
      if (!multiSet2[key]) delete interSet[key];
    });
    Object.keys(multiSet2).forEach(key => {
      if (interSet[key]) {
        interSet[key] = Math.min(multiSet1[key], multiSet2[key]);
      } else {
        delete interSet[key];
      }
    });
    return interSet;
  };

  const getCount = multiSet => {
    let elCount = 0;
    for (const key in multiSet) {
      elCount += multiSet[key];
    }
    return elCount;
  };

  const multiSet1 = getMultiSet(str1);
  const multiSet2 = getMultiSet(str2);

  const inter = getCount(intersection(multiSet1, multiSet2));
  const uni = getCount(union(multiSet1, multiSet2));

  if (inter === 0 && uni === 0) return 65536;

  return Math.floor((65536 * inter) / uni);
}
