def fooBar ():
    for num in range (100, 100000):
        if num**0.5 % 1 == 0:
            print 'Bar'
        elif num > 1:
            for value in range (2, num):
                if (num % value) == 0:
                    print 'Foobar'
                    break
            else:
                print 'Foo'
        else:
            print 'FooBar'
fooBar()