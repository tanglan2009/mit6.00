# num = 5
# if num > 2:
#     print num
#     num -= 1
# print num

# num = 2
# while num <= 8:
#     print num
#     num += 2
# print num
# print "Goodbye!"
#
# for num in range(5):
#     print num

# for variable in range(20):
#     if variable % 4 == 0:
#         print variable
#     if variable % 16 == 0:
#         print 'Foo!'
#
# for num in range(2,12,2):
#     print num
# print 'Goodbye!'


# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in 'hello, world':
#         count += 1
#     print 'Iteration' + str(iteration) + '; count is: ' + str(count)
#     iteration += 1


#
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration +=1



