def solution(id_list, report, k):
    answer = []
    answer_dic = {}
    report_dic = {}
    bad_player = []
    report_list = [i.split(' ') for i in report] #2차원배열
    for i in id_list:
        report_dic[i] = []
        answer_dic[i] = 0
    for i in range(len(report)):
        if report_list[i][1] in report_dic:
            if report_list[i][0] not in report_dic[report_list[i][1]]:
                report_dic[report_list[i][1]]+=[report_list[i][0]]
        else:
            report_dic[report_list[i][1]]=[report_list[i][0]]
    for i in id_list:
        if len(report_dic[i])>=k:
            bad_player.append(i)
    for i in bad_player:
        for j in report_dic[i]:
            answer_dic[j] += 1
    for i in id_list:
        answer.append(answer_dic[i])
    return answer