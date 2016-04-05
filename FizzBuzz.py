count = 1
x = int(raw_input("Vnesi stevilo med 1 in 100: "))
while  x < 1 or x > 100:
        print "Stevilo ni v skladu z navodili"
        x = int(raw_input("Vnesi pravilno stevilo: "))
else:
    for x in range(1, x + 1):
        if (count % 5) == 0 and (count % 3) == 0:
            print "fizzbuzz"
            count = count + 1
        elif (count % 3) == 0:
            print "fizz"
            count = count + 1
        elif (count % 5) == 0:
            print "buzz"
            count = count + 1
        else:
            print count
            count = count + 1