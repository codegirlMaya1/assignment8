pizza_dough=1
grilled_chickenPack=1
canned_marinara_=1
pineapple_chunkPack=1
black_olivesPack=1
chicken_pizza= pizza_dough, grilled_chickenPack, canned_marinara_,pineapple_chunkPack,black_olivesPack
recipe=sum(chicken_pizza)
print(recipe)


start_order=int(input("Enter 1 to begin calculating recipe order:    "))
recipe_1=int(input(" Each pie is considered 1 serving and has 8 large slices. 1 serving = one pack each of pizza dough, grilled chicken, marinara, pineapple and black olives.... How many servings do you  need?:  "))
recipe_2=int(input(" These are very delicious chicken pizzas. Please enter the number of extra servings you would like.:  "))

order=recipe_1 + recipe_2
if start_order==1:
    print("Perfect there are", order*recipe,"ingredients needed to make a recipe of", order, 'servings of delicious Chicken Pineapple Pizza Pie!' )
    pass
try :
    ValueError
    print( "The difference of amount of ingredients for your original recipe order vs those extras pizzas you would really like is only:",order*recipe/5- recipe_1/5)
finally:
    print(" ***This message is displayed with/without exceptions.*** The summary today is that there are", order*recipe,"ingredients needed to make a recipe of", order, "servings of delicious Chicken Pineapple Pizza Pie!" )
    