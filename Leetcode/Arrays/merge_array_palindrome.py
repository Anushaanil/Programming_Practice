def merge_array_palindrome(arr):
    c =0
    i,j = 0,len(arr)-1

    if arr == arr[::-1]:
        return 0

    else:
        while i<=j:
            if arr[i]==arr[j]:
                i+=1
                j-=1
            elif arr[i]>arr[j]:
                j-=1
                arr[j] = arr[j]+arr[j+1]
                c+=1
                #print(j,arr,c)
            else:
                i+=1
                arr[i] = arr[i]+arr[i+1]
                c+=1
                #print(i,arr,c)
        return c


arr = [11, 14, 15, 11]
print(merge_array_palindrome(arr))