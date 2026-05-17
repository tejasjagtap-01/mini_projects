#Inputs required - 
# 1. total rent ; 
# 2. total food order ; 
# 3. Electricity Unit use ; 
# 4. Charge per unit;
# 5. Total Number of Roommates

# Output -> Total amount to pay

rent = int(input("Enter the total rent: "))
food_order = int(input("Enter the amount of food ordered: "))
electricity_use = int(input("Enter the total number of units used: "))
charge = int(input("Enter the charge per unit: "))
persons = int(input("Enter the total number of persons: "))

total_elcetricity = electricity_use * charge

output = (rent + food_order + total_elcetricity) // persons

print(f"The amount paid by each member is {output}")