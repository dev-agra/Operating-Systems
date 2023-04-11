#  SCAN Disk Scheduling Algorithm

disk_tracks = int(input("Enter the number of disk tracks: "))
track_list = [int(n) for n in input("Enter the tracks: ").split(' ')]
last_head = round(max(track_list)/100)*100
position_head = int(input("Enter the position head: "))

# Whether to go on the increasing side or the decreasing side
choice = int(input("Enter the choice: "))
seek_tym = 0

if choice == 1:  # Maximum
    seek_tym += abs((last_head - 1) - position_head)
    seek_tym += abs((last_head - 1) - min(track_list))

elif choice == 0:  # Minimum
    seek_tym += max(track_list) + position_head

print(f'Seek time for the SCAN Algorithm is: {seek_tym}')
