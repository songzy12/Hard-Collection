class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [None for i in range(len(people))]
        queue = [i for i in range(len(people))]
        people.sort()
        i = 0
        _people = [list(x) for x in people] # NOTE: store origin array
        while i < len(people):
            j = i + 1
            while j < len(people) and people[j][0] == people[i][0]:
                people[j][-1] -= (j - i) # NOTE: remove same one
                j += 1
            i = j
        for i in range(len(people)):
            h, k = people[i]
            index = queue.pop(k)
            res[index] = _people[i]
        return res

# idea: maintain a queue q of indices
# then sort the heights
# for each h, pop the k-th element of 