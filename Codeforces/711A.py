n = int(input())  # number of rows of seats on bus

bus_status = []
for row_number in range(n):
    bus_status.append(input())

solution = ""

have_seat = False
for row_of_seats in bus_status:
    if not have_seat and row_of_seats[0] == row_of_seats[1] == "O":
        solution += "++" + row_of_seats[2:] + "\n"
        have_seat = True
    elif not have_seat and row_of_seats[3] == row_of_seats[4] == "O":
        solution += row_of_seats[:3] + "++\n"
        have_seat = True
    else:
        solution += row_of_seats + "\n"

if (have_seat):
    print("YES\n" + solution)
else:
    print("NO")
