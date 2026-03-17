class LinearSearch:
    def solution(self,arr,element):
        is_present=False
        for num in arr:
            if num == element:
                is_present=True
                break
        return is_present
ls_instance=LinearSearch()
arr=[10,11,12,13,43,25,2]
element=2
print(ls_instance.solution(arr,element))
#1010011010101010100100100101000110