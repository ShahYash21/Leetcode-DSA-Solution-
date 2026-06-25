class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in (s+s)
        """
        also do it below way(after 4 th line)
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False      
        """
