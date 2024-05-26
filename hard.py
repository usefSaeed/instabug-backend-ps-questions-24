from utils import append_number_to_file, read_next_three_ints, read_next_int

class SandMHardTestcase:

    def __init__(self, machine_limits, max_capacity, prices, budget):
        self.__machine_limits = machine_limits
        self.__max_capacity = max_capacity
        self.__prices = prices
        self.__budget = budget

    def solve(self):
        ITEMS_COUNT = 3
        max_machines = 101
        remaining_specs = self.__max_capacity[:]
        for item, cap in zip(self.__machine_limits, self.__max_capacity):
            max_machines = min(max_machines, cap // item)
        for i in range(ITEMS_COUNT):
            remaining_specs[i] -= max_machines * self.__machine_limits[i]
        reached_end = False
        while not reached_end:
            for i in range(ITEMS_COUNT):
                specs_needed =  self.__machine_limits[i] - remaining_specs[i] 
                if specs_needed <= 0:
                    remaining_specs[i] -= self.__machine_limits[i]
                    continue
                budget_needed = specs_needed * self.__prices[i]
                if self.__budget < budget_needed:
                    reached_end = True
                    break
                remaining_specs[i] += specs_needed
                remaining_specs[i] -= self.__machine_limits[i]
                self.__budget -= budget_needed
            if not reached_end:
                max_machines += 1
        return max_machines

class SandMHardDriver:

    def __init__(self, input_path, output_path):
        self.i_path = input_path
        self.o_path = output_path

    def exec(self):
        with open(self.i_path, 'r') as file:
            testcases_count = read_next_int(file)
            for _ in range(testcases_count):
                machine_limits = read_next_three_ints(file)
                max_cap = read_next_three_ints(file)
                prices = read_next_three_ints(file)
                budget = read_next_int(file)
                testcase = SandMHardTestcase(machine_limits, max_cap, prices, budget)
                output = testcase.solve()
                append_number_to_file(output, self.o_path)


prog = SandMHardDriver('./hard.txt','./output.txt')
prog.exec()