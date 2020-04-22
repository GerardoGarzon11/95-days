bills = [100, 20, 10, 5, 1]

dollars = int(input())
bills_to_receive = 0

for bill in bills:
	if dollars >= bill:
		bills_to_receive += dollars // bill
		dollars -= (dollars // bill) * bill

print(bills_to_receive)
