amount = int(input('Eneter withdrawal amount: '))

note1 = amount//100
note2 = (amount%100)//50
note3 = (amount%100)%50//10

print("note of 100 dollars are", note1)
print("note of 50 dollars are", note2)
print("note of 10 dollars are", note3)