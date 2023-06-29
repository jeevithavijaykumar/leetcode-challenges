#70. Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Climbingstairs():
    def noofways(self,n):
        current_step =0
        next_step=1

        for i in range(0,n):
            temp = current_step
            current_step=next_step
            next_step =temp + next_step
        return(next_step)

c=Climbingstairs()
print(c.noofways(5))






