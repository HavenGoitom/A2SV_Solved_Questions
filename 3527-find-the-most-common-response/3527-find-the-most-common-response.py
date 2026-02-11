from collections import Counter

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        response_list = []
        unique_response = []

        for sublist in responses:
            unique_response.append(set(sublist))

        for sublist in unique_response:
            for word in sublist:
                response_list.append(word)

        responses_map = Counter(response_list)
        max_freq = max(responses_map.values())
        max_freq_responses = []

        for response in responses_map:
            if responses_map[response] == max_freq:
                max_freq_responses.append(response)
        
        return min(max_freq_responses)


            
