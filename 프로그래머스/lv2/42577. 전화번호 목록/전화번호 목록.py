def solution(phone_book):
    phone = {}
    for i in phone_book:
        phone[f'{i}'] = 1
    
    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            value = phone.get(f"{phone_book[i][:j]}")
            if value != None:
                return False
                
    return True