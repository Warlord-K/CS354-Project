# Installation

### Install SUMO latest version(Linux):

```bash
sudo add-apt-repository ppa:sumo/stable
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
```
Don't forget to set SUMO_HOME variable (default sumo installation path is /usr/share/sumo)
```bash
echo 'export SUMO_HOME="/usr/share/sumo"' >> ~/.bashrc
source ~/.bashrc
```
Important: for a huge performance boost (~8x) with Libsumo, you can declare the variable:
```bash
export LIBSUMO_AS_TRACI=1
```
Notice that you will not be able to run with sumo-gui or with multiple simulations in parallel if this is active ([more details](https://sumo.dlr.de/docs/Libsumo.html)).

### Install SUMO (Windows):

Go to [SUMO Website](https://sumo.dlr.de/docs/Installing/index.html) and download the installer.

### Install Python Requirements

```bash
pip install -r requirements.txt
```

# Run

### Train

To train an agent, just run the file, set `use_gui=False` for faster training.

For example, for A2C on Normal Intersection,
```bash
python a2c.py
```

| Algorithm | Environment        | File                    |   |   |
|-----------|--------------------|-------------------------|---|---|
| A2C       | Basic Intersection | a2c.py                  |   |   |
| A2C       | Big Intersection   | a2c_big_intersection.py |   |   |
| DQN       | Basic Intersection | dqn.py                  |   |   |
| DQN       | Big Intersection   | dqn_big_intersection.py |   |   |
| PPO       | Basic Intersection | ppo.py                  |   |   |
| PPO       | Big Intersection   | ppo_big_intersection.py |   |   |
| MAQRL     | City (4x4)         | env_4x4.py              |   |   |

### Plot

We also provide code to plot the outputs, to plot outputs from a2c.py

```bash
python plot.py -f outputs/a2c
```
