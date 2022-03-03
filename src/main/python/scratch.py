final = {}
data = [['10/03/2022', 3000.0], ['20/02/2022', 538500.0], ['22/02/2022', 5000.0]]
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


for i in data:
    key = i[0][3:]
    if key in final:
        final[key] = final.get(key) + i[1]
    else:
        final[key] = i[1]

for _, v in enumerate(final):
    print(v, final[v])
