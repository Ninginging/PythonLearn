import os

INIT_STRING = 'ABCDEFGHIJKLMNOPQISTUVWXYZabcdefghijklmnopqrstuvwxyz\'-'

Statistical_File = open('source\\CountWords.txt', 'r', encoding='utf-8')
Temp_String = Statistical_File.read()


def get_words_list(word_str):
    temp_word = ''
    string_index = 0
    word_list = []
    while string_index < len(word_str):
        if word_str[string_index] in INIT_STRING:
            temp_word += word_str[string_index]
        elif temp_word != '':
            word_list.append(temp_word)
            temp_word = ''
        string_index += 1
    return word_list


# def get_statistical_dict(word_list):  # 传入排好顺序的列表,传出键为列表元素,值为元素出现个数的字典
#     temp_dict = {}
#     list_index = 0
#     while list_index < len(word_list)-1:
#         if word_list[list_index] != word_list[list_index + 1]:
#             temp_dict[word_list[list_index]] = word_list.count(word_list[list_index])
#         list_index += 1
#     return temp_dict


Word_list = get_words_list(Temp_String)
Word_Num = len(Word_list)
# Word_list.sort()  # 列表排序
# print(Word_list)
# print(Word_Num)


Statistical_File.close()


