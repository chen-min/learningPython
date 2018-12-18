import json
student  = [
                {"name": "qiyue", "age":18, "flag": False},
                {"name": "qiyue", "age":18},

            ]
json_str  = json.dumps(student)
print(type(json_str)) #<class 'str'>
print(json_str)
# [{"name": "qiyue", "age": 18, "flag": false}, {"name": "qiyue", "age": 18}]


JSON对象  JSON  JSON字符串区别?

