iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1


#Test 1
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
# above is a infinite loop, you have to put a break in the while loop!!!

# Test 2
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        break
# Test 3
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)

