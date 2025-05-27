# This code demonstrates nested loops in Python 
for i in range(1, 4):
    print(".external-loop; iteration : ", i)
    for j in range(1, 5):
        print(".internal-loop ",j,end="")
    print()  # To move to the next line after the inner loop
