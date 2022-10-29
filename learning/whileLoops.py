from datetime import datetime

wait_until = datetime.now().second + 1

while datetime.now().second != wait_until:
    pass
print(f'We are at {wait_until} seconds')

# break

while True:
  if datetime.now().second == wait_until:
    print(f'We are at {wait_until} seconds')
    break

# continue

while True:
  if datetime.now().second < wait_until:
    continue
  break
print(f'We are at {wait_until} seconds')
