class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        last_value = 0

        for i in operations:
            print(records)
            
            if i == 'D':
                temp = records[len(records)-1]
                records.append(2*temp)
                continue
            
            if i == 'C':
                records.pop()
                continue

            if i == '+':
                temp1 = records[len(records)-1]
                temp2 = records[len(records)-2]
                records.append(temp1 + temp2)
                continue

            records.append(int(i))

        return sum(records)


            