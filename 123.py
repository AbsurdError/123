

# //////// 2 задача //////

# def list_insert(ref_list, start, num, rep):
#     return ref_list[:start] + [num]*rep + ref_list[start:] if len(ref_list) >= start else -1
# print(*list_insert([int(i) for i in input('tab  ').split()], int(input('start:  ')), int(input('num:  ')), int(input('rep:  '))))

# /// 1 задача ///
# def de_none(lst):
#     return [val for val in lst if val is not None]
#
# lst = input("Введите список значений через пробел: ").split()
# lst = [eval(val) if val != "None" else None for val in lst]
#
# result = de_none(lst)
# print(*result)
