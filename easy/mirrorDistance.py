class Solution:
    def mirrorDistance(self, n: int) -> int:
        str_n = str(n)
        list_n = list(str_n)
        length = len(list_n)

        for i in range(length//2):
            temp = list_n[i]
            list_n[i] = list_n[length-i-1]
            list_n[length-i-1] = temp

        reversed_n = int(''.join(list_n))
        return (abs(n-reversed_n))
    

# sol = Solution()
# print(sol.mirrorDistance(321))



## OR

def mirrorDistance2(n: int) -> int:
    list_n = str(n)

    reversed_str = list_n[::-1]

    reversed_n = int(reversed_str)

    return(abs(n - reversed_n))

print(mirrorDistance2(451))