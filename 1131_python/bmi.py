def computeBMI(kg, M):
    if kg>200 and M>2.5: #錯誤，範圍判斷錯誤
        return -1
    if kg<=2 or M<=0.05:
        return -1
    BMI = round(kg/(M*M),2) #錯誤，四捨五入取兩位小數
    #BMI = ((100*kg/(M*M))//1)/100 #正確，去尾，乘100取整數，再除100取兩位小數
    return BMI