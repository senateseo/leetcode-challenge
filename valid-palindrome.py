class Solution:
    def isPalindrome(self, s: str) -> bool:
        output=''
        for character in s:
            if character.isalnum():
                output+=character
        output=output.lower()

        return output==output[::-1]