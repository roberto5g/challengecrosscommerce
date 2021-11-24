import json


def mergesort(vet, start=0, end=None):
    if end is None:
        end = len(vet)
    if end - start > 1:
        middle = (end + start)//2
        mergesort(vet, start, middle)
        mergesort(vet, middle, end)
        merge(vet, start, middle, end)


def merge(vet, start, middle, end):
    left = vet[start:middle]
    right = vet[middle:end]
    top_left, top_right = 0, 0
    for k in range(start, end):
        if top_left >= len(left):
            vet[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            vet[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            vet[k] = left[top_left]
            top_left = top_left + 1
        else:
            vet[k] = right[top_right]
            top_right = top_right + 1


def attach(data):
    print('Start attach process')
    try:
        with open('../data_transformation/data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
    except Exception as inst:
        print(f'attach {inst}')


def ordering():
    print('Start ordering process')
    try:
        with open('../data_extraction/data.json') as file:
            data = json.load(file)
            mergesort(data)
            attach(data)
    except Exception as inst:
        print(f'ordering {inst}')
