
"""
You are given a stream of logging statements for a server as a list. Your product manager wants to know what categories of error are the most common, as well as what errors in the most common categories are the most common. 

Here are a few log lines, each is a string structured similarly to this:
[
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 Login Successful',
'[INFO] 200 User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]

Return a dictionary with logging statistics, that is formatted like so ( don't worry about spacing or formatting, only the data matters )
 
{
	'WARNING': {
		'403': {
			'Forbidden': {
				'No token in request parameters': 1
			}
		}
	},
	'ERROR': {
		'500': {
			'Server Error': {
				'int is not subscriptable': 2
			}
		}
	},
	'INFO': {
		'200': {
			'OK': {
				'Login Successful': 1,
				'User sent a message': 1
			}
		}
	}
}
"""


def log_stats(logs):
    
	stat_dict = {}

	data_index = 0

	while data_index < len(logs):
		# transforming each line into list
		separated_log = logs[data_index].split(' ')
		one_stat_index = 0
		stat_part = separated_log[one_stat_index]
		# 'WARNING': {}
		stat_dict[stat_part] = {
			separated_log[one_stat_index + 1]: {separated_log[one_stat_index + 2]: {}}}



		# while one_stat_index < len(separated_log):
		# 	stat_part = separated_log[one_stat_index]
		# 	# 'WARNING': {}
		# 	stat_dict[stat_part] = {}
		# 	# 'WARNING': { '403': {}


		# 	# if stat_dict.get(stat_part):
		# 	# 	stat_dict[stat_part] += 1
		# 	# else:
		# 	# 	stat_dict[stat_part] = 1
		# 	one_stat_index += 1	
		data_index +=1


	print(stat_dict)


test_data = [
    '[WARNING] 403 Forbidden: No token in request parameters',
    '[ERROR] 500 Server Error: int is not subscriptable',
    '[INFO] 200 OK: Login Successful',
    '[INFO] 200 OK: User sent a message',
    '[ERROR] 500 Server Error: int is not subscriptable'
]



print(log_stats(test_data))
