#Request Optimization code

import time

request = {}

LIMIT = 5
TIME_WINDOW = 60  # seconds

def is_allowed(user_id):
    current_time = time.time()

    if user_id not in request:
        request[user_id] = []
    #remove old requests
    request[user_id] = [
        t for t in request[user_id] 
        if current_time - t < TIME_WINDOW
        ]
    if len(request[user_id]) < LIMIT:
        request[user_id].append(current_time)
        return True
    else :
        return False
    
    #testing

    for i in range(7):
        print(i+1,is_allowed("user123"))