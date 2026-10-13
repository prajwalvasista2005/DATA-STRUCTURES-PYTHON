def outer():
    number=10
    def inner():
        print(number)
    inner()
outer()