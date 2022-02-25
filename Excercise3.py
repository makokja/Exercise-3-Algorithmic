def int_to_roman(x):
    #get the list of both numeric and roman
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M",]
    i = 12 #create varilble i for 12 index
    rom_num = ""
    while x != 0: #the process end when x reaches 0
        if numbers[i] <= x: #Find the largest number on the list that less than x
            rom_num += roman[i] # Add roman reps to the answer
            x = x - numbers[i] #subtract the number that already been used from x
        else:  # if the above condition is not true, just move down the list to previous value
            i -= 1
    return rom_num

x = int(input("Enter Number: ")) 
print(int_to_roman(x))