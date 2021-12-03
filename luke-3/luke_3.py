

f = open('input.txt', mode='r', encoding='utf-8')
gift_list = f.read().strip()
f.close()


index_neighborhood = -1
size_neighborhood = -1

slice_index = 0
slice_size = 2


while slice_size + slice_index <= len(gift_list):
    while slice_size + slice_index <= len(gift_list):
        gift_list_slice = gift_list[slice_index:slice_size + slice_index]
        yay = gift_list_slice.count('J')
        nay = gift_list_slice.count('N')
        if yay == nay and yay + nay > size_neighborhood:
            size_neighborhood = yay + nay
            index_neighborhood = slice_index
        slice_size += 2
    slice_size = 2
    slice_index += 1

print(size_neighborhood, ', ', index_neighborhood)






