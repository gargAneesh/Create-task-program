# tool that allows to solve for x
from sympy import symbols
x, y = symbols('x y')
# library for special math functions such as square root
import math

func = input("Welcome to the math calculator! Choose what type of math operation you would like to do: an equation (for example, a linear equation in the form mx + b), the pythagorean theorem, the quadratic formula, or a calculator. ")

# user chooses the type of equation
if func == 'equation':

  q_or_l = input("Quadratic (ax^2+bx+c), or li
  near (mx+b)? ")
  # if user chose quadratic equation
  if q_or_l == 'quadratic':
      # creates class to handle a,b, and c values
      class quadratic:
        def __init__(self, a, b, c):
          self.a = a
          self.b = b
          self.c = c
          # user chooses a,b, and c values
      p1 = quadratic(int(input("Choose an a value ")), int(input("Choose a b value ")), int(input("Choose a c value ")))
      # creates and shows user's equation
      eqn = p1.a*(x**2) + p1.b*x + p1.c
      print("Your equation is, ", eqn)
      # solves user's equation for a value of x they provide
      exp = eqn.subs(x, int(input("Choose a value for x ")))
      # shows solution
      print("The solution to the equation is,", exp)
      # loop to prompt user if they would like to resuse their equation after each use
      z = 0
      while z < 1000:
        asd = input("Do you want to use the calculator again? ")
        # 1 added to the variable, z, so that the loop is not infinite. Since the condition keeps z less than 2, it will prompt the user again after each run
        z = z + 1
        if asd == 'yes':
            exp = eqn.subs(x,int(input("Choose a value for 'x' ")))
            print("The solution to your equation is ", exp)
        else:
          print("Goodbye")
  # if user chose a linear equation
  elif q_or_l == 'linear':
      # user chooses values to be substituted into the equation
      m = int(input("Choose a 'm' value "))
      b = int(input("Choose a 'b' value "))
      # the equation is formed using the user's values put into the shell
      eqn = m*x + b
      # shows user their equation
      print("Your equation is ", eqn)
      # prompts user for x-value
      eqn2 = eqn.subs(x,int(input("Choose a value for 'x' ")))
      print("The solution to your equation is ", eqn2)
      # loop to prompt user if they would like to resuse their equation after each use
      z = 0
      while z < 1000:
        asd = input("Do you want to use the calculator again? ")
        # 1 added to the variable, z, so that the loop is not infinite. Since the condition keeps z less than 2, it will prompt the user again after each run
        z = z + 1
        if asd == 'yes':
          # solves equation
          eqn2 = eqn.subs(x,int(input("Choose a value for 'x' ")))
          print("The solution to your equation is ", eqn2)
        else:
          print("Goodbye")

elif func == 'pythagorean theorem':
  # determines what to calculate
  n = input("Are you tying to calculate for the hypotenuse or a leg? ")
  if n == 'hypotenuse':
    while True:
      try:
        # gets values of sides
        q = int(input("What is the value of the first leg? "))
        z = int(input("What is the value of the second leg? "))
        # solves
        d = math.sqrt((q**2)+(z**2))
        # shows solution
        print("The hypotenuse has length ", d)
        break
      except ValueError:
        print("The triangle has no real value for the hypotenuse.")
        break
  if n == 'leg':
    while True:
      try:
        s = int(input("What is the value of the hypotenuse? "))
        e = int(input("What is the value of the other leg? "))
        r = math.sqrt((s**2)-(e**2))
        print("The leg has length ", r)
        break
      except ValueError:
        print("The triangle has no real value for the leg.")
        break
     

elif func == 'calculator':
  q = input("What do you want to be calculated?(For exponential calculations use **followed by the number. ex: 2**3 = 8. You can use this for logarithms as well if you use a fractional exponent.) ")
  print("The solution is:")
  # takes user input and solves
  print(eval(q))
  z = 0
  # same loop used as before, which will prompt the user if they want to go again
  while z < 2:
    again = input("Go again? ")
    z = z + 1
    if again  == 'yes':
      # solves again
      wqe = input("What do you want to be calculated?(For exponential calculations use **followed by the number. ex: 2**3 = 8) ")
      print("The solution is: ")
      print(eval(wqe))
    elif again == 'no':
      print("Goodbye")

elif func == 'quadratic formula':
  # determines value from user for substituting
  a = int(input("What is the 'a' value of the equation? "))
  b = int(input("What is the 'b' value of the equation? "))
  c = int(input("What is the 'c' value of the equation? "))
  while True:
    try:
      s1 = -b + (math.sqrt((b**2) - (4*a*c)))
      s2 = s1/2*a
      s3 = -b - math.sqrt((b**2) - (4*a*c))
      s4 = s3/2*a
      # shows both solutions to equation, if there are any
      print("The first solution to the equation, when equal to 0, is ", s4)
      print("The second solution to the equation, when equal to 0, is ", s2)
      break
    except ValueError:
      # if the solution is not possible, resulting in ValueError, this will be displayed
      print("There was no real solution to your equation.")
      # ends program (prevents infinite looping)
      break
