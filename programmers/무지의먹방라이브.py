import heapq
import copy

def solution(food_times, k):
    answer = -1
    
    # 핵심은 먹을 음식이 적은 음식 순서대로 가져와 k값을 조절해준다
    # 우선순위 큐에 (음식 시간, 해당 인덱스)를 페어로 저장
    # minheap으로 구현하여 가장 작은 수가 먼저 나오도록 한다.
    # 가장 작은 음식 시간이 나오면 그 음식이 사라지는데 걸리는 시간은 N * food_times[i]이다.
    # 그리고 k에서 n * food_times[i]를 빼준다.
    # 이 과정을 반복하면서 k가 0이하일때를 찾아 인덱스를 반환해 준다. 
    # q에 아무것도 없는데 k가 남으면 먹을 음식이 없기 때문에 -1을 출력
    
    
    pq = []
    
    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i+1))
        
    prev_time = 0
        
    while pq:
        length = len(pq)
        time, index = heapq.heappop(pq)
        
        if (time - prev_time) * length > k:
            heapq.heappush(pq, (time, index))
            break
        
        k -= (time - prev_time) * length
        prev_time = time
    
    result = []
    
    while pq:
        time, idx = heapq.heappop(pq)
        result.append((idx, time))
        
    result.sort()
    
    if len(result) != 0:
        answer = result[k][0]
    
    return answer