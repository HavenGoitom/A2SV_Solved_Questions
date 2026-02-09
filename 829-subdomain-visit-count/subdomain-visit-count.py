class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        output = []
        domains_counter = defaultdict(int)

        for entry in cpdomains:
            count_str, full_domain = entry.split(" ")
            visit_count = int(count_str)

            parts = full_domain.split(".")
            subdomain = ""

            for i in range(len(parts) - 1, -1, -1):
                if subdomain == "":
                    subdomain = parts[i]
                else:
                    subdomain = parts[i] + "." + subdomain

                domains_counter[subdomain] += visit_count

        for key, value in domains_counter.items():
            output.append(str(value) + " " + key)

        return output
