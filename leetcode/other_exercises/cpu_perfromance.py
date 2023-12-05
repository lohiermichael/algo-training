from typing import *


def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    logs = [log.split(':') for log in logs]
    res = [0] * n
    running = []
    t = 0
    while logs:
        f_id, state, log_t = logs[0]
        if int(log_t) == t:
            if state == "start":
                running.append(f_id)
            else:
                running.pop()
            res[int(f_id)] += 1
            logs.pop(0)
        else:
            res[int(running[-1])] += 1
        t += 1
    return res


if __name__ == '__main__':
    logs_test = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    n_test = 2
    print(exclusiveTime(n_test, logs_test))
