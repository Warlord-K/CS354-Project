import os
from stable_baselines3 import PPO
from sumo_rl import SumoEnvironment


sudo_path = "C:\Program Files (x86)\Eclipse\Sumo\\"
tools = os.path.join(sudo_path, "tools")


env = SumoEnvironment(
    net_file="network.net.xml",
    route_file="routes.rou.xml",
    out_csv_name="outputs/ppo",
    single_agent=True,
    use_gui=False,
    num_seconds=10000,
)

model = PPO(
    "MlpPolicy",
    env,
    learning_rate=0.0003,
    n_steps=2048,
    batch_size=64,
    n_epochs=5,
    gamma=0.99, 
    gae_lambda=0.95,
    clip_range=0.2, 
    verbose=1,
    device="cuda" 
)
model.learn(total_timesteps=10000)