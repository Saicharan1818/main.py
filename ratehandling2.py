import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity        
        self.refill_rate = refill_rate    
        self.tokens = capacity            
        self.last_refill = time.time()

    def allow(self):
        current_time = time.time()
        #refill tokens based on elapsed time

        elapsed = current_time - self.last_refill
        added_tokens = elapsed * self.refill_rate
        if added_tokens > 0:
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            self.last_refill = current_time

    def consume(self, tokens=1):
        self.allow()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        else:
            return False
if __name__ == "__main__":
    bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 tokens max, 1 token/sec

    print("Sending 10 requests...\n")
    for i in range(10):
        if bucket.consume():
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Blocked (Not enough tokens)")
        time.sleep(0.5)