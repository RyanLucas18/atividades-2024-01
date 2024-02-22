# Ryan Lucas Pires Campos

print("                ")
print("#### Maior soma possível de números consecutivos ####")
print("                ")

def max_consecutive_sum(nums):
    if not nums:
        return 0
    
    soma_max = soma_atual = nums[0]
    
    for num in nums[1:]:
        soma_atual = max(num, soma_atual + num)
        soma_max = max(soma_max, soma_atual)
    
    return soma_max


nums1 = [1, -3, 2, 1, -1]
print("Maior soma de números consecutivos em", nums1, ":", max_consecutive_sum(nums1))

nums2 = [2, -1, 3, 5, -6, 2, 1]
print("Maior soma de números consecutivos em", nums2, ":", max_consecutive_sum(nums2))


print("Maior soma de números consecutivos em [-2, 1, -3, 4, -1, 2, 1, -5, 4]: ", max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print("Maior soma de números consecutivos em [5, -1, -2, 3, -1, 2, -4]: ", max_consecutive_sum([5, -1, -2, 3, -1, 2, -4])) # 6
print("Maior soma de números consecutivos em [1]: ", max_consecutive_sum([1])) # 1
print("Maior soma de números consecutivos em [-1, -2, -3, -4, -5]: ", max_consecutive_sum([-1, -2, -3, -4, -5])) # -1


def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

print("                ")
print("#### Palidrome ####")
print("                ")


print("A palavra radar: ", is_palindrome("radar"))   
print("A palvavra Ana: ", is_palindrome("Ana"))
print("A palavra ossos: ", is_palindrome("osso"))
print("A palavra python: ", is_palindrome("python"))


def count_increasing_subsets(nums):
    def count_subsets_helper(nums, anterior, atual):
        if atual == len(nums):
            return 1

        count = 0

        if nums[atual] > nums[anterior]:
            
            count += 1 + count_subsets_helper(nums, atual, atual + 1)

        
        count += count_subsets_helper(nums, anterior, atual + 1)

        return count

    total_count = 0

    for i in range(len(nums)):
        total_count += count_subsets_helper(nums, i, i + 1)

    return total_count

print("              ")
print("#### Contagem de Subconjuntos Crescentes ####")
print("              ")

nums = [1,5,2,4]
print("Número total de subconjuntos crescentes em", nums ," :" , count_increasing_subsets(nums))
print("Número total de subconjuntos crescentes em [1, 3, 2, 4] : ", count_increasing_subsets([1, 3, 2, 4]))