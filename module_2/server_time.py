"""
You are in charge of a server that needs to run some submitted tasks on a first-come, first-served basis. Each day, you can dedicate the server to run these tasks for at most T minutes. Given the time each task takes, you want to know how many of them will be finished today.

Consider the following example:

Assume T=180 and the tasks take 45, 30, 55, 20, 80 and 20 minutes (in the order that they are submitted). Then, only four tasks can be completed. The first four tasks can be completed because they take 150 minutes, but not the first five, because they take 230 minutes which is greater than 180. Notice that although there is enough time to perform the sixth task (which takes 20 minutes) after completing the fourth task, you cannot do that because the fifth task is not done yet.


Input

The input consists of a two lines. 

The first line contains two integers n and T.
1 ≤ n ≤ 50 is the number of tasks 
1 ≤ T ≤ 500 is the total amount of execution time available. 

The second line contains n positive integers, separated by spaces, smaller than 100, indicating how long each task takes in order they are submitted (the same order they must be evaluated in).
1 < n < 100 - the input looks like this:
n n n n n 

Output
Display (by printing) the number of tasks that can be completed in T minutes on a first-come, first-served basis.
"""


def server_time_check(task_config, task_times):
    # PSEUDOCODE
    
    # declare competed variable = 0
    completed_tasks = 0
    # total_time variable = task_config[1:]
    times_required = []
    time_left = int(task_config[1:]) # works
    # print(times_required)
    # keep the task_times in the array
    # TODO: converting task_times into int
    times_required.append(task_times)
    # iterate over the task_times array:
    while time_left <= 0:
        for time in times_required:
        # start substracting each index item from T (use sys.arg[:1] - try) >> time_left variable
            time_left -= time
        # after each substraction completed += 1
            completed_tasks += 1
            # if  time_left <= 0:
        return completed_tasks
#   print(task_config[1:])


## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input(
    "Please input the number of tasks, and the maximum total execution time:")
task_times = input(
    "Please input the execution times of each task, seperated with a space:")

server_time_check(task_config, task_times)
