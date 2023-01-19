def solution(n):
    answer = ''
    # 3진법
    num_dict={
        1:'1',
        2:'2',
        0:'4'
    }
    # number_list=['4','1','2']
    # number_list[3%3]
    while n !=0:
        나머지 = n%3
        answer=num_dict[나머지]+answer
        if n%3==0:
            n=n//3-1
        else:
            n=n//3
    
    return answer