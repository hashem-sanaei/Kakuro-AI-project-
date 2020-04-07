from csp import *
import time

class Kakuro(CSP):

    def __init__(self, puzzle):

        self.puzzle = puzzle
        variables = []
        for i, line in enumerate(puzzle):
            # print line
            for j, element in enumerate(line):
                if element == '_':
                    var1 = str(i)
                    if len(var1) == 1:
                        var1 = "0" + var1
                    var2 = str(j)
                    if len(var2) == 1:
                        var2 = "0" + var2
                    variables.append("X" + var1 + var2)

        domains = {}

        for var in variables:
            domains[var] = set(range(1, 10))

        self.sumsAndVar = [] 		# (sum,[var1,var2,...])

        for i, line in enumerate(puzzle):
            for j, element in enumerate(line):
                if element != '_' and element != '*':
                    # down - column
                    if element[0] != '':
                        x = []
                        for k in range(i + 1, len(puzzle)):
                            if puzzle[k][j] != '_':
                                break
                            var1 = str(k)
                            if len(var1) == 1:
                                var1 = "0" + var1
                            var2 = str(j)
                            if len(var2) == 1:
                                var2 = "0" + var2
                            x.append("X" + var1 + var2)
                        self.sumsAndVar.append((element[0], x))

                    # right - line
                    if element[1] != '':
                        x = []
                        for k in range(j + 1, len(puzzle[i])):
                            if puzzle[i][k] != '_':
                                break
                            var1 = str(i)
                            if len(var1) == 1:
                                var1 = "0" + var1
                            var2 = str(k)
                            if len(var2) == 1:
                                var2 = "0" + var2
                            x.append("X" + var1 + var2)
                        self.sumsAndVar.append((element[1], x))

        neighbors = {}

        for var in variables:
            neighbors[var] = []
            for line in self.sumsAndVar:
                if var in line[1]:
                    neighbors[var] += line[1]
                    del neighbors[var][neighbors[var].index(var)]

        CSP.__init__(self, variables, domains,
                     neighbors, self.FindConstraints)

    def FindConstraints(self, A, a, B, b):

        if a == b:
            return False

        emptySpace = 0
        currentSum = 0
        numbers = []

        for element in self.sumsAndVar:

            variables = element[1]
            totalSum = element[0]

            if A in variables and B in variables:

                for var in variables:
                    if var == A:
                        numbers.append(a)
                    elif var == B:
                        numbers.append(b)
                    else:
                        if self.curr_domains == None or len(self.curr_domains[var]) > 1:
                            emptySpace += 1
                        elif len(self.curr_domains[var]) == 1:
                            numbers.append(*self.curr_domains[var])
                if emptySpace > 0:
                    currentSum = sum(numbers)
                    if currentSum <= totalSum:
                        return True
                    else:
                        return False
                else:
                    currentSum = sum(numbers)
                    if currentSum == totalSum:
                        return True
                    else:
                        return False
        return True

    def display(self, assignment=None):
        for i, line in enumerate(self.puzzle):
            puzzle = ""
            for j, element in enumerate(line):
                if element == '*':
                    puzzle += "[*]\t"
                elif element == '_':
                    var1 = str(i)
                    if len(var1) == 1:
                        var1 = "0" + var1
                    var2 = str(j)
                    if len(var2) == 1:
                        var2 = "0" + var2
                    var = "X" + var1 + var2
                    if assignment is not None:
                        if isinstance(assignment[var], set) and len(assignment[var]) is 1:
                            puzzle += "[" + str(first(assignment[var])) + "]\t"
                        elif isinstance(assignment[var], int):
                            puzzle += "[" + str(assignment[var]) + "]\t"
                        else:
                            puzzle += "[_]\t"
                    else:
                        puzzle += "[_]\t"
                else:
                    puzzle += str(element[0]) + "\\" + str(element[1]) + "\t"
            print(puzzle)

print()
print()
print("-------------------------kakuro1------------------------")
print()

kakuro_fw = Kakuro(kakuro1)
start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with simple backtracking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=forward_checking)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with forward checking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=mac)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with MAC search in ", totalTime,"microseconds")
print()
kakuro_fw.display(kakuro_fw.infer_assignment())

print()
print()
print("-------------------------kakuro2------------------------")
print()
kakuro_fw = Kakuro(kakuro2)
start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with simple backtracking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=forward_checking)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with forward checking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=mac)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with MAC search in ", totalTime,"microseconds")
print()
kakuro_fw.display(kakuro_fw.infer_assignment())

print()
print()
print("-------------------------kakuro3------------------------")
print()
kakuro_fw = Kakuro(kakuro3)
start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with simple backtracking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=forward_checking)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with forward checking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=mac)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with MAC search in ", totalTime,"microseconds")
print()
kakuro_fw.display(kakuro_fw.infer_assignment())

print()
print()
print("-------------------------kakuro4------------------------")
print()

kakuro_fw = Kakuro(kakuro4)
start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with simple backtracking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=forward_checking)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with forward checking search in ", totalTime,"microseconds")

print()
kakuro_fw.display(kakuro_fw.infer_assignment())
print()

start = float(round(time.time() * 1000))
result = backtracking_search(kakuro_fw, inference=mac)
end = float(round(time.time() * 1000))

if not result:
	print("There's no result for this algorithm")

totalTime = end - start;
print("Problem solved with MAC search in ", totalTime,"microseconds")
print()
kakuro_fw.display(kakuro_fw.infer_assignment())