def solve(numheads,numlegs):
    rabbit = (numlegs-2*numheads)/2
    chicken = numheads-rabbit
    return {rabbit,chicken}
numheads,numlegs = map(int,input().split())
answer = solve(numheads,numlegs)
print(answer[0],answer[1])