import requests
import csv
import time
def get_data(offset, kode_ref_pend, pengadaan_kd):
    # https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend=5191063&pengadaan_kd=2&offset=0

    # {
    # "status": 200,
    # "error": false,
    # "message": "Success",
    # "data": {
    #     "meta": {
    #         "total": 2420
    #     },
    #     "page": {
    #         "total": 10
    #     },
    #     "data": [
    #         {
    #             "formasi_id": "4340f7e3-aca4-441a-8104-424d3bee7a60",
    #             "ins_nm": "Badan Informasi Geospasial",
    #             "jp_nama": "CPNS",
    #             "formasi_nm": "UMUM",
    #             "jabatan_nm": "MANGGALA INFORMATIKA AHLI PERTAMA",
    #             "lokasi_nm": "Badan Informasi Geospasial | DEPUTI BIDANG INFRASTRUKTUR INFORMASI GEOSPASIAL | DIREKTORAT STANDAR DAN TEKNOLOGI INFORMASI GEOSPASIAL",
    #             "jumlah_formasi": 1,
    #             "disable": 1,
    #             "gaji_min": "5500000",
    #             "gaji_max": "7800000"
    #         },
    #     GET /2024/portal/spf?kode_ref_pend=5191063&pengadaan_kd=2&offset=0 HTTP/1.1
    # Accept: application/json, text/plain, */*
    # Accept-Encoding: gzip, deflate, br, zstd
    # Accept-Language: en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7
    # Cache-Control: no-cache
    # Connection: keep-alive
    # Host: api-sscasn.bkn.go.id
    # Origin: https://sscasn.bkn.go.id
    # Pragma: no-cache
    # Referer: https://sscasn.bkn.go.id/
    # Sec-Fetch-Dest: empty
    # Sec-Fetch-Mode: cors
    # Sec-Fetch-Site: same-site
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
    # sec-ch-ua: "Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"
    # sec-ch-ua-mobile: ?0
    # sec-ch-ua-platform: "macOS"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'api-sscasn.bkn.go.id',
        'Origin': 'https://sscasn.bkn.go.id',
        'Pragma': 'no-cache',
        'Referer': 'https://sscasn.bkn.go.id/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    response = requests.get(
        f'https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend={kode_ref_pend}&pengadaan_kd={pengadaan_kd}&offset={offset}',
        headers = headers
    )
    return response.json()

if __name__ == '__main__':
    timestamp = time.time()
    with open(f'data-{timestamp}.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Instansi', 'Formasi', 'Jabatan', 'Unit Kerja', 'Jumlah Kebutuhan', 'Gaji Min', 'Gaji Max', "Link"])
        pass
    for i in range(0, 2420, 10):
        kode_pendidikan = '5191063'
        kode_pengadaan = '2'
        data = get_data(i, kode_pendidikan, kode_pengadaan)
        with open(f'data-{timestamp}.csv', mode='a') as file:
            writer = csv.writer(file)
            for item in data['data']['data']:
                formasi = str(item['jp_nama']) + ' ' + str(item['formasi_nm'])
                instituisi = item['ins_nm'].replace(',', '-')
                writer.writerow([instituisi, formasi, item['jabatan_nm'], item['lokasi_nm'], str(item['jumlah_formasi']), item['gaji_min'], item['gaji_max'], 'https://sscasn.bkn.go.id/detailformasi/' + item['formasi_id']])
    
    print('Done')
            