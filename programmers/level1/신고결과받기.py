def solution(id_list, report, k):
    answer = [0]*len(id_list)
    table = []
    for i in range(len(report)):
        table.append([])
    table2 = [0]*len(id_list)
    table3 = []

    s = set(report)
    for i in s:
        first, last = i.split()
        index = id_list.index(first)
        table[index].append(last)
        index2 = id_list.index(last)
        table2[index2] +=1
        if(table2[id_list.index(last)] == k):
            table3.append(last)
    for j in range(len(table)):
        if(table[j] == []):
            continue
        for w in table3:
            if w in table[j]:
                answer[j] +=1
    return answer
