def check(string: str, target_deep):
    parentheses = {"{": "}", "[": "]", "(": ")"}
    queue = []
    deep = 0
    output = ""
    for char in string:
        if char in parentheses.keys():  # 左括號
            queue.append(char)
            deep += 1
        elif char in parentheses.values():  # 錯誤右括號
            if len(queue) == 0:
                return "fail"
            if char == parentheses[queue.pop()]:
                deep -= 1
            else:
                return "fail"
        elif deep == target_deep:
            output += char
    if deep:
        return "fail"
    return f"pass, {output if output else 'EMPTY'}"


def main():
    string_num = int(input())
    target_deep = int(input())
    string_list = [input() for _ in range(string_num)]
    output_list = [check(string, target_deep) for string in string_list]
    for output in output_list:
        print(output)


main()
