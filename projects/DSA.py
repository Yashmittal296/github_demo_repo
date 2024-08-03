class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        list_s = list(s)
        if set(list_s).issubset(set(dict_roman.keys())):
            if 1 <= len(s) <= 15:

                ans = 0
                for i in range(0, len(list_s)):
                    if i == len(s) - 1:
                        ans = ans + dict_roman[list_s[i]]
                    else:
                        num1 = dict_roman[list_s[i]]
                        num2 = dict_roman[list_s[i + 1]]
                        if num1 < num2:
                            temp = num2 - num1
                            ans = ans + temp
                            i += 2
                        else:
                            ans = ans + num1

                print(ans)


Solution().romanToInt(s='MCM')
