# 프로그래머스
# 뉴스 클러스터링
import sys

def change(str):
    arr = []
    for i in range(len(str)-1):
        if 'a' <= str[i] <= 'z' or 'A' <= str[i] <= 'Z':
            if 'a' <= str[i+1] <= 'z' or 'A' <= str[i+1] <= 'Z':
                arr.append(str[i].lower()+str[i+1].lower())
            else:
                i += 2
        else:
            i += 1
    return arr

def solution(str1, str2):
    answer = 0
    result = 0
    
    tmp = str1
    tmp2 = str2
    
    list1 = []
    list2 = []
    
    list1 = change(str1)
    list2 = change(str2)
    
    inter = []
    
    print(list1)
    print(list2)
    
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and list1[i] != '' and list2[j] != '':
                inter.append(list2[j])
                list1[i] = ''
                list2[j] = ''
                
    print(inter)
    
    union_size = len(list1) + len(list2) - len(inter)
    inter_size = len(inter)
    
    if union_size == 0 and inter_size == 0:
        result = 1
    else:
        result = inter_size / union_size
    
    answer = int(result * 65536)
        
    return answer