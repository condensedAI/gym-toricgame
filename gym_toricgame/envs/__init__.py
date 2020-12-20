from gym.envs.registration import register

register(
    id='toricgame-v0',
    entry_point="gym_toricgame.envs.toricgame:ToricGameEnv",
    nondeterministic=True
)
