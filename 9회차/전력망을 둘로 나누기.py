from collections import deque
def bfs(graph, start_node):
    visit = []
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def solution(n, wires):
    answer = n - 2
    for i in range(len(wires)):
        temp = wires.copy()
        graph = [[] for i in range(n + 1)]
        temp.pop(i)
        for wire in temp:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx, wir in enumerate(graph):
            if wir != []:
                start = idx
                break
        net = abs(2*len(bfs(graph, start)) - n)
        if net < answer:
            answer = net
    return answer
