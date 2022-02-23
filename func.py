def count_letter(list, letter):
    sum = 0
    for word in list:
        # for char in word:
        #     if char == letter:
        if letter in word:
               sum += 1
    return sum

sum = count_letter(['python', 'c++', 'c', 'scala', 'jacva'], "c")
print(sum)