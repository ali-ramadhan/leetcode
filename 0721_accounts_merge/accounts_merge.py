# Runtime: 4776 ms (beats 5.1%) lol
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # We will store names and emails using a hashmap.
        # If there is only one "Omar" then storage["Omar"][0] will store all of Omar's emails.
        # If there are two people named "Zahra" then storage["Zahra"][0] will store the first's
        # emails, and storage["Zahra"][1] will store the second's emails.
        storage = {}

        for person in accounts:
            name = person[0]
            emails = person[1:]
            
            if name not in storage:
                storage[name] = {}
                storage[name][0] = []
                storage[name][0].extend(emails)
            else:
                # Check if this person corresponds to an existing person.
                person_id = None
                max_id = max(storage[name].keys())
                for i in range(max_id+1):
                    for email in emails:
                        if email in storage[name][i]:
                            person_id = i
                            break
                    if person_id:
                        break
                
                if person_id is not None:
                    storage[name][person_id].extend(emails)
                else:
                    person_id = max_id + 1
                    storage[name][person_id] = []
                    storage[name][person_id].extend(emails)

        print(storage)

        # Very ugly solution for merging accounts in case any were missed.
        # This can happen if a 3rd or 4th entry reveals that two previously
        # separate people were actually the same person.
        # Actually it's extremely ugly because I'm doing it 6 times to take care of edge cases.
        for _ in range(6):
            for name in storage:
                ids = sorted(storage[name].keys())
                for i in storage[name]:
                    ids_larger_than_i = sorted([k for k in storage[name].keys() if k > i])
                    for j in ids_larger_than_i:
                        for email in storage[name][i]:
                            if email in storage[name][j]:
                                # Merging j into i
                                storage[name][i].extend(storage[name][j])
                                storage[name][j] = []

        output = []
        for name in storage:
            for i in storage[name]:
                if len(storage[name][i]) > 0:
                    person = [name]
                    emails = storage[name][i]
                    emails.sort()

                    for email in emails:
                        if email not in person:
                            person.append(email)
                    
                    output.append(person)
    
        return output
