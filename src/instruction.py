class Instruction:
    def __init__(self, input_states: list, function_list: list, output_states: list):
        self.input = input_states
        self.output = output_states
        self.functions = function_list
    
    