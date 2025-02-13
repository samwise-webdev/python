def find_it(seq):
    # I really don't understand why this isn't working :(
    for item in seq:
        counting = seq.count(seq[0])
        if counting % 2 != 0:
            print(item)
            return item
        elif counting == 1:
            print(item)
            return item
# these don't do what I need them to
    # for item in seq:
    #     counting = seq.count(seq[0])
    #     if counting % 2 != 0:
    #         print(item)
    #     else:
    #         pass
    # for item in seq:
    #   if item % 2 == 0:
    #       pass
    #   else:
    #       print(item)


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])