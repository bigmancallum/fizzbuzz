Number = 0 #Sets Number to 0 at start

for i in range (100): #Repeat 100 times
  Number = Number + 1 #Add 1 to Number

  #If Number is a multiple of 3 and 5 display "FizzBuzz"
  if Number % 3 == 0 and Number % 5 == 0:
    print ("FizzBuzz")
  
  #If Number is a multiple of 3 display "Fizz"
  elif Number % 3 == 0:
    print ("Fizz")

  #If Number is a multiple of 5 display "Buzz"
  elif Number % 5 == 0:
    print ("Buzz")

  #If Number is a multiple of neither 3 or 5 display just the number
  else:
    print(Number)
