def tresaurs(*names):
    dict_1 = dict()
    for name in names:
        dict_1.setdefault(name[0], [])
        dict_1[name[0]].append(name)
    return dict_1

print(tresaurs('Андрей', 'Алексей', 'Михаил', 'Галина'))