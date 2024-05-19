# Find whether a substring exists in the main string or not:
import introJitendra

introJitendra.printIntro("Find whether a substring exists in the main string or not")


def substring_exists(s, sub):
    if sub in s:
        return True
    else:
        return False


s = input("enter string : ")
sb = input("enter substring : ")

print("`", sb, "` exist in `", s, "`: ", substring_exists(s, sb))
