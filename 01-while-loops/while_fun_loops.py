#i = 1
#numbers = []

#while i <= 20:
    
#    if(i == 13):
#        print "hello"
        #numbers.append("Hello")
#    else:
 #       print i
        #numbers.append(i)
 #   i += 1

#print numbers 


#i = 0

#while i <= 10:
#    if(i%2!=0):
#        print i 
#    i += 1


#i = 10

#while i >= 0:
    
#    if (i==0):
#        print "Blastoff"
#    else: 
#        print i 

#    i -= 1

#fruits = ["apples", "oranges", "bananas"]
#index = 0 

#while (index < len(fruits)):
#    print fruits[index]  
#    index += 1


#def sum_nums(num):
#    sum = 0
#    i = 0

#    while i<num+1: 
#        sum += i 
#        i+=1 
#    return sum  

#print sum_nums(3)


def sum_nums2(num):
    sum = 0
    i = 0
    if num<0:
        i = num
        num = 0

    while i<=num: 
        sum += i 
        i+=1
    return sum  

print sum_nums2(3)
