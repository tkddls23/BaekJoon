function solution(n, words) {
    let answer = [];

    const wordHistory = new Set([words[0]]);

    let turn = 1;
    while (1) {
        for (let person = 0; person < n; person++) {
            if (!checkValid(wordHistory, words[turn - 1], words[turn])) {
                answer.push(((person + 1) % n) + 1);
                answer.push(parseInt(turn / n) + 1);

                return answer;
            }

            wordHistory.add(words[turn]);
            turn++;

            if (turn >= words.length) {
                return [0, 0];
            }
        }
    }

    return [0, 0];
}

function checkValid(history, prevWord, curWord) {
    if (curWord.length <= 1) {
        return false;
    }

    if (prevWord.slice(-1) !== curWord[0]) {
        return false;
    }

    if (history.has(curWord)) {
        return false;
    }

    return true;
}
