import sys
import re
import string

passport_fle = open(sys.argv[1])
passports = passport_fle.read().split("\n\n")
passport_fle.close()

def byr_validation(year):
    if len(year) == 4:
        year = int(year)
        if year in range(1920, 2003):
            return True

    return False

def iyr_validation(year):
    if len(year) == 4:
        year = int(year)
        if year in range(2010, 2021):
            return True

    return False

def eyr_validation(year):
    if len(year) == 4:
        year = int(year)
        if year in range(2020, 2031):
            return True

    return False

def hgt_validation(height):
    if "cm" in height or "in" in height:
        # split up the hieght using cm or in as a delimeter and keep the delimeter
        # and filter out empty string produced by the split
        height, unit = list(filter(None, re.split(r'(cm|in)', height)))

        if unit == 'cm' and int(height) in range(150, 194):
            return True

        if unit == "in" and int(height) in range(59, 77):
            return True

        return False
    
    return False

def hcl_validation(color):
    if len(color) == 7:
        if color[0] == '#':
            # the map expression returns a list of bools indicating whether the char is a hexdigit
            # if each letter in the string after # is a hexdigit return True
            if False not in list(map(lambda x: x in string.hexdigits, color[1:])):
                return True

    return False

def ecl_validation(color):
    if color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True

    return False

def pid_validation(pid):
    if len(pid) == 9:

        try:
            int(pid)
            return True

        except ValueError:
            pass

    return False

expected_fields = {
        "byr": byr_validation, "iyr": iyr_validation,
        "eyr": eyr_validation, "hgt": hgt_validation, 
        "hcl": hcl_validation, "ecl": ecl_validation, 
        "pid": pid_validation, "cid": lambda x: True
        }

valid_passport_count1 = 0
valid_passport_count2 = 0

for passport in passports:
    fields = {}
    # split up the passport string by whitespace and filter out empty strings
    fields_raw = filter(None, re.split("\s+", passport))

    for raw in fields_raw:
        key, val = raw.split(":")
        fields[key] = val

    diff = set(expected_fields.keys()) - set(fields.keys())
    
    if not diff or (len(diff) == 1 and 'cid' in diff):
        valid_passport_count1 += 1
        
        # 10/10 should never be done in prod code
        if False not in list(map(lambda field_name: expected_fields[field_name](fields[field_name]), fields.keys())):
            valid_passport_count2 += 1
        else:
            pass


print(f'Part one: {valid_passport_count1}')
print(f'Part one: {valid_passport_count2}')
