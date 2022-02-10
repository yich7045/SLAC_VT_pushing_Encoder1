import gym
import minitouch.env

def make_dmc():
    env = gym.make("Opening-v1")
    return env
