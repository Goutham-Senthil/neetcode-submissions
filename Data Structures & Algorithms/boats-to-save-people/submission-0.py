class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        n = len(people) - 1
        people.sort()

        boats = 0
        # print(people)
        while l <= r:
            boats+=1
            # print(boats)
            remaining = limit - people[r]
            # print(f"{l},{r} and {people[l]},{people[r]}")
            if remaining > 0 and people[l]<=remaining:
                l+=1
            r-=1
        return boats