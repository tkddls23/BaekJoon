function solution(n) {
    let answer = 0;

    const nToBinary = n.toString(2);
    const nCountOne = countOnes(nToBinary);

    for (let i = n + 1; i <= 1000000; i++) {
        const cand = i.toString(2);

        if (countOnes(cand) === nCountOne) {
            answer = i;
            break;
        }
    }

    return answer;
}

function countOnes(bin) {
    let cnt = 0;

    for (const it of bin) {
        if (Number(it) === 1) {
            cnt++;
        }
    }

    return cnt;
}
