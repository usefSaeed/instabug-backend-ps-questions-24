from utils import append_number_to_file, read_next_three_ints, read_next_int

class SandMEasyTestcase:

    def __init__(self, machine_limits, max_capacity):
        self.__machine_limits = machine_limits
        self.__max_capacity = max_capacity

    def solve(self):
        max_machines = 101
        for item, cap in zip(self.__machine_limits, self.__max_capacity):
            max_machines = min(max_machines, cap // item)
        return max_machines

class SandMEasyDriver:

    def __init__(self, input_path, output_path):
        self.i_path = input_path
        self.o_path = output_path

    def exec(self):
        with open(self.i_path, 'r') as file:
            N = read_next_int(file)
            for _ in range(N):
                machine_limits = read_next_three_ints(file)
                max_cap = read_next_three_ints(file)
                testcase = SandMEasyTestcase(machine_limits, max_cap)
                output = testcase.solve()
                append_number_to_file(output, self.o_path)


prog = SandMEasyDriver('./easy.txt','./output.txt')
prog.exec()

