def solution(progresses, speeds):
    answer = []
    
    day = 1
    temp = []

    while progresses:
        if progresses[0] + speeds[0] * day >= 100:
            temp.append(progresses[0])
            progresses.pop(0)
            speeds.pop(0)
        else:
            day += 1
            if len(temp) != 0:
                answer.append(len(temp))
                temp = []
    answer.append(len(temp))

    return answer
data = [93,30,55]
speeds = [1,30,5]
print(solution(data,speeds))