function solution(brown, yellow) {
    let answer = [];

    brown /= 2;

    for (let i = 1; i < brown / 2; i++) {
        if (checkValid(i, brown - i, yellow)) {
            answer.push(brown - i);
            answer.push(i + 2);
            break;
        }
    }

    return answer;
}

function checkValid(height, width, y) {
    if ((width - 2) * height === y) {
        return true;
    }

    return false;
}
