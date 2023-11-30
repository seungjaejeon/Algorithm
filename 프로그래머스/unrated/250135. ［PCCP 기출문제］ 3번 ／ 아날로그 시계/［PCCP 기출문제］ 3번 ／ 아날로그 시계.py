def replace_sec(h, m, s):
    re = h*3600 + m*60 + s
    return re
def replace_angle(sec):
    h = int(sec/3600)
    m = int((sec%3600)/60)
    s = (sec%3600)%60
    sec_angle = s*6 % 360
    min_angle = ((m*6) + (s/10)) % 360
    hour_angle = ((h*30) + (m/2) + (s/120)) % 360
    return (hour_angle, min_angle, sec_angle)

def solution(h1, m1, s1, h2, m2, s2):
    answer = -1
    count = 0
    past_h, past_m, past_s = 0,0,0
    for i in range(replace_sec(h1, m1, s1), replace_sec(h2, m2, s2)+1):
            h, m, s = replace_angle(i)
            if i == 0:
                count += 1
                continue
            if i == 3600 * 12:
                count += 1
            else:
                if past_s < past_h and s >= h:
                    count += 1
                elif past_s < past_h and s == 0:
                    count += 1
                elif s == h:
                    count += 1
                if past_s < past_m and s >= m:
                    count += 1
                elif past_s < past_m and s == 0:
                    count += 1
            
            # 시침과 분침 초침이 모두 겹치는 경우 
            # 11시 59분 59초에서 12시 0분 0초로 넘어가는 경우 체크
            past_h = h
            past_m = m
            past_s = s

    return count

