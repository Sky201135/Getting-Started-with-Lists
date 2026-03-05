start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

squares = [n**2 for n in range(start, end+1)]

even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)