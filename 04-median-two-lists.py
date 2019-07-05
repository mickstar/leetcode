# from math import ceil,floor,inf

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        if n == 1:
            if nums1 == []: return nums2[0]
            return nums1[0]
        if n == 2:
            if nums1 == []:
                return (nums2[0]+nums2[1])/2.0
            elif nums2 == []:
                return (nums1[0]+nums1[1])/2.0
            else:
                return (nums1[0] + nums2[0]) / 2.0
        middle = math.ceil(n / 2)
        pos1 = 0
        pos2 = 0
        i=0
        cur=0
        while i < middle:
            if (pos1 < len(nums1)):
                v1 = nums1[pos1]
            else:
                v1 = math.inf

            if (pos2 < len(nums2)):
                v2 = nums2[pos2]
            else:
                v2 = math.inf

            if (v1<v2):
                cur = v1
                pos1 += 1
            else:
                cur = v2
                pos2 += 1
            # print(i,cur,v1,v2,pos1,pos2)
            i+=1

        if (n%2 == 1):
            return cur
        else:
            # print("next",cur,self.getNext(nums1,nums2,pos1,pos2))
            return (cur + self.getNext(nums1,nums2,pos1,pos2)) / 2.0

    def getNext(self, nums1, nums2, pos1, pos2):
        try:
            v1 = nums1[pos1]
        except:
            v1 = math.inf
        try:
            v2 = nums2[pos2]
        except:
            v2 = math.inf
        return min(v1,v2)
