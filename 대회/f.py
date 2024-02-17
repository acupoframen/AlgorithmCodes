def kmp_search(text, patterns):
    """
    Searches for all patterns in the given text using the KMP algorithm.
    """
    def build_lps(pattern):
        """
        Builds the Longest Prefix Suffix (LPS) array for the KMP algorithm.
        """
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    def match(pattern, text):
        lps = build_lps(pattern)
        j = 0
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                return True
        return False

    substrings = set()
    for pattern in patterns:
        for i in range(len(text)):
            if match(pattern, text[i:]):
                substrings.add(text[i:i+len(pattern)])
    return substrings

# Example usage
if __name__ == "__main__":
    text = "raararaara"
    patterns = ["ra", "aa", "ar"]
    substrings = kmp_search(text, patterns)
    print("Substrings found:", substrings)
