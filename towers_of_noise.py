num_times_solved = 0
def solve(num_disks, start, middle, end):
    global num_times_solved
    if num_disks == 0:
        return
    else:
        num_disks_to_solve = num_disks -1
        solve(num_disks_to_solve,start,end,middle)
        print("move top disk " + str(start) + " to " + str(end))
        print("recursion layer: " + str(num_disks))
        num_times_solved += 1
        print(num_times_solved)
        solve(num_disks_to_solve, middle, start, end )        

solve(int(input("number: ")),1,2,3)