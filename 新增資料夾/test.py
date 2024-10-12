import re

class course:
    def __init__(self):
        self.name = input()
        hours = int(input())
        self.lessons = set()
        name_pattern = re.match(r'\D+\d{4}', self.name)
        if name_pattern is None:
            raise Exception
        if len(self.name) != len(name_pattern.group()):
            raise Exception
        if not 1<=hours<=3:
            raise Exception
        for _ in range(hours):
            lesson = input()
            if re.match(r'[1-5][a-c1-9]', lesson) is None:
                raise Exception
            elif len(lesson) != 2:
                raise Exception
            else:
                self.lessons.add(lesson)

def check(course_1:course, course_2:course)->None:
    conflict = course_1.lessons & course_2.lessons
    if conflict:

        output = f'{course_1.name},{course_2.name},{conflict}'
        outputList = [output for lesson in conflict if ]
    

if __name__ == '__main__':
    try:
        course_list = [course() for _ in range(3)]
        check(course_list)
    except Exception:
        print(-1)

