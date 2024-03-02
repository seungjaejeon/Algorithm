from collections import deque
def solution(bridge_length, weight, truck_weights):
    lenght =deque([0 for _  in range(bridge_length)])
    truck_wait = deque(truck_weights)
    truck_done = []
    truck_going = deque([])
    while True:
        if truck_wait:
            if sum(truck_going)+truck_wait[0]-lenght[0]<=weight:
                num = truck_wait.popleft()
                truck_going.append(num)
                lenght.append(num)
                num = lenght.popleft()
                truck_done.append(num)
                if num != 0:
                    truck_going.popleft()
            else:
                num = lenght.popleft()
                if num != 0:
                    truck_going.popleft()
                truck_done.append(num)
                lenght.append(0)
        else: return len(truck_done) + bridge_length