class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        '''count=0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]>0:
                count+=1
                for j in range(i+1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j]-1)'''

        count=0
        for device in batteryPercentages:
            if device-count>0:
                count+=1
            
        
        return count