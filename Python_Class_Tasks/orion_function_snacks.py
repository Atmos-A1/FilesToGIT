name_of_item = input("Enter the name of item: ")

original_price_of_item = int(input("Enter the original price of the item: "))

promo_code = input("Enter promo code: ")

discount_cost = 0

if promo_code.casefold() == "save10":

	discount_cost = original_price_of_item * 0.1

elif promo_code.casefold() == "halfoff":

	discount_cost = original_price_of_item * 0.5

else:

	discount_cost = 0

final_cost = original_price_of_item - discount_cost


print(final_cost)





