import pybullet_multigoal_gym as pmg

env = pmg.make('KukaReachRenderSparseEnv-v0')
obs = env.reset()
t = 0
while True:
    t += 1
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    print(action,'\n',
          'state: ', obs['state'], '\n',
          'desired_goal: ', obs['desired_goal'], '\n',
          'achieved_goal: ', obs['achieved_goal'], '\n',
          'reward: ', reward, '\n')
    if done:
        env.reset()
