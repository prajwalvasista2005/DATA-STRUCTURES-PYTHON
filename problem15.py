def outer():
    count=5
    def inner():
        nonlocal count
        count+=1
       
    inner()
    inner()
    inner()
    print(count)
outer()