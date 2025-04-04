class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        # find the shortest string
        for i in range(len(strs)):
            if strs[i] < prefix:
                prefix = strs[i]


        for j in range(len(strs)):
            word = strs[j]

            while prefix != word[:len(prefix)]:
                prefix = prefix[:-1]

                if not prefix:
                    return ""


        return prefix
        