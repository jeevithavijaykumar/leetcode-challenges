#134. Gas Station

class Gasstation():
    def circuitcompletion(self,gas,cost):
        if(sum(gas) < sum(cost)):
            return(-1)
        start_index =0
        total_gas=0

        for i in range (0,len(gas)):
            total_gas = total_gas + gas[i]- cost[i]
            if(total_gas <0):
                start_index = i+1
                total_gas = 0
        return(start_index)

g = Gasstation()
gas = [1,2,3,4,5]
cost= [3,4,5,1,2]
print(g.circuitcompletion(gas,cost))

