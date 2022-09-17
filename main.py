print("Welcome to the tip calculator.")

total_bill = float(input("What is the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = float(input("How many people to split the bill? "))

percentage = percent / 100

amount_split = total_bill / split_bill
amount_taxed = amount_split * percentage
amount_total = round(amount_split + amount_taxed, 2)
amount_total = "{:.2f}".format(amount_total)
print(f"Each person should pay: ${amount_total}")