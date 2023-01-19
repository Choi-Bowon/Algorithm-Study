def solution(lottos, win_nums):
    answer = []
    # 로또 번호 6개
    # 0개, 1개는 순위 6
    rank=[6,6,5,4,3,2,1]
    
    z=lottos.count(0)
    cnt=0
    
    for i in win_nums:
        if i in lottos:
            cnt+=1
    answer=[rank[cnt+z], rank[cnt]]
    
    return answer