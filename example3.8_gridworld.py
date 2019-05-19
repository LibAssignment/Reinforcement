"""
Example 3.8: Gridworld
consider the grid
  .A.B.
  .....
  ...b.
  .....
  .a...
* action off grid leaves unchanged with reward -1
* A -> a with reward 10
* B -> b with reward 5
* γ = 0.9
"""

#%%
from collections import namedtuple
Grid = namedtuple('Grid', ['size', 'rule'])
grid = Grid(rule={(0,1): ((4,1), 10), (0,3): ((2,3), 5)}, size=(5,5))
action_space = "snwe"
grid

#%%
def move(grid: Grid, state, action):
  """
  state is (x, y) where x, y in [0, n)
  action could be s(south/up), n(north/down), w(west/left), e(east/right)
  """
  assert action in action_space
  if state in grid.rule:
    return grid.rule[state]
  elif state[0] == 0 and action == 's':
    return (state, -1)
  elif state[0]+1 == grid.size[0] and action == 'n':
    return (state, -1)
  elif state[1] == 0 and action == 'w':
    return (state, -1)
  elif state[1]+1 == grid.size[1] and action == 'e':
    return (state, -1)
  else:
    if action == 's':
      state = (state[0]-1, state[1])
    elif action == 'n':
      state = (state[0]+1, state[1])
    elif action == 'w':
      state = (state[0], state[1]-1)
    elif action == 'e':
      state = (state[0], state[1]+1)
    return (state, 0)

#%%
import random
def random_action():
  return random.choice(action_space)

#%%
import numpy as np
state = (0, 0)
values = np.zeros(grid.size)
# for _ in range(10000):
#   new_state, value = move(grid, state, random_action())
#   values[state] = values[new_state] * 0.9 + value
#   # print(state, values[state])
#   state = new_state
for _ in range(1000):
  new_values = np.array(values, copy=True)
  for state, _ in np.ndenumerate(values):
    new_value = []
    for action in action_space:
      new_state, value = move(grid, state, action)
      new_value.append(values[new_state] * 0.9 + value)
    new_values[state] = np.mean(new_value)
  values[:] = new_values

print(np.around(values, 2))
