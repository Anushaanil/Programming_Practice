class Solution:
    '''
    def overlappedInterval(self, intervals):
        output =set()
        for i in range(1,len(intervals),1):
            max_start = max(intervals[i-1][0], intervals[i][0])
            min_stop = min(intervals[i-1][1], intervals[i][1])

            min_start = min(intervals[i-1][0], intervals[i][0])
            max_stop = max(intervals[i-1][1], intervals[i][1])

            print(min_start,min_stop,max_start,max_stop)

            if max_start <= min_stop:
                output.add((min_start,max_stop))
            else:
                output.add((intervals[i-1][0],intervals[i-1][1]))
        print(intervals)
        return output

    '''
    def overlappedInterval(self, intervals):
        output = []
        intervals.sort()
        temp = intervals[0]

        for i in range(len(intervals)):
            if intervals[i][0]<=temp[1]:
                temp[1]=max(intervals[i][1], temp[1])
            else:
                output.append(temp)
                temp = intervals[i]
        output.append(temp)
        return output

    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += [i]
        return out

intervals = [[6,8],[1,9],[2,4],[4,7]]
s = Solution()
print(s.overlappedInterval(intervals))