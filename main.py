import argparse
import matplotlib.pyplot as plt
from Umbrellas import Umbrellas

parser = argparse.ArgumentParser(description='Q6')

parser.add_argument('-r', type=int, required=False,default=3,help='Number of Umbrellas')
parser.add_argument('-rmax', type=int, required=False,default=10,help='Varying r for the 2nd part and hence the max value')
parser.add_argument('-p', type=float, required=False,default=0.6,help='Probability it will rain')


args = parser.parse_args()

print("Args in simulation")
print(f"r {args.r} , r_max {args.rmax} ,  p {args.p}")


model = Umbrellas(args.r , args.p)

print(f"Q1) Proportion of time or Probability that our man gets wet is {model.part1()}")

temp = []

end = args.rmax+1

for r in range(end):
    model = Umbrellas(r , args.p)
    limiting_probabs = model.pi
    temp.append(limiting_probabs)

q2_plotting_data = []

for i in range(2*(end)):
    inner_list = []
    for j in range(i//2,end):
        inner_list.append(temp[j][i])
    q2_plotting_data.append(inner_list)

for i, sublist in enumerate(q2_plotting_data):
    x = [i//2 + j + 1 for j in range(len(sublist))]  
    y = sublist 
    plt.plot(x, y, marker='o',label=f'State {i}')

# Add labels and legend
plt.xlabel('Number of Umbrellas (r)')
plt.ylabel('Stationary Probability')
plt.title(' Limiting probabilities for each Markov chain State varying r')
plt.legend()

# Show the plot
plt.show()




