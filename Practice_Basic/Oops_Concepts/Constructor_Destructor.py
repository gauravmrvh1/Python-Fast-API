class Demo:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


d = Demo()
