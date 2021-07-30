# monthly expenses
expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
diff = expense[1] - expense[0]
print(f'1. Diff = {diff}')

# 2. Find out your total expense in first quarter (first three months) of the year.
total_fst_qtr = expense[0] + expense[1] + expense[2]
print(f'2. Total first qtr = {total_fst_qtr}')

# 3. Find out if you spent exactly 2000 dollars in any month
print(f'3. Spent = {2000 in expense}')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(f'4. New expense array = {expense}')

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense[3] = expense[3] - 200
print(f'5. Updated expense = {expense}')
