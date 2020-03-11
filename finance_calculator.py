## 16 Jan 2020
## This program is an investment calculator and a home loan repayment calculator

import math
#A = P(1 + R/100)T
#Where,
#A is the amount of money accumulated after n years, including interest.
#P is the principal amount
#R is the rate and
#T is the time span

menu = """
Pick a calculation (1-2):
   1) Investment
   2) Bond
"""
calculation = int(input(menu))
if calculation == 1:

   menu = """
   Pick an option:
   3) Compound 
   4) Simple
   """
   option = int(input(menu))
   if option == 3:
   #compund
      def compound_interest(principle, rate, time):
      
         result = principle * (pow((1 + rate / 100), time))
         return result

      p = float(input("Enter the principal amount: "))
      r = float(input("Enter the interest rate: "))
      t = float(input("Enter the time in years: "))

      amount = compound_interest(p, r, t)
      interest = amount - p
      print("Compound amount is %.2f" % amount)
      print("Compound interest is %.2f" % interest)

   if option == 4:
   #simple

      def simple_interest(deposit, interest, duration):
      

         result = a*(1+b*c)
         return result

      a = float(input("Enter the principal amount: "))
      b = float(input("Enter the interest rate: "))
      c = float(input("Enter the time in years: "))

      final_amount = simple_interest(a, b, c)
      interest = final_amount - a
      print("Simple amount is %.2f" % final_amount)
      print("Simple interest is %.2f" % interest)

      calculation = int(input(menu))


if calculation == 2:

   def bond_repayment(rate, time):
   
      result = (i*(1 + i)**n) / ((1+i)**n -1)
      return result

   i = float(input("Enter the interest rate per month: "))
   n = float(input("Enter the time in years: "))

   bond_final = bond_repayment(i,n)
   print("bond repayment monthly is " + str(bond_final))