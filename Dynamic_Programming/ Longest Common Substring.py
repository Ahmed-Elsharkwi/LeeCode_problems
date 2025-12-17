def lcs(str1: str, str2: str) -> int:
    # write your code here
    prev = [0] * (len(str2) + 1)
    ans = 1

    for index in range(1, len(str1) + 1):
        post = [0] * (len(str2) + 1)
        
        for idx in range(1, len(str2) + 1):
            if str1[index - 1] == str2[idx - 1]:
                post[idx] = prev[idx - 1] + 1
                ans = max(ans, post[idx])
            else:
                post[idx] = 0
        prev = post

    return ans
        
