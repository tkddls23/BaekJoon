function solution(plans) {
  debugger;
  const timeToNum = time => {
    const [hour, minute] = time.split(':').map(Number);
    return 60 * hour + minute;
  };

  const answer = [];
  const planTable = {};

  plans.forEach(plan => {
    const [name, start, playtime] = plan;
    planTable[timeToNum(start)] = {
      name,
      playtime: +playtime,
    };
  });

  let currPlan;
  const stopPlans = [];
  for (let i = 0; i <= timeToNum('25:40') * 100; i++) {
    if (currPlan && planTable[i]) {
      currPlan.playtime -= 1;
      if (currPlan.playtime === 0) {
        answer.push(currPlan.name);
      } else {
        stopPlans.push(currPlan);
      }
      currPlan = planTable[i];
    } else if (planTable[i]) {
      currPlan = planTable[i];
    } else if (currPlan) {
      currPlan.playtime -= 1;
      if (currPlan.playtime === 0) {
        answer.push(currPlan.name);
        currPlan = stopPlans.pop();
      }
    }
  }

  return answer;
}
