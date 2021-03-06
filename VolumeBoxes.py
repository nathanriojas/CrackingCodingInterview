# the following functions go through a given array from left to right and find the number of empty spaces between a maximum
# on the left and right. The function used to do this only counts volume when there a definitive end on the right (i.e. the right bound
# is greater than the left). Because it does not consider bounds where the left is greater than the right, this function must
# be run again on the reverse of the given array. Adding the totals from each yields the total volume. If two bounds have the same max
# an overlap value will be counted, since this would be counted twice during the final calculation. So the overlap is subtracted out.
# The is done in O(n) time


# go through the array and find the volume between each section where there are indices with boxes less that 
# a set of boxes (on the left and right), where the right is greater than the left
def left_to_right (arr):
    total_volume = 0
    left = 0  # left max index
    box_count = 0 # repeatedly count the number of boxes between the left and right stack to get volume
    overlap = 0 # volume to subtract due to overlap
    max_boxes = arr[left] # number of boxes that occur where the maximum is
    for box in range(1, len(arr)):
        if arr[box] >= arr[left]:
            diff = box - left - 1 # how many units are between the left max and the current box
            if (left == 0):
                diff -= 1
            total_volume += (diff * arr[left]) - box_count
            if arr[box] == arr[left] and arr[box] == max_boxes: # two equal ends with that are maxes of the array
                overlap += (diff * arr[left]) - box_count # emsure they are not counted twice in final calculation
            elif arr[box] > max_boxes:
                max_boxes = arr[box] # if a new max occurs that does not have a duplicate erase previously thought overlaps
                overlap = 0
            left = box
            box_count = 0
        else:
            box_count += arr[box]
    return total_volume, overlap

def find_volume (arr):
    if len(arr) < 3: # volume can only occur if there is at least one unit diff between ends
        return 0
    volume_Start_Left, overlap = left_to_right(arr)
    volume_Start_Right, overlap = left_to_right(arr[::-1])
    return volume_Start_Left + volume_Start_Right - overlap


def main():
    #sample tests
    #box_array = [0,4,0,4,0,4,0]
    #box_array = [2,5,0,0,2,1,6,0,0,1,0,2,6,0,1,2,4,0,5]
    #box_array = [0,0,0,5,0,0,0]
    #box_array = [1, 0, 0, 5, 0, 0, 0]
    box_array = [0, 0, 0, 5, 0, 0, 1]
    print(find_volume(box_array))

main()


