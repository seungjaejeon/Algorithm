def solution(bandage, health, attacks):
    answer = 0
    cur_heal = health
    def heal(before_time, sec, heal):
        non_attack_time = sec - before_time
        if non_attack_time < bandage[0]:
            heal += non_attack_time * bandage[1]
        else:
            heal += non_attack_time * bandage[1] + (non_attack_time // bandage[0]) * bandage[2]
        if heal > health:
            return health
        else:
            return heal
    
    before_time = 0
    for i, val in enumerate(attacks):
        cur_sec, damage = val[0]-1, val[1]
        if cur_heal < health:
            cur_heal = heal(before_time, cur_sec, cur_heal)
        cur_heal -= damage
        before_time = cur_sec+1
        if cur_heal <= 0:
            cur_heal = -1
            break
    return cur_heal