class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        size = [1]*n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return 
            
            if size[px] > size[py]:
                parent[py] = px
                size[px] += size[py]
            else:
                parent[px] = py
                size[py] += size[px]
        
        emails = {}

        for i in range(n):
            for em in accounts[i][1:]:
                if em in emails:
                    union(i, emails[em])
                else:
                    emails[em] = i
        
        # print(emails) {'johnsmith@mail.com': 0, 'john_newyork@mail.com': 0, 'john00@mail.com': 1, 'mary@mail.com': 2, 'johnnybravo@mail.com': 3}
        # print(parent) [0, 0, 2, 3]

        final_emails = defaultdict(list)

        for em, idx in emails.items():
            p = find(idx)
            final_emails[p].append(em)
        
        # print(final_emails)

        result = []

        for key in final_emails:
            name = accounts[key][0]
            ordered = sorted(final_emails[key])
            ans = [name] + ordered
            result.append(ans)
        
        return result
