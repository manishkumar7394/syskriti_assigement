'''TaskPY200_T3: Write program to calcite Electricity Bill Slabs. User enters a bill unit and gets the total bill according to following logic.
Input: units Rates: • First 100 @ 2/unit • Next 100 (101–200) @ 3/unit • Next 300 (201–500) @ 5/unit
• Above 500 @ 8/unit Add fixed charge 50 if units > 0 Print total bill'''

# Electricity Bill Calculator

units = int(input("Enter electricity units consumed: "))

 bill = 0                  #This variable will store the total calculated bill amount.

if units > 0:               # If units are 0 or negative, the bill calculation will not proceed.

    # First 100 units
    if units <= 100:
        bill = units * 2            # Each unit costs ₹2. So, total bill = units × 2
    else:    
        bill = 100 * 2               # So, 100 × 2 = 200 is added to the bill.

        # Next 100 units (101–200)
        if units <= 200:
            bill += (units - 100) * 3       #  The remaining units after 100 are charged ₹3 per unit.(units - 100) gives the number of units after the first 100. += means add this amount to the existing bill.
        else:
            bill += 100 * 3

            # Next 300 units (201–500)
            if units <= 500:
                bill += (units - 200) * 5           # Units after 200 are charged ₹5 per unit.
            else:
                bill += 300 * 5                     # Full 300 units (201–500) are charged ₹5 per unit. So, 300 × 5 = 1500 is added.

                # Above 500 units
                bill += (units - 500) * 8           #If units are more than 500, The remaining units above 500 are charged ₹8 per unit.

    # Add fixed charge
    bill += 50                              # If units > 0, A fixed charge of ₹50 is added to the total bill.

print("Total Electricity Bill:", bill)          # This prints the final calculated electricity bill.

'''Example (250 Units)
	•	First 100 → 100 × 2 = 200
	•	Next 100 → 100 × 3 = 300
	•	Remaining 50 → 50 × 5 = 250
	•	Fixed charge → 50

Total = 800'''
