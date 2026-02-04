class Solution(object):
    def removeComments(self, source):
        cleaned_code = []
        current_comment = " "  
        current_index = -1 
        last = -1

        for idx, code in enumerate(source):
            arr = []
            join_them = False
            i = 0
            while i < len(code):
                two_chars = code[i:i+2]

                if two_chars == '*/' and current_comment == '/*':
                    if current_index != idx:
                        join_them = True
                    current_comment = " "
                    i += 2
                    continue

                if current_comment == '/*':
                    i += 1
                    continue

                if two_chars == '/*':
                    current_comment = '/*'
                    current_index = idx
                    i += 2
                    continue

                if two_chars == '//':
                    break

                arr.append(code[i])
                i += 1

            if arr:
                if join_them and current_index == last:
                    cleaned_code[-1] += "".join(arr)
                else:
                    cleaned_code.append("".join(arr))
                    last = idx

        return cleaned_code
