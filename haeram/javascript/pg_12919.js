function solution(seoul) {
    let answer = "";

    seoul.forEach((name, idx) => {
        if (name === "Kim") {
            answer = `김서방은 ${idx}에 있다`;
        }
    });

    return answer;
}
