from collections import deque 

def calculate_capital_gain(transactions):
    fifo_queue = deque() # Creating a deque to simulate the FIFO protocol
    capital_gain = 0

    for transaction in transactions:
        if transaction.startswith('buy'):
            _, shares, price = transaction.split()
            fifo_queue.append(int(shares), int(price))
        elif transaction.startswith('sell'):
            _, shares, price = transaction.split()
            remaining_shares = int(shares)

            while remaining_shares > 0: # Continue selling shares until there are none left
                if not fifo_queue:
                    raise ValueError('Not enough shares to sell.')
                
                oldest_shares, stock_price = fifo_queue[0]

                if oldest_shares <= remaining_shares:
                    fifo_queue.popleft() # Remove the oldest shares from the queue
                    capital_gain += oldest_shares * (int(price) - stock_price)
                    remaining_shares -= oldest_shares
                else:
                    capital_gain += remaining_shares * (int(price) - stock_price)
                    fifo_queue[0] = (oldest_shares - remaining_shares, stock_price)
                    remaing_shares = 0

    return capital_gain
transactions = ["buy 100 20",
                "buy 20 24",
                "buy 200 36",
                "sell 150 30"]

total_capital_gain = calculate_capital_gain(transactions)
print("Total Capital Gain/Loss:", total_capital_gain)