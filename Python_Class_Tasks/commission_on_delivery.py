number_of_daily_deliveries_to_be_made = 100

riders_delivery = int(input("Enter the number of deliveries made: "))

commission_rate = (riders_delivery / number_of_daily_deliveries_to_be_made) * 100

commission_pay = 0

amount_per_parcel = 0

BASE_PAY = 5000

if commission_rate < 50:

	amount_per_parcel = 160

elif commission_rate >= 50 and commission_rate <= 59:

	amount_per_parcel = 200


elif commission_rate >= 60 and commission_rate <= 69:

	amount_per_parcel = 250

else:

	amount_per_parcel = 500


commission_pay = riders_delivery * amount_per_parcel + base_pay

print(commission_pay)







