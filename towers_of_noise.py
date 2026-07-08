def solve(num_disks, start, middle, end):
    if num_disks == 0:
        return
    else:
        num_disks_to_solve = num_disks -1
        solve(num_disks_to_solve,start,end,middle)
        pinrt("move top disk from" + start + "to" + "end ")

