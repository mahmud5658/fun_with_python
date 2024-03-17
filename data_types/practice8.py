def regenerate_sorted(data):
    sorted_list = sorted(data,reverse=True)
    return sorted_list

number = list((1,2,3,4,5,6))

new_list=regenerate_sorted(number)

print(new_list)