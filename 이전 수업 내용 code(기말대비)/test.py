def input_number(): 
    number = int(input("입력할 자료 개수(반복 횟수) 입력: "))
    while number > 2: 
        if(number < 2): 
            print("반복 횟수는 2번 이상부터!")
            break
        else:
            return number 


def save_to_list(num, num_arr):
    for _ in range(num):
        num = int(input("숫자 입력 (종료:999): "))
        if(num == 999): 
            break
        num_arr.append(num)
        num_arr.sort()
        print("중간 정렬 결과", num_arr) #디버깅 
            


def evaluate_print(num_arr):
    # 999가 있다면 계산하지말고 종료 
    length = len(num_arr)
     
    #아이템 개수 
    item_num = len(num_arr) 
        #합계 
    sum_num = sum(num_arr)
        #평균 
    ex_num = sum_num / item_num
        #최대 
    i = item_num-1
        #최대 
    max_num = num_arr[i]
        #최소 
    min_num = num_arr[0]
    
    desc_arr = sorted(num_arr, reverse=True)
    
    print("최종 정렬 결과: ", num_arr)  
    print("내림차순 정렬: ", desc_arr)       
    
    print("item 개수: ", item_num)
    print("합계 : ", sum_num)
    print(f"평균: {ex_num:.2f}")

    print("최대: ", max_num) 
    print("최소: ", min_num)
    
####################################
num_arr = []
num = input_number()
save_to_list(num, num_arr)
evaluate_print(num_arr)