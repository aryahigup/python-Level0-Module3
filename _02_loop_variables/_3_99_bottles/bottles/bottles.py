count = 99
for i in range(99):
    if count == 2:
        print(str(count) + " bottles of beer on the wall, " + str(
            count) + " bottles of beer. \n Take one down and pass it around, "
              + str(count - 1) + " bottle of beer on the wall.")
    elif count == 1:
        print(str(count) + " bottle of beer on the wall, " + str(
            count) + " bottle of beer. \n Take one down and pass it around, no more bottles of beer on the wall."
                     "\n No more bottles of beer on the wall, no more bottles of beer. \n"
                     "Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print(
            str(count) + " bottles of beer on the wall, " + str(count) + " bottles of beer. \n Take one down and pass "
                                                                         "it around, " + str(
                count - 1) + " bottles of beer on the wall.")
    count = count - 1
