# we are going to 4 nested loops in Python
# This code demonstrates nested loops in Python with 4 levels of nesting
for i in range(1, 4):
    print(".external-loop; iteration : ", i)
    for j in range(1, 5):
        print(".internal-loop 1 ", j, end="")
        for k in range(1, 6):
            print(".internal-loop 2 ", k, end="")
            for l in range(1, 7):
                print(".internal-loop 3 ", l, end="")
            print()  # To move to the next line after the innermost loop
        print()  # To move to the next line after the second inner loop
    print()  # To move to the next line after the first inner loop    