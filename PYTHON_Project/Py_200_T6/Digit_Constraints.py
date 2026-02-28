
'''askPY200_T6: Find the Smallest Number With “Digit Constraints” Input: N Find smallest number x in 1..N such that:
• sum of digits of x is divisible by 7 • x contains exactly two 3s • x does not contain digit 0 If none, print -1.'''

# Find the smallest number with given digit constraints

N = int(input("Enter value of N: "))    # User gives the upper limit.

def sum_of_digits(num):                       # This function calculates the sum of digits of a number.For example 133 → 1 + 3 + 3 = 7
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

result = -1

for x in range(1, N + 1):               # We check every number from 1 to N.
    
    s = str(x)                              # We convert number into string so we can: Count digits•	Check if ‘0’ exists

    
    # Condition 1: contains exactly two '3'
    if s.count('3') != 2:
        continue
    
    # Condition 2: does not contain digit '0'
    if '0' in s:
        continue
    
    # Condition 3: sum of digits divisible by 7
    if sum_of_digits(x) % 7 != 0:
        continue
    
    result = x
    break   # stop at first (smallest) valid number
                            # We stop immediately because we need the smallest number.
print(result)

'''
 Example

If N = 200

Smallest valid number = 133

Check:
	•	Contains exactly two 3s 
	•	No 0 digit 
	•	1+3+3 = 7 → divisible by 7

output 133 '''


# If no such number exists → Output: -1