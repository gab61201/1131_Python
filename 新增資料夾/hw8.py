import re

class course:
    def __init__(self):
        self.name = input()
        hours = int(input())
        self.lessons = list()
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
                self.lessons.append(lesson)

def conflict(course:list)->None:
    isCorrect = True
    for lesson in course[0].lessons:
        if lesson in course[1].lessons:
            print(f'{course[0].name},{course[1].name},{lesson}')
            isCorrect = False
        if lesson in course[2].lessons:
            print(f'{course[0].name},{course[2].name},{lesson}')
            isCorrect = False
    for lesson in course[1].lessons:
        if lesson in course[2].lessons:
            print(f'{course[1].name},{course[2].name},{lesson}')
            isCorrect = False
    if isCorrect:
        print('correct')

if __name__ == '__main__':
    try:
        course_list = [course() for _ in range(3)]
        conflict(course_list)
    except Exception:
        print(-1)