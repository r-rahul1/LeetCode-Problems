class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people.sort()
        fp,sp = 0,len(people)-1
        
        while fp <= sp:
            boat += 1
            if people[fp]+people[sp] <= limit:
                fp += 1
            sp -= 1
        
        return boat