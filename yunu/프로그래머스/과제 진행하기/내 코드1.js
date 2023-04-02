function solution(plans) {
  const timeToNum = time => {
    const [hour, minute] = time.split(':').map(Number);
    return 60 * hour + minute;
  };

  const answer = [];

  plans = plans
    .map(([name, start, playtime]) => [name, timeToNum(start), +playtime])
    .sort((a, b) => a[1] - b[1]);

  let currPlan = null;
  const stopPlans = [];
  for (const nextPlan of plans) {
    if (currPlan === null) {
      currPlan = nextPlan;
      continue;
    }
    let timeDiff = nextPlan[1] - currPlan[1];
    if (timeDiff >= currPlan[2]) {
      answer.push(currPlan[0]);
      timeDiff -= currPlan[2];
      while (stopPlans.length) {
        const lastPlan = stopPlans.pop();
        if (timeDiff >= lastPlan[1]) {
          answer.push(lastPlan[0]);
          timeDiff -= lastPlan[1];
        } else {
          stopPlans.push(lastPlan);
          break;
        }
      }
    } else {
      stopPlans.push([currPlan[0], currPlan[2] - timeDiff]);
    }
    currPlan = nextPlan;
  }

  const stack = [];
  for (const plan of plans) {
    if (stack.length) {
      const [name, start, playtime] = stack.pop();
      const diffTime = plan[1] - start;
    }
    stack.push(plan);
  }

  return [...answer, currPlan[0], ...stopPlans.map(el => el[0]).reverse()];
}
