# 파일 입력 및 출력 예제

# 파일 읽기
with open('LII-1.inp', 'r') as file:
    lines = file.readlines()
k=0
var2_2_name = ['5','6','7']
var2_3_name = ['2','3','4']
var2_3_values = ['2e-2, 2e-2, 2e-3, 2e-3, 2e-3, 2e-3','3e-2, 3e-2, 3e-3, 3e-3, 3e-3, 3e-3','4e-2, 4e-2, 4e-3, 4e-3, 4e-3, 4e-3']
var2_2_values = ['1e-1, 5e-2, 5e-3, 5e-3, 5e-3, 5e-3','1e-1, 6e-2, 6e-3, 6e-3, 6e-3, 6e-3','1e-1, 7e-2, 7e-3, 7e-3, 7e-3, 7e-3']
var4_values = ['-10000', '-9000', '-8000', '-7000']
while 1:
    
    if k==3:
        break
    # 변수 1 변경    
    var1_values = ['7800','7850','7900']
    for i in [28, 142, 150, 159, 167]:
        line1 = lines[i-1]
        line_parts = line1.split("=")
        line_parts[3] = var1_values[k]+", section=BOX\n"
        line1 = line_parts[0]+"="+line_parts[1]+"="+line_parts[2]+"="+line_parts[3]
        lines[i-1] = line1

    # 변수 3 변경
    var3_values = [' 21E+10, 81E+9\n', ' 21E+10, 81E+9\n', ' 21E+10, 81E+9\n']
    for i in [31, 145, 153, 162, 170]:
        lines[i-1] = var3_values[k]


# 이렇게 3경우
# 29, 151,168 라인 현재  3e-2, 3e-2, 3e-3, 3e-3, 3e-3, 3e-3 으로 되어있는데
    # 변수 2 변경
    for x in range(0,3):
        for j in range(0,3):
            for var2_2 in [143, 160]:
                line2_2 = var2_2_values[j]+"\n"
                lines[var2_2-1] = line2_2
                # 변수 4 변경 -10000 -9000 -8000 -7000
            for var2_3 in [29,151,168]:
                line2_3 = var2_3_values[x]+"\n"
                lines[var2_3-1] = line2_3
                for t in range(0,4):
                    line4 = lines[281].split(',')
                    line4[2] = var4_values[t]+'\n'
                    lines[281] = line4[0]+","+line4[1]+", "+line4[2]
                    # 새로운 파일 생성
                    with open(var1_values[k]+'_'+var4_values[t]+'_'+var2_2_name[j]+'_'+var2_3_name[x]+".inp", 'w') as file:
                        file.writelines(lines)
    k = k+1