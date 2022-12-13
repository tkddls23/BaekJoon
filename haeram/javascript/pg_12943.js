function solution(num) {
    let answer = 0;

    let cnt = 0;
    let flag = false;

    if (num == 1) {
        return 0;
    }

    for (let i = 0; i < 500; i++) {
        cnt++;

        const now = pro(num);

        if (now == 1) {
            flag = true;
            break;
        }

        num = now;
    }

    if (flag) {
        answer = cnt;
    } else {
        answer = -1;
    }

    return answer;
}

function pro(num) {
    if (num % 2 == 0) {
        return num / 2;
    } else {
        return num * 3 + 1;
    }
}
