# import time

# count_seconds = 10
# for i in reversed(range(count_seconds + 1)):
# 	if i > 0:
# 		print(i, end='>>>', flush = True)
# 		time.sleep(1)
# 	else:
# 		print('Start')

import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>')
		time.sleep(1)
	else:
		print('Start')
