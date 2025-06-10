# problem:
# given an array of ints -> return k ints starting from the highest frequency
# soln: bucket sort O(n)
# variation of bucket sort, we will use frequency as the "index"
# and the numbers of each frequency as the values
# the "index" is determined by the length of the array because edge case all ints in the array are the same
# then the int is as frequent as the length of the array

# we want to have a count for each int
# then we want to track the frequency 
# then iterate over the frequence table to return the k most frequence elements
# frequency table has count and val -> therefore use count.items()

def top_k_most_freq_elts(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    # count dict matches number to count
    
    freq = [[] for i in range(len(nums) + 1)]
    for num, cnt in count.items():
        freq[cnt].append(num)

    # then iterate the frequency backwards returning the highest frequency values first k times
    result = []
    # start from end of array and walk to the start of array -> 0 is exclusive since no elt can be less frequent than 1 time
    for i in range(len(freq) - 1, 0, -1):
        # we then traverse the list of numbers under each frequency incase there are 3 numbers with the same frequency but k = 2
        for n in freq[i]:
            result.append(n)
            # continue appending until result is the length of k -> k most freq elts are found
            if len(result) < k:
                continue
            else:
                return result