"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
phones = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        phones.add(text[0])
        phones.add(text[1])
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telemarketers = set()
    for call in calls:
        phones.add(call[1])
    for call in calls:
        phone = call[0]
        if phone not in phones:
            telemarketers.add(phone)
    print("These numbers could be telemarketers: \n{}".format("\n".join(sorted(telemarketers))))
"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

