def printnumber(n):
    iteration = 0
    print("The number entered by user is", n)
    iteration += 1
    print("Total iterations done by the code is", iteration, "\n")
    print(f"Time Complexity of this loop: O(1)\n")

printnumber(10)
printnumber(20)
print("With any 'n' the time taken by our code won't change\n")


def ONSquareTime(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
            iteration += 1
        print("")
    print(f"\nWhen n is {n}, Iterations = {iteration}")
    print(f"Time Complexity of this loop: O(n^2)\n")

ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("With every 'n' the time taken equals n^2")
print("O(n^2)")

print("\n--- Summary ---")
print("printnumber(n)  -> O(1)   [Constant Time]")
print("ONSquareTime(n) -> O(n^2) [Quadratic Time]")
print("Total Time Complexity: O(1) + O(n^2) = O(n^2)")