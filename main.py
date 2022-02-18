number = 0 #Sets number to 0 at start

for i in range (100): #Repeat 100 times
  number = number + 1 #Add 1 to number

  #If number is a multiple of 3 and 5 display "FizzBuzz"
  if number % 3 == 0 and number % 5 == 0:
    print ("FizzBuzz")
  
  #If number is a multiple of 3 display "Fizz"
  elif number % 3 == 0:
    print ("Fizz")

  #If number is a multiple of 5 display "Buzz"
  elif number % 5 == 0:
    print ("Buzz")

  #If number is a multiple of neither 3 or 5 display just the number
  else:
    print(number)
