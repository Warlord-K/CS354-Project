import os
from stable_baselines3.dqn.dqn import DQN
from sumo_rl import SumoEnvironment


sudo_path = "C:\Program Files (x86)\Eclipse\Sumo\\"
tools = os.path.join(sudo_path, "tools")


env = SumoEnvironment(
    net_file="nets/network.net.xml",
    route_file="nets/routes.rou.xml",
    out_csv_name="outputs/dqn",
    single_agent=True,
    use_gui=True,
    num_seconds=10000,
)

model = DQN(
    env=env,
    policy="MlpPolicy",
    learning_rate=0.001,
    learning_starts=0,
    train_freq=1,
    target_update_interval=500,
    exploration_initial_eps=0.05,
    exploration_final_eps=0.01,
    verbose=1,
    device = "cuda"
)
model.learn(total_timesteps=10000)