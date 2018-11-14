# users = [
#     {
#         'username':'abc',
#         'password': 'abc123'
#     },
#     {
#         'username':'abcd',
#         'password': 'abcd123'
#     }
# ]

# print(users[1]['username'])
# users.append({'username':'lalu','password':'123'})
# print(users)
# print(users[2]['password'])
kursus = {
    'nama': 'Python Basic',
    'jml_peserta': 2,
    'peserta': [
        {
            'nama': 'Komaril',
            'pekerjaan': 'Mahasiswa'
        },
        {
            'nama': 'Oonk',
            'pekerjaan': 'Mahasiswa'
        }
    ],
}


# kursus.append('peserta':{'name':'hai','work':'programmer'})
# kursus['peserta']={'name':'hai','work':'programmer'}
kursus.update({'peserta':{'name':'hai','work':'programmer'}})

# Belum bisa menambah value peserta
