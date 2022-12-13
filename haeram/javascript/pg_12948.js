function solution(phone_number) {
    let answer = "";

    const len = phone_number.length;

    for (let i = 0; i < len - 4; i++) {
        answer += "*";
    }

    answer += phone_number.substr(len - 4, 4);

    return answer;
}
