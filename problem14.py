level="Global"
def outer():
    level="enclosing"
    def inner():
        level="local"
        print(level)

    inner()

    print(level)
outer()
print(level)