def happy(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True

# Print the first 8 happy numbers
print([x for x in range(500) if happy(x)][:8])

# Print the first 8 unhappy numbers (optional)
print([x for x in range(500) if not happy(x)][:8])