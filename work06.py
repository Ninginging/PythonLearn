import os
import work04
from collections import Counter

Directory = 'source\\DiaryFiles\\'
Diary_Files_List = os.listdir(Directory)


def statistical_words(__dir, files_list):
    for i in range(len(files_list)):
        temp_file = open(__dir+files_list[i])
        temp_string = temp_file.read()
        word_list = work04.get_words_list(temp_string)
        words_count_dict = Counter(word_list)
        print('%s当中出现次数前三多的单词和出现数量是' % Diary_Files_List[i], words_count_dict.most_common(3))
        temp_file.close()


statistical_words(Directory, Diary_Files_List)
