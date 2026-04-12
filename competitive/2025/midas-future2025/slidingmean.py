import collections
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    idx = 1
    sym_data = {}
    
    results = []
    
    for _ in range(N):
        ts = int(input_data[idx])
        symbol = input_data[idx+1]
        price = int(input_data[idx+2])
        idx += 3
    
        if symbol not in sym_data:
            sym_data[symbol] = [collections.deque(), 0.0]
        
        queue, current_sum = sym_data[symbol]
        
        queue.append((ts, price))
        current_sum += price
        
        limit = ts - 60000
        while queue and queue[0][0] < limit:
            old_ts, old_price = queue.popleft()
            current_sum -= old_price

        sym_data[symbol][1] = current_sum
        
        mean_price = current_sum / len(queue)
        results.append(f"{mean_price:.10f}")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()


"""Input: 8
1766822400000 BTC 93824
1766822400001 ETH 3371
1766822400999 BTC 93823
1766822460500 BTC 93829
1766822460501 ETH 3379
1766822460502 ETH 3390
1766822460503 ETH 3310
1766822460505 BTC 93000


Output: 93824
3371
93823.5
93826
3379
3384.5
3359.6666666667
93550.6666666667 """