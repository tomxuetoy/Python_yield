def h():  
    print 'Wen Chuan',
    m = yield 5 # Fighting!  
    print m  
    d = yield 12  
    print 'We are together!'  
c = h()  
mm = c.next() #m gets the value of yield 5
dd = c.send('Fighting!') #d gets the value of yield 12
print 'We will never forget the date', mm, '.', dd
