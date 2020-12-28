n, m = map(int, input().split()) #카드가 N행 M열로 이루어짐

cards = []
min_list = []
for i in range(n):
    card_list = list(map(int, input().split())) #M개 카드
    cards.append(card_list)

for i in range(n):
    min_list.append(min(cards[i]))

result = max(min_list)

print(result)