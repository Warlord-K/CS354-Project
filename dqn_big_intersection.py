import os
from stable_baselines3.dqn.dqn import DQN
from sumo_rl import SumoEnvironment

sudo_path = "C:\Program Files (x86)\Eclipse\Sumo\\"
tools = os.path.join(sudo_path, "tools")

env = SumoEnvironment(
    net_file="nets/big-intersection.net.xml",
    single_agent=True,
    route_file="nets/big-intersection.rou.xml",
    out_csv_name="outputs/big-intersection/dqn",
    use_gui=False,
    num_seconds=10000,
    yellow_time=4,
    min_green=5,
    max_green=60,
)

model = DQN(
    env=env,
    policy="MlpPolicy",
    learning_rate=1e-3,
    learning_starts=0,
    buffer_size=50000,
    train_freq=1,
    target_update_interval=200,
    exploration_fraction=0.05,
    exploration_final_eps=0.01,
    verbose=1,
)
model.learn(total_timesteps=10000)
