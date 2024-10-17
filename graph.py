graph = {
    'A':{'B':20,'C':15,'E':80},
    'B':{'A':40,'E':10,'F':15},
    'C':{'A':20,'B':4,'F':10},
    'D':{'A':36,'B':18,'C':15},
    'E':{'C':90,'D':15},
    'F':{'C':45,'D':4,'E':10}
}
def print_path_and_cost(start,goal,parent,g):
    path=[]
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print('duong di','->'.join(path)) # hiển thị đường đi
    print('C(p) = ',g[goal]) # hiển thị chi phí

def AT(graph, start, goals):
    MO = [start] # danh sách các dỉnh chờ đươc duyệt
    g = {start:0} # chi phis tới đỉnh
    DONG = [] # danh sach các điển đã xét xong
    parent = {} # lưu trữ cha của mỗi đỉnh

    while MO:
        # lấy đỉnh n có chi phí g(n) nhỏ nhất từ tập MO
        min_cost = float('inf')
        n = None
        for vertex in MO:
            if vertex in g:
                cost = g[vertex]
            else:
                cost = float('inf')
            if cost< min_cost:
                min_cost = cost
                n = vertex
        if n in goals:
            print_path_and_cost(start,n,parent,g)
            return True
        
        MO.remove(n) # xóa đỉnh n khỏi tập MO
        DONG.append(n) # them vertex n vào tập để xet

        for m in graph.get(n,{}): # duyệt các đỉnh kề của n
            cost = graph[n][m] # chi phí từ n đến m
            new_cost = g.get(n,float('inf')) +cost
            # nếu m để có cha và đường đi mới ngắn hơn
            if m in parent and new_cost < g[m]:
                 g[m] = new_cost
                 parent[m] = n
            # nếu m chưa được duyệt
            elif m not in MO and m not in DONG:
                g[m] = new_cost
                parent[m] = n
                MO.append(m)
    return False # không tìm thấy đường đi dến đỉnh đích

start = 'A'
goals = ['E','D']
print(AT(graph,start,goals))
