class AddCommand:
    def execute(self, *args):
        return sum(args)

class SubtractCommand:
    def execute(self, *args):
        return args[0] - sum(args[1:])

class MultiplyCommand:
    def execute(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

class DivideCommand:
    def execute(self, *args):
        if len(args) < 2 or args[1] == 0:
            raise ValueError("Cannot divide by zero or insufficient arguments")
        return args[0] / args[1]
