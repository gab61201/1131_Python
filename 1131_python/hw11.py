from math import ceil

def new_book(name:str, price:int)->dict:  # 創建一個字典，內容為書本的購買資訊
    input_list = [int(string) for string in input().split(',')]
    return {'name': name, 'price': price, 'amount': input_list.pop(0), 'sales': input_list}

def total_price(book:dict)->int:  # 傳入書本dict，回傳計算完的總價
    price = book['amount']*book['price']
    if book['amount'] <= 10:
        return ceil(price)
    elif book['amount'] <= 20:
        return ceil(price*book['sales'][0]/100)
    elif book['amount'] <= 30:
        return ceil(price*book['sales'][1]/100)
    else:
        return ceil(price*book['sales'][2]/100)

if __name__ == '__main__':
    book_list = [new_book('A',380), new_book('B',1200), new_book('C',180)]  # 建立一個含有多個書本dict的list
    book_list = sorted(book_list, key=total_price, reverse=True)  # 以書本的總價排列list
    for book in book_list:
        print(f'{book["name"]},{total_price(book)}')
    print(sum([total_price(book) for book in book_list]))