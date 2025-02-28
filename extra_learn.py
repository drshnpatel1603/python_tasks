# # class demo:
# #     @classmethod
# #     def extra(cls):
# #         print(cls)
# #
# # class demo1(demo):
# #     # @classmethod
# #     # def extra(cls):
# #     #     print(cls)
# #     pass
# #
# # # d = demo()
# # # d.extra()
# #
# # # d1 = demo1()
# # demo.extra()
#
#
# class A:
#     @classmethod
#     def key_fn(cls, id):
#         raise NotImplementedError('')
#
#     @classmethod
#     def load_all(cls):
#         return cls.key_fn("foo")
#
# class B(A):
#     @classmethod
#     def key_fn(cls, id):
#         return f'/keys/{id}'
#
# print(B.load_all())

# dict1 = {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Machine Learning']}
# dict2 = {'city': 'New York', 'is_active': True, 'hobby': 'Reading'}
#
# print({**dict1,**dict2})

d = {"drshn" : {"python" : (20,20), "java" : (30,10)}}
name = "drshn"
book = "java"

d[name].update({"sql" : (10,10)})
# del d[name][book]
print(d)

