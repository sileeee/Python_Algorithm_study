def solution(id_list, report, k):
    dict_report = {name: [] for name in id_list}
    dict_count = {name: 0 for name in id_list}
    stop = []
    result = []

    for i in report:
        user, get_report_user = i.split()
        if get_report_user not in dict_report[user]:
            dict_report[user].append(get_report_user)

    for i in id_list:
        for j in dict_report:
            if i in dict_report[j]:
                dict_count[i] += 1
        if dict_count[i] >= k:
            stop.append(i)

    for i in dict_report:
        count = 0
        for j in dict_report[i]:
            if j in stop:
                count += 1
        result.append(count)

    return result
