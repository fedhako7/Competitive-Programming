
from collections import defaultdict

class Solution:

    def findDuplicate(self, paths):

        

        def in_between (string):

            word_start_index = string.find("(")+1

            word_end_index = string.find(")")

            return string[: word_start_index-1], string[word_start_index: word_end_index]

            

        result = defaultdict(list)

        

        for root in paths:
            

            files = root.split(" ")

            directory = files.pop(0)
            for file in files:

                path, content = in_between(file)  
                result[content].append(directory + "/" + path)

        return [value for key, value in result.items() if len(value)>1]