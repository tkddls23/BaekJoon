function solution(today, terms, privacies) {
    const LAST_DAY = 28;

    const convertDateToArr = (date) => {
        return date.split(".").map((value) => parseInt(value));
    };

    const [tYear, tMonth, tDay] = convertDateToArr(today);

    const termTable = terms.reduce((table, term) => {
        const [type, month] = term.split(" ");
        table[type] = parseInt(month);
        return table;
    }, {});

    const isValidPrivacy = (date, type) => {
        let [year, month, day] = date;
        month += termTable[type];
        day -= 1;
        if (day === 0) {
            month--;
            day = LAST_DAY;
        }
        year += parseInt((month - 1) / 12);
        month = month % 12 === 0 ? 12 : month % 12;
        if (tYear > year) return false;
        if (tYear === year && tMonth > month) return false;
        if (tYear === year && tMonth === month && tDay > day) return false;
        return true;
    };

    return privacies.reduce((prev, privacy, index) => {
        const [date, type] = privacy.split(" ");
        if (!isValidPrivacy(convertDateToArr(date), type)) prev.push(index + 1);
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
