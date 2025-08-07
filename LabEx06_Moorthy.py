def balancedParanthesis(givenExp):
    stack = []
    open = "([{"
    close = "}])"
    matched = {")":"(", "]":"[", "}":"{"}

    for char in givenExp:
        if char in open:
            stack.append(char)
        elif char in close:
            if not stack or stack[-1] != matched[char]:
                #print("Unbalanced")
                return "Unbalanced"
            stack.pop()

    if not stack:
        return "Balanced"
    else:
        return "Unbalanced"


def main():

    print(balancedParanthesis("{[]{()}}"))
    print(balancedParanthesis("[{}{}(]"))


main()
