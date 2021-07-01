import os
import work04
from collections import Counter

Directory = 'source\\DiaryFiles\\'
Diary_Files_List = os.listdir(Directory)


def statistical_words(__dir, files_list):
    for i in range(len(files_list)):
        temp_file = open(__dir + files_list[i])
        temp_string = temp_file.read()
        word_list = work04.get_words_list(temp_string)
        words_count_dict = Counter(word_list)
        statis_results = words_count_dict.most_common(3)
        print('%s当中出现次数最多的单词是:%s,出现数量是:%s' % \
              (Diary_Files_List[i], statis_results[0][0], statis_results[0][1]))
        temp_file.close()


statistical_words(Directory, Diary_Files_List)
