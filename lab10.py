nums = []
while True:
    value = input('enter a number or done ')
    if value == "done":
        break
    try:
        nums.append(int(value))
    except ValueError:
        print('not a number please try agian')



print(nums)