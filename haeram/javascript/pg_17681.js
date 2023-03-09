function solution(n, arr1, arr2) {
    let answer = [];

    arr1ToBin = [];
    arr2ToBin = [];

    for (const bin of arr1) {
        arr1ToBin.push(bin.toString(2).padStart(n, 0));
    }

    for (const bin of arr2) {
        arr2ToBin.push(bin.toString(2).padStart(n, 0));
    }

    for (let i = 0; i < n; i++) {
        let line = "";

        for (let j = 0; j < n; j++) {
            if (
                Number(arr1ToBin[i][j]) === 1 ||
                Number(arr2ToBin[i][j]) === 1
            ) {
                line += "#";
                continue;
            }

            line += " ";
        }

        answer.push(line);
    }

    return answer;
}
