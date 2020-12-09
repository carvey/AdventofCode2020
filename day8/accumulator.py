import sys
import re

with open(sys.argv[1]) as instruction_fle:
    instructions = []
    for instruction_raw in instruction_fle.readlines():
        instruction, value = instruction_raw.strip().split(" ")
        instructions.append({'instruction': instruction, 'value': value, "count": 0})

def run(switched_index=None):
    """
    If a switched_index arg is provided, the instruction at that particular index will be switched.
    Switches are between NOP <-> JMP only.

    This function will return the value of the accumulator and True or False indicating if all instructions
    were ran without a loop.
    """
    accumulator = 0
    index = 0

    for instruction in instructions:
        instruction['count'] = 0

    while True:
        if index == len(instructions) - 1:
            return accumulator, True

        instructions_dict = instructions[index]

        instruction = instructions_dict['instruction']
        value = instructions_dict['value']
        count = instructions_dict['count']

        if switched_index == index:
            if instruction == "jmp":
                instruction = "nop"
            elif instruction == "nop":
                instruction = "jmp"

        if count == 1:
            return accumulator, False
            break

        instructions[index]['count'] += 1

        if instruction == "nop":
            index += 1
            continue

        elif instruction == "acc":
            if value[0] == "-":
                accumulator -= int(value[1:])

            elif value[0] == "+":
                accumulator += int(value[1:])

            index += 1
            continue

        elif instruction == "jmp":
            if value[0] == "-":
                index -= int(value[1:])

            elif value[0] == "+":
                index += int(value[1:])
            
            continue

final_accumulator = None
for index, instruction in enumerate(instructions):
    if instruction['instruction'] == "jmp" or instruction['instruction'] == "NOP":
        accumulator, completed = run(index)

    if completed:
        final_accumulator = accumulator
        break

print(f"Part 1: {run()[0]}")
print(f"Part 2: {final_accumulator}")

