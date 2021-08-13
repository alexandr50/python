def thesaurus(*kwargs):
    dict = {}
    for kwarg in kwargs:
        for i in kwarg:
            if i == kwarg[0]:
                dict[i] = kwarg



    print(dict)
thesaurus('Иван', 'Андрей','Михаил','Егор','Алексей')