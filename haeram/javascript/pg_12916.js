function solution(s) {
    let answer = true;

    const temp = s.toLowerCase();

    let pCnt = 0;
    let yCnt = 0;

    for (let i = 0; i < temp.length; i++) {
        if (temp[i] === "p") {
            pCnt += 1;
        }
        if (temp[i] === "y") {
            yCnt += 1;
        }
    }

    if (pCnt === yCnt) {
        answer = true;
    } else {
        answer = false;
    }

    return answer;
}
