import re
class InputHandler:
    def __init__(self):
        self.isValid = False
        self.input_string = None
        self.__pattern = r"^[1-9/xX]$"
        self.__corresponding_values = {x:10}

    def is_valid_input(self, input_string):
        self.isValid = re.match(self.__pattern, input_string) is not None
        if self.isValid:
            self.input = input_string
    
    def to_number(self,input_string):
        if self.is_valid_input(input_string) or self.isValid is True:
            if re.match(r"^[1-9]$", self.input_string):
                number = int(self.input_string)
                return number
            if re.match(r"^[/xX]$",self.input_string):
                
                return number
                
            