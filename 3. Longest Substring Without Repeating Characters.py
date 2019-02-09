class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # abcab
        # seroksrthor
        # bbiacdkbtuicdfegrfeg
        # abcdefghijklmnopqwerstuvwabxyzcdefgeh
        # 첫번째 문자를 선두로 substring 찾기.
        if len(s) == 0:
            return 0
        longest_length = 1

        for start in range(len(s)):
            end = start + 1
            temp_length = 1
            if (longest_length >= len(s) - start):
                return longest_length

            while end < len(s):
                if not s[end] in s[start:end]:
                    temp_length += 1
                    end += 1
                else:
                    break

            if temp_length > longest_length:
                longest_length = temp_length
