def main():
    cup_list = [1,0,0]
    swap_sequence = input()
    for i in swap_sequence:
        if(i == 'A'):
            temp = cup_list[0] 
            cup_list[0] = cup_list[1]
            cup_list[1] = temp
        elif(i == 'B'):
            temp = cup_list[1] 
            cup_list[1] = cup_list[2]
            cup_list[2] = temp
        else:
            temp = cup_list[0] 
            cup_list[0] = cup_list[2]
            cup_list[2] = temp
    print(cup_list.index(1) + 1)
    
  
if __name__== "__main__":
  main()
