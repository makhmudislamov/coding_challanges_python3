
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
		# transforming each line into list with 5 elements: 
		# Format >> ['[ERROR]', '500', 'Server', 'Error:', 'int is not subscriptable']
		separated_log = logs[data_index].split(' ', 4)
	
		print('list:', separated_log)
		data_index += 1

		inner_index = 0
		while inner_index < len(separated_log):
			log_type = separated_log[inner_index]
			log_code = separated_log[inner_index + 1]
			slice_start = separated_log.index(log_code) + 1
			# print('slice start', slice_start)
			log_status = separated_log[slice_start:len(separated_log)-1]
			log_message = separated_log[len(separated_log)-1]
			stat_dict[log_type] = {} 
			stat_dict[log_type][log_code] = {} 
			stat_dict[log_type][log_code][separated_log[inner_index + 2]] = {}
			# print(log_type, log_code, log_status, log_message)
			# TODO: list: ['[WARNING]', '403', 'Forbidden:', 'No', 'token in request parameters'] - find better way to split it
			break
	# 		if log_part not in stat_dict:
	# 			stat_dict[log_part] = 1
	# 		else:
	# 			stat_dict[log_part] += 1

	return stat_dict

	
		


	print(stat_dict)
	# print(stat_key_part)
	# print(separated_log)


test_data = [
    '[WARNING] 403 Forbidden: No token in request parameters',
    '[ERROR] 500 Server Error: int is not subscriptable',
    '[INFO] 200 OK: Login Successful',
    '[INFO] 200 OK: User sent a message',
    '[ERROR] 500 Server Error: int is not subscriptable'
]



print(log_stats(test_data))
