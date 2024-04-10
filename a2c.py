
import os
from stable_baselines3 import A2C
from sumo_rl import SumoEnvironment

sudo_path = "C:\Program Files (x86)\Eclipse\Sumo\\"
tools = os.path.join(sudo_path, "tools")
env = SumoEnvironment(
    net_file="nets/network.net.xml",
    route_file="nets/routes.rou.xml",
    out_csv_name="outputs/a2c",
    single_agent=True,
    use_gui=True,
    num_seconds=10000,
)

model = A2C(
    "MlpPolicy",
    env,
    learning_rate=0.0007,  
    n_steps=5, 
    ent_coef=0.01,  
    gamma=0.99,  
    gae_lambda=1.0,  
    vf_coef=0.25,  
    max_grad_norm=0.5,  
    rms_prop_eps=1e-5, 
    use_rms_prop=True,  
    verbose=1,
    tensorboard_log="./logs", 
    device="cuda"
)
model.learn(total_timesteps=10000)