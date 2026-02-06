class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        duplicate_path = dict()
        path_dict = dict()

        for path in paths:
            word = path.split(" ")
            root = word[0]
            for i in range(1,len(word)):
                file_name = word[i].split("(")
                content = file_name[1]

                if content not in path_dict:
                    path_dict[content] = []
                path_dict[content].append(root + "/" + file_name[0])
            
    
        for key in path_dict:
            if len(path_dict[key]) > 1:
                duplicate_path[key] = path_dict[key]

        return list(duplicate_path.values())

                