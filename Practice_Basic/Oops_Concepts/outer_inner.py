class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "'Init function call'"

        def set_name(self):
            self.name = "'Inner Set name function call'"
            
        def display(self):
            print("This is the inner class", self.name)


outer = Outer()
print(outer.name)
inner = outer.Inner()   # Inner class object
inner.display()
inner.set_name()
inner.display()
