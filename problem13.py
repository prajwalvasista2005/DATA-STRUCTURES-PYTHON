message="Global Message"
def outer():
    message="Outer message"
    def inner():
        print(message)
        
    inner()
outer()
print(message)

