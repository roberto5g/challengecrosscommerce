import requests
import json
import os
import time


def extract_data():
    time_init = time.time()
    page = 1
    data = []

    print('Time init:', format(time_init))

    while True:
        print('Page number: ', page)
        response = requests.get(f'http://challenge.dienekes.com.br/api/numbers?page={page}')

        if response.status_code != 200:
            print('Error status code: ', response.status_code)
            continue

        results = response.json()['numbers']
        if len(results) == 0:
            break

        for i in results:
            data.append(i)

        page = page + 1

    print(len(data))

    path = os.getcwd()+'/data_extraction'
    
    with open(path+'/data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

    time_end = time.time()
    calc_time = time_end - time_init
    print('Time out:', format(calc_time))
