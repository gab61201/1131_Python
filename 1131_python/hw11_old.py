from math import ceil

def get_input()->dict:
    books = dict()
    books['A'] = [int(string) for string in input().split(',')]+[380]
    books['B'] = [int(string) for string in input().split(',')]+[1200]
    books['C'] = [int(string) for string in input().split(',')]+[180]
    return books

def print_price(books:dict):
    for title, num_list in books.items():
        #將字典value由串列改為金額(int)
        if num_list[0] <= 10:
            books[title] = ceil(num_list[0]*num_list[-1])
        elif num_list[0] <= 20:
            books[title] = ceil(num_list[0]*num_list[-1]*num_list[1]/100)
        elif num_list[0] <= 30:
            books[title] = ceil(num_list[0]*num_list[-1]*num_list[2]/100)
        else:
            books[title] = ceil(num_list[0]*num_list[-1]*num_list[3]/100)
    for book in sorted(books, key=books.get, reverse=True):
        print(f'{book},{books[book]}')
    print(sum(books.values()))

if __name__ == '__main__':
    books_dict = get_input()
    print_price(books_dict)