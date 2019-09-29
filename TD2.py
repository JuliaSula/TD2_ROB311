
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import random
from statistics import mode

from math import sqrt

 

def optimal_value(gamma, opt_value, rewards, actions, states):
  """Calculs the optimal value fonction and its policy

  input:
  gamma: discount factor 
  opt_value: last value of the optimal fonction
  rewards: array of rewards values for each state
  action: transition matrix for each action
  states: state numbers
  

  output: 
  next_policy: the policy for the greater optimal value fonction of this iteration
  next_opt_value: the result of the optimal value fonction
  
  """
  v=[]
  pi=[]
  next_opt_value=np.zeros(states)
  next_policy=np.zeros(states)
  for i in range (states):
    for action in actions:
      pi.append(gamma*(np.dot(np.array(action[i]),opt_value)))
      v.append(rewards[i]+gamma*(np.dot(np.array(action[i]),opt_value)))
    next_opt_value[i]=max(v)
    next_policy[i]=np.argmax(pi)
    v=[]
    pi=[]
  """print(next_policy)"""
  return next_opt_value, next_policy


"""Parameters definition"""
x=0.25
y=0.25
gamma=0.9
states=4
opt_value=[0,0,0, 0]
rewards=[0, 0, 1, 10]
actions=[]
action0=([[0,0,0,0],[0, 1-x ,0 ,x], [1-y,0,0,y ], [1, 0 , 0, 0]])
action1=([[0,1,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
action2=([[0,0,1,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
actions=[action0, action1, action2]
epsilon=10e-4
next_opt_value=-100*np.ones(4)

i=0
"""Main Loop"""
while(sum(abs(next_opt_value-opt_value))>epsilon):
  opt_value=next_opt_value
  next_opt_value, next_policy=optimal_value(gamma, opt_value, rewards, actions, states)
  i=i+1
  """print(next_opt_value)"""
print('Number of iterations: '+str(i))
print('Opt Value'+str(next_opt_value))
print('Optimum policy:'+str(next_policy))




  
