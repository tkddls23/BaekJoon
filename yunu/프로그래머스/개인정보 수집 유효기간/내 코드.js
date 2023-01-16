function solution(today, terms, privacies) {
    const MONTH = 28;

    const convertDateToNum = (date) => {
        const [year, month, day] = date
            .split(".")
            .map((value) => parseInt(value));
        return year * 12 * 28 + month * 28 + day;
    };

    const todayNum = convertDateToNum(today);

    const termTable = terms.reduce((table, term) => {
        const [type, month] = term.split(" ");
        table[type] = parseInt(month);
        return table;
    }, {});

    const isValidPrivacy = (date, type) => {
        let dateNum = convertDateToNum(date);
        dateNum += termTable[type] * MONTH;
        return todayNum <= dateNum - 1;
    };

    return privacies.reduce((prev, privacy, index) => {
        const [date, type] = privacy.split(" ");
        if (!isValidPrivacy(date, type)) prev.push(index + 1);
        return prev;
    }, []);
}

console.log(
    solution(
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    )
);
console.log(
    solution(
        "2020.01.01",
        ["Z 3", "D 5"],
        [
            "2019.01.01 D",
            "2019.11.15 Z",
            "2019.08.02 D",
            "2019.07.01 D",
            "2018.12.28 Z",
        ]
    )
);
