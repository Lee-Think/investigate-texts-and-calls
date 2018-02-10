"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
count = 0
s = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        if text[0] not in s:
            s.add(text[0])
        if text[1] not in s:
            s.add(text[1])
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        if call[0] not in s:
            s.add(call[0])
        if call[1] not in s:
            s.add(call[1])

print("There are {} different telephone numbers in the records.".format(str(len(s))))
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
