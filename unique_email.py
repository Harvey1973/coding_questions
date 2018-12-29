class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if emails == []:
            return 0
        results = {}
        for i in emails:
            email1 = i.split("@")
            #print(email1)
            valid = email1[0].split("+")[0]
            local_name = ''.join(valid.split("."))
            domain_name = email1[1]
            results[local_name +"@"+ domain_name] = valid

        print(len(results))

        return len(results)
        #for e in email1[0]:
            
         

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
obj = Solution()
obj.numUniqueEmails(emails)

