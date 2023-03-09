function solution(cacheSize, cities) {
    let answer = 0;

    let cache = [];

    if (cacheSize === 0) {
        return 5 * cities.length;
    }

    for (const c of cities) {
        const city = c.toLowerCase();

        if (cache.includes(city)) {
            //cache hit
            cache = cache.filter((el) => el !== city);
            cache.push(city); //맨 뒤에 push

            answer++;
            continue;
        }

        //cache miss
        if (cache.length >= cacheSize) {
            cache.shift();
        }

        cache.push(city);
        answer += 5;
    }

    return answer;
}
