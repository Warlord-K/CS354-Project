import os
import sumo_rl
from sumo_rl.agents import QLAgent
from sumo_rl.exploration import EpsilonGreedy

sudo_path = "C:\Program Files (x86)\Eclipse\Sumo\\"
tools = os.path.join(sudo_path, "tools")


if __name__ == "__main__":
    alpha = 0.1
    gamma = 0.99
    decay = 1
    runs = 1

    env = sumo_rl.env(
        net_file="nets/4x4.net.xml",
        route_file="nets/4x4.rou.xml",
        use_gui=True,
        min_green=8,
        delta_time=5,
        num_seconds=10000,
    )

    for run in range(1, runs + 1):
        env.reset()
        initial_states = {ts: env.observe(ts) for ts in env.agents}
        ql_agents = {
            ts: QLAgent(
                starting_state=env.unwrapped.env.encode(initial_states[ts], ts),
                state_space=env.observation_space(ts),
                action_space=env.action_space(ts),
                alpha=alpha,
                gamma=gamma,
                exploration_strategy=EpsilonGreedy(initial_epsilon=0.05, min_epsilon=0.005, decay=decay),
            )
            for ts in env.agents
        }
        infos = []
        for agent in env.agent_iter():
            s, r, terminated, truncated, info = env.last()
            done = terminated or truncated
            if ql_agents[agent].action is not None:
                ql_agents[agent].learn(next_state=env.unwrapped.env.encode(s, agent), reward=r)

            action = ql_agents[agent].act() if not done else None
            env.step(action)

        env.unwrapped.env.save_csv("outputs/4x4", run)
        env.close()
