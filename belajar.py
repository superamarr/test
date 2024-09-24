awal = 5000
deposit = int(input ('mau deposit berapa?'))
hutang = 50_000

if deposit < hutang:
    print ('maaf saldo anda tidak cukup untuk melanjutkan pembayaran')

else:
    saldo_akhir = awal + deposit - hutang
    print ('YEAYYY PEMBAYARAN BERHASILL')
    print ('saldo kamu sekarang adalah ' + str(saldo_akhir))