def triangle(rows:int):
    return list(reversed(revTriangle(rows)))

def revTriangle(rows:int):
    output_list = list()
    for r in range(rows):
        output = '#'*r + '*'*(2*rows-1-2*r) + '#'*r
        output_list.append(output if output else '')
    return output_list

def rhombus(rows:int):
    output = triangle(rows//2+1)[:-1] + revTriangle(rows//2+1)
    return [row.replace('#',' ') for row in output] 

def fish(rows:int):
    body = rhombus(rows)
    tale = [' '*(rows//2-r) + '-'*r for r in range(rows//2+1)]
    tale = tale[:-1] + list(reversed(tale))
    return [body[i] + tale[i] for i in range(rows)]

def main():
    graph, rows = int(input()), int(input())
    if not(rows%2 == 1 and 3<=rows<=49):
        return print('error')
    draw = {1:triangle(rows), 2:revTriangle(rows), 3:rhombus(rows), 4:fish(rows)}
    for string in draw[graph]:
        print(string)

if __name__ == '__main__':
    main()