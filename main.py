from sympy import symbols
x, y = symbols('x y')
import math

func = input("Welcome to the math calculator! Choose what type of math function you would like to do: an equation (for example, a linear equation in the form mx + b), the pythagorean theorem, or a calculator (not scientific). ")

if func == 'equation':
  q_or_l = input("Quadratic (ax^2+bx+c), or linear (mx+b)? ")
  if q_or_l == 'quadratic':
      a = int(input("Choose an 'a' value "))
      b = int(input("Choose a 'b' value "))
      c = int(input("Choose a 'c' value "))
      exp = a*(x**2) + b*x +c
      print("Your equation is ", exp)
      exp2 = exp.subs(x,int(input("Choose a value for 'x' ")))
      print("The solution to your equation is ", exp2)
  elif q_or_l == 'linear':
      m = int(input("Choose a 'm' value "))
      b = int(input("Choose a 'b' value "))
      eqn = m*x + b
      print("Your equation is ", eqn)
      eqn2 = eqn.subs(x,int(input("Choose a value for 'x' ")))
      print("The solution to your equation is ", eqn2)
  z = 0
  while z < 2:
    asd = input("Do you want to use the calculator again? ")
    z = z + 1
    if asd == 'yes':
      wqe = input("Was your equation quadratic or linear? ")
      if wqe == 'quadratic':
        exp2 = exp.subs(x,int(input("Choose a value for 'x' ")))
        print("The solution to your equation is ", exp2)
      elif wqe == 'linear':
        eqn2 = eqn.subs(x,int(input("Choose a value for 'x' ")))
        print("The solution to your equation is ", eqn2)

elif func == 'pythagorean theorem':
  n = input("Are you tying to calculate for the hypotenuse or a leg? ")
  if n == 'hypotenuse':
    q = int(input("What is the value of the first leg? "))
    z = int(input("What is the value of the second leg? "))
    d = math.sqrt((q**2)+(z**2))
    print("The hypotenuse has length ", d)
  if n == 'leg'
    s = int(input("What is the value of the hypotenuse? "))
    e = int(input("What is the value of the other leg? "))
    r = math.sqrt((s**2)-(e**2))
    print("The leg has length ", r)
