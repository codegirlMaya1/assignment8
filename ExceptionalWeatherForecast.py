
def weather():
   while True:
       try:
          num=int(input( "Enter the weather: "))
          return num
       except ValueError:
           print("Please enter numbers only")

results=weather
print(results)
new_input=int(input( "Enter the weather: "))
if new_input >0:
    print(" The weather is", new_input, )
else:
    print("Please enter numbers only")
    pass

try:
    
    ZeroDivisionError
except ZeroDivisionError:
    pass
    divide=0.5
    celsius_sum=sum(new_input)
    celsius_total=celsius_sum*divide
    print( celsius_total)
    
input2=input(" Would you like to see the weather of in celsius? Type lower yes or no: ")
if input2=="yes":
    print(new_input*0.5) 
    
else:
    print( " In celsius the weather is ",new_input*0.5,)
    pass

try :
    ValueError
finally:
    print(" ***This message is displayed with/without exceptions.*** The summary of your interaction today is: The weather is ", new_input," , and in celsius the weather is ",new_input*0.5, )
    

  

