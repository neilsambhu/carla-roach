# TODO: write script to modify (1) train_rl.yaml and (2) endless_all.yaml and call (3) train_rl_NeilBranch.sh.
import subprocess
import yaml, math, os
from datetime import datetime

def train_rl_yaml(total_timesteps):
    with open("config/train_rl.yaml.bak1") as file:
        train_rl = yaml.load(file, Loader=yaml.FullLoader)
        train_rl['total_timesteps'] = int(total_timesteps)
        with open("config/train_rl.yaml", 'w') as file:
            yaml.dump(train_rl, file)
def endless_all_yaml(listTowns):
    with open('config/train_envs/endless_all.yaml', 'w') as file:
        file.write("# @package _group_\n")
        for sTown in listTowns:
            endless_all = f'''- env_id: Endless-v0
  env_configs:
    carla_map: {sTown}
    num_zombie_vehicles: [0, 150]
    num_zombie_walkers: [0, 300]
    weather_group: dynamic_1.0
  gpu: [0]\n'''
            file.write(endless_all)
def train_rl_NeilBranch0_sh():  
    subprocess.call(['run/train_rl_NeilBranch0.sh'])
def get_listTowns(listTowns,lTowns,lEpoch):
    lIdx_listTowns = lEpoch%lTowns
    listTownsOutput = []
    for lTown in range(lTowns):
        sTown = listTowns[lIdx_listTowns%len(listTowns)]
        listTownsOutput.append(sTown)
        lIdx_listTowns += 1
    return listTownsOutput
def EstimatedCompletion(dtStart, dtCurrent, lEpoch, lEpochs):
    fPercentComplete = lEpoch/lEpochs
    tdStartCurrent = dtCurrent-dtStart
    dtEstimatedCompletion = dtStart + tdStartCurrent/fPercentComplete
    print(f'fPercentComplete: {fPercentComplete}, tdStartCurrent: {tdStartCurrent}, dtEstimatedCompletion: {dtEstimatedCompletion}')

if __name__ == '__main__':
    if os.path.exists("outputs/checkpoint.txt"):
        os.remove("outputs/checkpoint.txt")

    lGlobal_total_timesteps = int(1e7)
    # lGlobal_total_timesteps = int(10)

    n_steps_total = 0
    with open("config/agent/ppo/training/ppo.yaml") as file:
        ppo = yaml.load(file, Loader=yaml.FullLoader)
        n_steps_total = ppo['kwargs']['n_steps_total']
    # lStepsFirstEpoch = n_steps_total*20
    # lEpochs = math.ceil((lGlobal_total_timesteps-lStepsFirstEpoch)/n_steps_total)+1
    lDeltaStepsEpoch = n_steps_total*20
    lEpochs = math.ceil(lGlobal_total_timesteps/lDeltaStepsEpoch)
    print(f'lGlobal_total_timesteps: {lGlobal_total_timesteps}, n_steps_total: {n_steps_total}, lEpochs: {lEpochs}')
    listTowns=["Town01","Town02","Town03","Town04","Town05","Town06"]

    total_timesteps = lDeltaStepsEpoch
    dtStart = datetime.now()
    for lEpoch in range(lEpochs):
        listTownsEpoch=get_listTowns(listTowns=listTowns,lTowns=5,lEpoch=lEpoch)
        print(f'starting epoch {lEpoch}, total_timesteps: {total_timesteps}, listTowns: {listTownsEpoch}')
        train_rl_yaml(total_timesteps=total_timesteps)
        endless_all_yaml(listTowns=listTownsEpoch)
        train_rl_NeilBranch0_sh()
        print(f'finished epoch {lEpoch}')

        EstimatedCompletion(dtStart,datetime.now(),lEpoch,lEpochs)

        total_timesteps += lDeltaStepsEpoch