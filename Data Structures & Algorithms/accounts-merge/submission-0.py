from collections import defaultdict
'''
Based on union-find. Combine 'account's based on whether they have emails in common.
First, assume each account belongs to a different person. assign account numbers 0 to n-1 for the accounts. 
Create a dict meant to map email IDs to account numbers.
Then, iterate through the emails of each account, and if the email already exists in the dict, it means
another accNo also had the email, so merge the current account no and that account number. Otherwise,
add the emailID:accNo pairing. Doing this will mean ALL distinct email IDs in the problem will be present.
Next, iterating through this mapping, find the accNo of leader of each account, create a list for each
leader to store email IDs. These leaders will correspond to the distinct people (deduplicated accs).
Do this through another dict. Go on adding each email ID in first mapping to the leader of that accNo's
list.
Finally, sort the emails in each leader's list, and return it as a list of lists.
'''
class disjointGroups:
    def __init__(self, n): #creates n disjoint groups
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find_root(self, node) -> int:
        if self.parent[node] == node:
            return node
        #node is shifted up so it's the direct child of root
        self.parent[node] = self.find_root(self.parent[node]) 
        return self.parent[node]
    
    def union(self, node1, node2) -> bool:
        r1, r2 = self.find_root(node1), self.find_root(node2)
        if r1==r2: return False #no union needed to be performed
        if self.size[r1] >= self.size[r2]:
            self.parent[r2] = r1
            self.size[r1] += self.size[r2]
        else:
            self.parent[r1] = r2
            self.size[r2] += self.size[r1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #initially create n distinct people (one corresponding to each 'account')
        n = len(accounts)
        groups = disjointGroups(n)
        email_to_accNo = {}
        for accNo, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_accNo: #already have that email for another acc, try to merge them
                    groups.union(accNo, email_to_accNo[email])
                else:
                    email_to_accNo[email] = accNo
        #now we have merged accNos. into groups, we have to correspondingly merge the lists of emails
        #do this on the basis of leader/root account nos. we have found with union-find
        leaderNo_to_emails = defaultdict(list)
        for email, accNo in email_to_accNo.items():
            leaderNo = groups.find_root(accNo)
            leaderNo_to_emails[leaderNo].append(email)
        
        #now return the answer, since we have lists of merged email IDs in leaderNo_to_emails
        ans = []
        for accNo, emails in leaderNo_to_emails.items():
            name = accounts[accNo][0]
            ans.append([name] + sorted(emails))
        
        return ans