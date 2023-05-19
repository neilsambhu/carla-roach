# TODO: write script to modify (1) train_rl.yaml and (2) endless_all.yaml and call (3) train_rl_NeilBranch.sh.
import subprocess
import yaml, math, os
from datetime import datetime
from inspect import currentframe, getframeinfo
bVerbose = True

def train_rl_yaml(total_timesteps):
    with open("config/train_rl.yaml.bak1") as file:
        train_rl = yaml.load(file, Loader=yaml.FullLoader)
        train_rl['total_timesteps'] = int(total_timesteps)
        with open("config/train_rl.yaml", 'w') as file:
            yaml.dump(train_rl, file)
def ppo_yaml(n_steps_total):
    with open("config/agent/ppo/training/ppo.yaml.bak1") as file:
        ppo = yaml.load(file, Loader=yaml.FullLoader)
        ppo['kwargs']['n_steps_total'] = int(n_steps_total)
        with open("config/agent/ppo/training/ppo.yaml", 'w') as file:
            file.write('# @package _group_\n')
            yaml.dump(ppo, file)
def endless_all_yaml1(listTowns):
    with open('config/train_envs/endless_all.yaml', 'w') as file:
        file.write("# @package _group_\n")
        for sTown in listTowns:
            endless_all = f'''- env_id: Endless-v0
  env_configs:
    carla_map: {sTown}
    num_zombie_vehicles: [0, 150]
    num_zombie_walkers: [0, 300]
    weather_group: dynamic_1.0
  gpu: [1]\n'''
            file.write(endless_all)
def endless_all_yaml(listTowns, listGpuIds):
    with open('config/train_envs/endless_all.yaml', 'w') as file:
        file.write("# @package _group_\n")
        for sTown in listTowns:
            for sGpuId in listGpuIds:
                endless_all = f'''- env_id: Endless-v0
  env_configs:
    carla_map: {sTown}
    num_zombie_vehicles: [0, 150]
    num_zombie_walkers: [0, 300]
    weather_group: dynamic_1.0
  gpu: [{sGpuId}]\n'''
                file.write(endless_all)
def train_rl_NeilBranch0_sh():  
    if os.path.exists("outputs/num_timesteps.txt"):
        os.remove("outputs/num_timesteps.txt")
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
    fPercentComplete = (lEpoch+1)/lEpochs
    # print(f'lEpoch: {lEpoch}, lEpochs: {lEpochs}, fPercentComplete: {fPercentComplete}')
    tdStartCurrent = dtCurrent-dtStart
    # print(f'fPercentComplete: {fPercentComplete}, tdStartCurrent: {tdStartCurrent}')
    dtEstimatedCompletion = dtStart + tdStartCurrent/fPercentComplete
    print(f'fPercentComplete: {fPercentComplete}, tdStartCurrent: {tdStartCurrent}, dtEstimatedCompletion: {dtEstimatedCompletion}')

if __name__ == '__main__':
    if os.path.exists("outputs/checkpoint.txt"):
        os.remove("outputs/checkpoint.txt")

    lGlobal_total_timesteps = int(1e7)
    # lGlobal_total_timesteps = int(1e3)
    listTowns=["Town01","Town02","Town03","Town04","Town05","Town06"]
    listGpuIds=[0,1]
    listGpuIds=[1]

    # n_steps_total = int(1e5)
    n_steps_total = int(1e4)
    # with open("config/agent/ppo/training/ppo.yaml") as file:
    #     ppo = yaml.load(file, Loader=yaml.FullLoader)
    #     n_steps_total = ppo['kwargs']['n_steps_total']
    # lStepsFirstEpoch = n_steps_total*20
    # lEpochs = math.ceil((lGlobal_total_timesteps-lStepsFirstEpoch)/n_steps_total)+1
    # lDeltaStepsEpoch = n_steps_total*20
    lDeltaStepsEpoch = math.ceil(lGlobal_total_timesteps/len(listTowns))
    # lDeltaStepsEpoch = lGlobal_total_timesteps
    lEpochs = math.ceil(lGlobal_total_timesteps/lDeltaStepsEpoch)
    print(f'lGlobal_total_timesteps: {lGlobal_total_timesteps}, n_steps_total: {n_steps_total}, lEpochs: {lEpochs}, lDeltaStepsEpoch: {lDeltaStepsEpoch}')

    total_timesteps = lDeltaStepsEpoch
    # lEpochs=1
    dtStart = datetime.now()
    for lEpoch in range(lEpochs):
        # setup for current epoch
        listTownsEpoch=get_listTowns(listTowns=listTowns,lTowns=5,lEpoch=lEpoch)
        listTownsEpoch=get_listTowns(listTowns=listTowns,lTowns=3,lEpoch=lEpoch)
        listTownsEpoch=get_listTowns(listTowns=listTowns,lTowns=1,lEpoch=lEpoch)
        print(f'starting epoch {lEpoch}, total_timesteps: {total_timesteps}, listTowns: {listTownsEpoch}')
        train_rl_yaml(total_timesteps=total_timesteps)
        ppo_yaml(n_steps_total=n_steps_total)
        # endless_all_yaml1(listTowns=listTownsEpoch)
        endless_all_yaml(listTowns=listTownsEpoch, listGpuIds=listGpuIds)
        # training
        if bVerbose: 
            frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
        train_rl_NeilBranch0_sh()
        if bVerbose: 
            frameinfo = getframeinfo(currentframe());print(f"Neil {frameinfo.filename}:{frameinfo.lineno}")
        completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
        print(f"completed_timesteps: {completed_timesteps}")
        while completed_timesteps < total_timesteps:
            train_rl_NeilBranch0_sh()
            completed_timesteps = int(open("outputs/num_timesteps.txt","r").read())
            print(f"completed_timesteps: {completed_timesteps}")
        # logs
        print(f'finished epoch {lEpoch}')
        EstimatedCompletion(dtStart,datetime.now(),lEpoch,lEpochs)
        # setup for next epoch
        total_timesteps += lDeltaStepsEpoch