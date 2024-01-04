def solution(array, commands):
    answer = []
    for arr in commands:
        array_slice = []
        for i in range(arr[0]-1, arr[1]):
            array_slice.append(array[i]) 
        array_slice.sort()
        answer.append(array_slice[arr[2]-1])
        
    return answer