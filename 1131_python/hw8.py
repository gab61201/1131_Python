import re

def new_course()->dict:
    course_dict = {'name':input(), 'lessons':set()}
    for _ in range(int(input())):
        lesson = input()
        if re.match(r'[1-5][a-c1-9]', lesson) and len(lesson) == 2:
            course_dict['lessons'].add(lesson)
        else:
            raise Exception
    return course_dict

def conflict(courses:list): 
    conflictList = list()
    for index_1, course_1 in enumerate(courses):
        for course_2 in courses[index_1+1:]:
            lessonSet = course_1['lessons'] & course_2['lessons']
            conflictList.extend([f'{course_1["name"]},{course_2["name"]},{lesson}' for lesson in lessonSet])
    for output in conflictList or ['correct']:
        print(output)
        
if __name__ == '__main__':
    try:
        courseList = [new_course() for _ in range(3)]
        conflict(courseList)
    except:
        print(-1)