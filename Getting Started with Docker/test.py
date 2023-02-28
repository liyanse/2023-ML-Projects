from statistics import median
import sys

def ArrayChallenge(arr):
    window_size = arr[0]
    nums = arr[1:]
    medians = []

    # Loop through the numbers in the array
    for i in range(len(nums) - window_size + 1):
        # Slice the array to get the current window of numbers
        window = nums[i:i+window_size]
        # Compute the median of the window and append it to the medians list
        medians.append(str(int(median(window))))

    # Convert the medians list to a string separated by commas and return it
    return ",".join(medians)
  
def main():
    # Get the input array from the command-line arguments
    input_array = list(map(int, sys.argv[1:]))

    # Call the ArrayChallenge function with the input array
    result = ArrayChallenge(input_array)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
