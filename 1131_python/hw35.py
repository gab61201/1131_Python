def match(school: list[dict], scearch: set[frozenset]) -> tuple[list]:
    for s in school:
        for case in scearch:
            matching = s["attribute"] & case
            s["full_match"] = (matching == case) or s.get("full_match", False)
            s["partial_match_lenth"] = len(matching) + s.get("partial_match_lenth", 0)

    full_match_school = [s["name"] for s in school if s["full_match"]]
    max_partial_match = max(school, key=lambda x: x["partial_match_lenth"])
    partial_match_school = [
        s["name"] for s in school
        if s["partial_match_lenth"] == max_partial_match["partial_match_lenth"]
    ]

    for s in school:
        del s["full_match"], s["partial_match_lenth"]

    return full_match_school, partial_match_school


def main():
    school = []
    for _ in range(int(input())):
        input_list = input().split()
        school.append({"name": input_list[0], "attribute": set(input_list[1:])})

    scearch_list = []
    for _ in range(int(input())):
        input_list = input().split("+")
        scearch = {frozenset(attribute.split()) for attribute in input_list}
        scearch_list.append(match(school, scearch))

    output_type = int(input())
    for output in scearch_list:
        print(" ".join(output[output_type]))


main()
