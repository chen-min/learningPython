import json
# python下的json模块
#json.loads >>> 把json字符串转为对应的python数据结构
# json_str = '{"name": "qiyue", "age":18}'
# student = json.loads(json_str)
# print(type(student))  # 数据类型为字典
# print(student)

#JSON  可以为object  也可以为array
json_str = '[{"name": "qiyue", "age":18}, {"name": "qiyue", "age":18}]'
student = json.loads(json_str)
print(type(student))  # 数据类型为list
print(student)
#[{'name': 'qiyue', 'age': 18}, {'name': 'qiyue', 'age': 18}]

