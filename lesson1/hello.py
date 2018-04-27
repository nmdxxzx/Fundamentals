def cat_n_times(s, n):
    for i in range(n):
        print(s)

text = input("What would you like the computer to repeat back to you: ")
num = int(input("How many times: ")) # Convert to an int immediately.

cat_n_times(text, num)
