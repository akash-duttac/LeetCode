'''Input: plants = [2,2,3,3], capacity = 5
Output: 14
Explanation: Start at the river with a full watering can:
- Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
- Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
- Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
- Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
- Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
- Walk to plant 3 (4 steps) and water it.
Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.'''

def steps():
    plants = [2,2,3,3]
    capacity = 5
    step = 0
    current_capacity = capacity
    for i in range(len(plants)):
        # if we have to go back
        if plants[i]>current_capacity:
            step += 2*i
            current_capacity = capacity
        
        current_capacity -= plants[i]
        step += 1
    
    return step

            

print(steps())


