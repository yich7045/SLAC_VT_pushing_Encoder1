import gym
import minitouch.env

def make_dmc():
    env = gym.make("OpeningDebug-v0")
    return env
