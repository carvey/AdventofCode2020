import sys

with open(sys.argv[1]) as fle:
    seats_raw = filter(None, fle.read().split('\n'))

seats = []


class Seat:

    def __init__(self, seat_code):
        self.code = seat_code

        self.row = None
        self.column = None
        self.id = None

        self.parse()

    def parse(self):

        def split(nums, code):
            if code == "F" or code == "L":
                return nums[:round(len(nums)/2)]
            elif code == "B" or code == "R":
                return nums[round(len(nums)/2):]

        # first 7 char specify row 0-127 (F = lower & B = upper)
        rows = list(range(0, 128))
        for code in self.code[:7]:
            rows = split(rows, code)

        self.row = rows[0]

        # last 3 chars specifiy column 0-7 (L = lower & R = upper)
        columns = list(range(0, 8))
        for code in self.code[7:]:
            columns = split(columns, code)

        self.column = columns[0]

        self.id = self.row * 8 + self.column


for seat_code in seats_raw:
    seat = Seat(seat_code)
    seats.append(seat)

seat_ids = [seat.id for seat in seats]
max_id = max(seat_ids)
missing_id = (set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)).pop()

print(f"Part 1: {max_id}")
print(f"Part 2: {missing_id}")
