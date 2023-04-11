# FIFO Disk Scheduling Algorithm

disk_tracks = int(input("Enter the number of disk tracks: "))
track_list = [int(n) for n in input("Enter the tracks: ").split(' ')]

position_head = int(input("Enter the position head: "))

seek_tym = 0

for i in range(len(track_list)-1):
    seek_tym += abs(track_list[i]-track_list[i+1])
seek_tym += abs(track_list[0]-position_head)

print(f"The seek time for thee disk arm is: {seek_tym}")
