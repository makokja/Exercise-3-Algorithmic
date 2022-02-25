def solve(num):
   result = ""
   table = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I"),
   ]
   for cap, roman in table:
      d, m = divmod(num, cap)
      result += roman * d
      num = m

   return result

num = int(input("Enter Number: ")) 
print(solve(num))