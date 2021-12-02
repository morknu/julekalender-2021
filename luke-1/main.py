import io

tall = ['femti', 'førtini', 'førtiåtte', 'førtisju', 'førtiseks', 'førtifem', 'førtifire', 'førtitre', 'førtito',
        'førtien', 'førti', 'trettini', 'trettiåtte', 'trettisju', 'trettiseks', 'trettifem', 'trettifire', 'trettitre',
        'trettito', 'trettien', 'tretti', 'tjueni', 'tjueåtte', 'tjuesju', 'tjueseks', 'tjuefem', 'tjuefire', 'tjuetre',
        'tjueto', 'tjueen', 'tjue', 'nitten', 'atten', 'sytten', 'seksten', 'femten', 'fjorten', 'tretten', 'tolv',
        'elleve', 'ti', 'ni', 'åtte', 'sju', 'seks', 'fem', 'fire', 'tre', 'to', 'en'
        ]

f = io.open('tall.txt', mode='r', encoding='utf-8')
tall_tull_str = f.read().strip()
f.close()

tall_tull_number = 0

while len(tall_tull_str) != 0:
    for index, val in enumerate(tall):
        if tall_tull_str.rfind(val) == len(tall_tull_str) - len(val) and len(tall_tull_str) - len(val) >= 0:
            tall_tull_str = tall_tull_str[:(len(tall_tull_str) - len(val))]
            tall_tull_number += 50 - index
            break
print(tall_tull_number)
