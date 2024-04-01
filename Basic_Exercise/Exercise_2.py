previous_num = 0


for i in range(0,10):
    current_sum = previous_num + i
    
    print(f"Current num {i}, previous num{previous_num} sum:{current_sum}")
    
    previous_num = i
    