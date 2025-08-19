# Python program to check duplicates among 5 integers

# Accept 5 integers from user
nums = []
for i in range(5):
    n = int(input(f"Enter integer {i+1}: "))
    nums.append(n)

# Check duplicates using set
if len(nums) != len(set(nums)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")
