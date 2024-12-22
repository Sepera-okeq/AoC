with open('input (21).txt', 'r') as file:
    secret_numbers = list(map(int, file.readlines()))

sequences_sells = {}

for secret_number in secret_numbers:
    secret_nums = [secret_number]
    for _ in range(2000):
        secret_number = (secret_number ^ (secret_number * 64)) % 16777216
        secret_number = (secret_number ^ (secret_number // 32)) % 16777216
        secret_number = (secret_number ^ (secret_number * 2048)) % 16777216
        secret_nums.append(secret_number)

    prices = [num % 10 for num in secret_nums]

    price_diffs = [prices[i+1] - prices[i] for i in range(len(prices)-1)]

    buyer_sequences = {}
    for i in range(len(price_diffs) - 3):
        seq = (price_diffs[i], price_diffs[i+1], price_diffs[i+2], price_diffs[i+3])
        if seq not in buyer_sequences:
            buyer_sequences[seq] = prices[i+4]

    for seq, sell_price in buyer_sequences.items():
        if seq not in sequences_sells:
            sequences_sells[seq] = sell_price
        else:
            sequences_sells[seq] += sell_price

max_bananas = 0
best_sequence = None
for seq, total_sell_price in sequences_sells.items():
    if total_sell_price > max_bananas:
        max_bananas = total_sell_price
        best_sequence = seq

print(max_bananas)