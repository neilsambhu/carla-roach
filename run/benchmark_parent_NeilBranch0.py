import subprocess,os,time,glob,statistics
class BenchmarkConfiguration:
    # various parameters when calling benchmark_NeilBranch0.sh
    def __init__(self,agent,wb_group,wb_notes,test_suites,agent_ppo_wb_run_path=None,bLB_all=False):
        self.agent = agent
        self.wb_group = wb_group
        self.wb_notes = wb_notes
        self.test_suites = test_suites
        # self.seed = seed
        self.wb_sub_group = ""
        if agent=="roaming":
            # benchmark Autopilot
            pass
        elif agent=="ppo" or agent=="cilrs":
            # benchmark RL experts
            self.agent_ppo_wb_run_path = agent_ppo_wb_run_path
        self.score_composed = []
        self.score_route = []
        self.bLB_all = bLB_all
    def stringConfiguration(self):
        return f'{self.wb_group} {self.test_suites}'
    def average_score_composed(self):
        if not self.bLB_all:
            return round(sum(self.score_composed)/len(self.score_composed),4)
        elif self.bLB_all:
            fAccumulator = 0
            print(f'average_score_composed: fAccumulator (before loop): {fAccumulator}')
            for list_score_composed_across_town in self.score_composed:
                # add average of values in list_score_composed_across_town to fAccumulator
                fAccumulator += sum(list_score_composed_across_town)/len(list_score_composed_across_town)
            print(f'average_score_composed: fAccumulator (after loop): {fAccumulator}')
            lCount_list_score_composed_across_town = len(self.score_composed)
            print(f'average_score_composed: lCount_list_score_composed_across_town: {lCount_list_score_composed_across_town}')
            return round(fAccumulator/lCount_list_score_composed_across_town,4)
    def average_score_route(self):
        if not self.bLB_all:
            return round(sum(self.score_route)/len(self.score_route),4)
        elif self.bLB_all:
            fAccumulator = 0
            print(f'average_score_route: fAccumulator (before loop): {fAccumulator}')
            for list_score_route_across_town in self.score_route:
                # add average of values in list_score_route_across_town to fAccumulator
                fAccumulator += sum(list_score_route_across_town)/len(list_score_route_across_town)
            print(f'average_score_route: fAccumulator (after loop): {fAccumulator}')
            lCount_list_score_route_across_town = len(self.score_route)
            print(f'average_score_route: lCount_list_score_route_across_town: {lCount_list_score_route_across_town}')
            return round(fAccumulator/lCount_list_score_route_across_town,4)
    def standardDeviation_score_composed(self):
        if not self.bLB_all:
            return round(statistics.pstdev(self.score_composed),4)
        elif self.bLB_all:
            listAverageForEachSetOfTowns = []
            print(f'standardDeviation_score_composed: listAverageForEachSetOfTowns (before loop): {listAverageForEachSetOfTowns}')
            for list_score_composed_across_town in self.score_composed:
                # add average of values in list_score_composed_across_town to listAverageForEachSetOfTowns
                listAverageForEachSetOfTowns.append(sum(list_score_composed_across_town)/len(list_score_composed_across_town))
            print(f'standardDeviation_score_composed: listAverageForEachSetOfTowns (after loop): {listAverageForEachSetOfTowns}')
            return round(statistics.pstdev(listAverageForEachSetOfTowns),4)
    def standardDeviation_score_route(self):
        if not self.bLB_all:
            return round(statistics.pstdev(self.score_route),4)
        elif self.bLB_all:
            listAverageForEachSetOfTowns = []
            print(f'standardDeviation_score_route: listAverageForEachSetOfTowns (before loop): {listAverageForEachSetOfTowns}')
            for list_score_route_across_town in self.score_route:
                # add average of values in list_score_route_across_town to listAverageForEachSetOfTowns
                listAverageForEachSetOfTowns.append(sum(list_score_route_across_town)/len(list_score_route_across_town))
            print(f'standardDeviation_score_route: listAverageForEachSetOfTowns (after loop): {listAverageForEachSetOfTowns}')
            return round(statistics.pstdev(listAverageForEachSetOfTowns),4)
    def StartBenchmarkProcess(self,seed):
        benchmarkProcess = None
        if self.agent=="ppo":
            # benchmarkProcess = subprocess.Popen([f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={self.agent} actors.hero.agent={self.agent} agent.ppo.wb_run_path={self.agent_ppo_wb_run_path} wb_group=\"{self.wb_group}\" wb_notes="{self.wb_notes}" test_suites={self.test_suites} seed={seed} +wb_sub_group={self.wb_sub_group} no_rendering=true'],shell=True)
            cmd = f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={self.agent} actors.hero.agent={self.agent} agent.ppo.wb_run_path={self.agent_ppo_wb_run_path} wb_group=\"{self.wb_group}\" wb_notes="{self.wb_notes}" test_suites={self.test_suites} seed={seed} +wb_sub_group={self.wb_sub_group} no_rendering=true'
            print(f'ppo cmd: {cmd}')
            benchmarkProcess = subprocess.Popen([cmd],shell=True)
        elif self.agent=="cilrs":
            # benchmarkProcess = subprocess.Popen([f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={self.agent} actors.hero.agent={self.agent} agent.cilrs.wb_run_path={self.agent_ppo_wb_run_path} wb_group=\"{self.wb_group}\" wb_notes="{self.wb_notes}" test_suites={self.test_suites} seed={seed} +wb_sub_group={self.wb_sub_group} no_rendering=true'],shell=True)
            cmd = f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={self.agent} actors.hero.agent={self.agent} agent.cilrs.wb_run_path={self.agent_ppo_wb_run_path} wb_group=\"{self.wb_group}\" wb_notes="{self.wb_notes}" test_suites={self.test_suites} seed={seed} +wb_sub_group={self.wb_sub_group} no_rendering=false'
            cmd = f'''python -u benchmark_NeilBranch0.py resume=true log_video=true \
  wb_project=iccv21-roach-benchmark \
  agent={self.agent} actors.hero.agent={self.agent} \
  agent.cilrs.wb_run_path={self.agent_ppo_wb_run_path} \
  'wb_group="{self.wb_group}"' \
  'wb_notes="{self.wb_notes}"' \
  test_suites={self.test_suites} \
  seed={seed} \
  +wb_sub_group={self.wb_sub_group} \
  no_rendering=false'''
            print(f'cilrs cmd: {cmd}')
            benchmarkProcess = subprocess.Popen([cmd],shell=True)
        elif self.agent=="roaming":
            benchmarkProcess = subprocess.Popen([f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={self.agent} actors.hero.agent={self.agent} +agent/roaming/obs_configs=birdview wb_group=\"{self.wb_group}\" wb_notes="{self.wb_notes}" test_suites={self.test_suites} seed={seed} +wb_sub_group={self.wb_sub_group} no_rendering=true'],shell=True)
        return benchmarkProcess
    def StartBenchmarkProcessAcross_test_suites(self,town):
        benchmarkProcess = None
        if self.test_suites==f'cc_test_{town}':
            cmd = f'''python -u benchmark_NeilBranch0.py resume=true log_video=true \
  wb_project=iccv21-roach-benchmark \
  agent={self.agent} actors.hero.agent={self.agent} \
  agent.cilrs.wb_run_path={self.agent_ppo_wb_run_path} \
  'wb_group="{self.wb_group}"' \
  'wb_notes="{self.wb_notes}"' \
  test_suites={self.test_suites} \
  seed={seed} \
  +wb_sub_group={self.wb_sub_group} \
  no_rendering=false'''
    def BenchmarkAcrossSeed(self):
        for seed in [2021,2022,2023]:
            DeleteScoreFiles()
            DeleteCheckpointFiles()
            while True:
                self.wb_sub_group = f'{self.test_suites}-{seed}'
                print(f'benchmark configuration: {self.wb_group} {self.wb_sub_group}')
                benchmarkProcess = self.StartBenchmarkProcess(seed)
                benchmarkProcess.wait()
                if CheckScoreFilesExist():
                    with open("score_composed.txt","r") as f:
                        self.score_composed.append(float(f.read()))
                    with open("score_route.txt","r") as f:
                        self.score_route.append(float(f.read()))
                    print(f'score_composed: {self.score_composed}, score_route: {self.score_route}')
                    break
        with open("results.txt","a") as f:
            f.write(f'{self.stringConfiguration()}\n')
            f.write(f'\tsuccess rate (average, standard deviation): {self.average_score_route()}, {self.standardDeviation_score_route()}\n')
            f.write(f'\tdriving score (average, standard deviation): {self.average_score_composed()}, {self.standardDeviation_score_composed()}\n')

    # 10/21/2022 9:23:47 AM: probably I should not iterate across towns here; delete function probably
    def BenchmarkAcrossTown(self):
        print(f'self.test_suites: {self.test_suites}')
        sBase_test_suites = self.test_suites
        self.score_composed = []
        self.score_route = []
        for seed in [2021,2022,2023]:
            list_score_composed_across_town = []
            list_score_route_across_town = []
            # for town in ["Town01","Town02","Town03","Town04","Town05","Town06"]:
            for town in ["Town01","Town02","Town03","Town04","Town05"]:
                DeleteScoreFiles()
                DeleteCheckpointFiles()
                while True:
                    self.test_suites = f'{sBase_test_suites}_{town}'
                    self.wb_sub_group = f'{self.test_suites}-{seed}'
                    print(f'benchmark configuration: {self.wb_group} {self.wb_sub_group}')
                    benchmarkProcess = self.StartBenchmarkProcess(seed)
                    benchmarkProcess.wait()
                    if CheckScoreFilesExist():
                        with open("score_composed.txt","r") as f:
                            list_score_composed_across_town.append(float(f.read()))
                        with open("score_route.txt","r") as f:
                            list_score_route_across_town.append(float(f.read()))
                        print(f'list_score_composed_across_town: {list_score_composed_across_town}, list_score_route_across_town: {list_score_route_across_town}')
                        break
            self.score_composed.append(list_score_composed_across_town)
            self.score_route.append(list_score_route_across_town)
            print(f'score_composed: {self.score_composed}, score_route: {self.score_route}')
        self.test_suites = sBase_test_suites
        with open("results.txt","a") as f:
            f.write(f'{self.stringConfiguration()}\n')
            f.write(f'\tsuccess rate (average, standard deviation): {self.average_score_route()}, {self.standardDeviation_score_route()}\n')
            f.write(f'\tdriving score (average, standard deviation): {self.average_score_composed()}, {self.standardDeviation_score_composed()}\n')
    def Benchmark(self):
        if not self.bLB_all:
            self.BenchmarkAcrossSeed()
        elif self.bLB_all:
            self.BenchmarkAcrossTown()
def DeleteScoreFiles():
    if os.path.exists("score_composed.txt"):
        os.remove("score_composed.txt")
    if os.path.exists("score_route.txt"):
        os.remove("score_route.txt")
def CheckScoreFilesExist():
    return os.path.exists("score_composed.txt") and os.path.exists("score_route.txt")
def DeleteCheckpointFiles():
    if os.path.exists("outputs/checkpoint.txt"):
        os.remove("outputs/checkpoint.txt")
    if os.path.exists("outputs/wb_run_id.txt"):
        os.remove("outputs/wb_run_id.txt")
    fileList = glob.glob('outputs/ep_stat_buffer_*.json', recursive=True)
    for filePath in fileList:
        if os.path.exists(filePath):
            os.remove(filePath)
def DeleteResultsFile():
    if os.path.exists("results.txt"):
        os.remove("results.txt")
def GenerateBenchmarkConfigurations0():
    benchmarkConfigurations = {}
    # for environment in ["tt","tn","nt","nn"]:
    for environment in ["tt"]:
        # # PPO+exp: NCd
        # PPO_exp_NCd = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes=f'Benchmark PPO+exp on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/10pscpih")
        # benchmarkConfigurations.append(PPO_exp_NCd)
        # # PPO+beta: NCd
        # PPO_beta_NCd = BenchmarkConfiguration(agent="ppo",wb_group="PPO+beta",wb_notes=f'Benchmark PPO+beta on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/1ch63m76")
        # benchmarkConfigurations.append(PPO_beta_NCd)
        # # Roach: NCd
        # Roach_NCd = BenchmarkConfiguration(agent="ppo",wb_group="Roach",wb_notes=f'Benchmark Roach on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
        # benchmarkConfigurations.append(Roach_NCd)
        # # Autopilot: NCd
        # Autopilot_NCd = BenchmarkConfiguration(agent="roaming",wb_group="Autopilot",wb_notes=f'Benchmark Autopilot on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}')
        # benchmarkConfigurations.append(Autopilot_NCd)
        # 10/5/2022 10:27:13 PM: IL agents trained on NoCrash benchmark: start
        L_A_AP_NCd = BenchmarkConfiguration(agent="cilrs",wb_group="L_A(AP)",wb_notes=f'Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/39o1h862")
        # benchmarkConfigurations.append(L_A_AP_NCd)
        benchmarkConfigurations[str(f'L_A_AP_NCd_{environment}')] = L_A_AP_NCd
        # L_K_L_F_c_NCd = BenchmarkConfiguration(agent="cilrs",wb_group="L_K+L_F(c)",wb_notes=f'Benchmark L_K+L_F(c) trained on NoCrash benchmark on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/31u9tki7")
        # benchmarkConfigurations.append(L_K_L_F_c_NCd)
        # 10/5/2022 10:27:13 PM: IL agents trained on NoCrash benchmark: end
    return benchmarkConfigurations
def GenerateBenchmarkConfigurations():
    benchmarkConfigurations = {}
    # for environment in ["tt","tn","nt","nn"]:
    for environment in ["tt"]:
        # # PPO+exp: NCd
        # PPO_exp_NCd = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes=f'Benchmark PPO+exp on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/10pscpih")
        # benchmarkConfigurations.append(PPO_exp_NCd)
        # # PPO+beta: NCd
        # PPO_beta_NCd = BenchmarkConfiguration(agent="ppo",wb_group="PPO+beta",wb_notes=f'Benchmark PPO+beta on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/1ch63m76")
        # benchmarkConfigurations.append(PPO_beta_NCd)
        # # Roach: NCd
        # Roach_NCd = BenchmarkConfiguration(agent="ppo",wb_group="Roach",wb_notes=f'Benchmark Roach on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
        # benchmarkConfigurations.append(Roach_NCd)
        # # Autopilot: NCd
        # Autopilot_NCd = BenchmarkConfiguration(agent="roaming",wb_group="Autopilot",wb_notes=f'Benchmark Autopilot on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}')
        # benchmarkConfigurations.append(Autopilot_NCd)
        # 10/5/2022 10:27:13 PM: IL agents trained on NoCrash benchmark: start
        # L_A_AP_NCd = BenchmarkConfiguration(agent="cilrs",wb_group="L_A(AP)",wb_notes=f'Benchmark L_A(AP) trained on NoCrash benchmark on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/39o1h862")
        # benchmarkConfigurations[str(f'L_A_AP_NCd_{environment}')] = L_A_AP_NCd
        # L_K_L_F_c_NCd = BenchmarkConfiguration(agent="cilrs",wb_group="L_K+L_F(c)",wb_notes=f'Benchmark L_K+L_F(c) trained on NoCrash benchmark on NoCrash-dense-{environment}.',test_suites=f'nocrash_dense_{environment}',agent_ppo_wb_run_path="iccv21-roach/trained-models/31u9tki7")
        # benchmarkConfigurations[str(f'L_K_L_F_c_NCd_{environment}')] = L_K_L_F_c_NCd
        # 10/5/2022 10:27:13 PM: IL agents trained on NoCrash benchmark: end
        pass
    # 10/23/2022 11:09:27 AM: Neil added LB-all: start
    PPO_exp_LB_all = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes=f'Benchmark PPO+exp on LeaderBoard-all.',test_suites=f'cc_test',agent_ppo_wb_run_path="iccv21-roach/trained-models/10pscpih",bLB_all=True)
    benchmarkConfigurations[str('PPO_exp_LB_all')] = PPO_exp_LB_all
    PPO_beta_LB_all = BenchmarkConfiguration(agent="ppo",wb_group="PPO+beta",wb_notes=f'Benchmark PPO+beta on LeaderBoard-all.',test_suites=f'cc_test',agent_ppo_wb_run_path="iccv21-roach/trained-models/1ch63m76",bLB_all=True)
    benchmarkConfigurations[str('PPO_beta_LB_all')] = PPO_beta_LB_all
    Roach_LB_all = BenchmarkConfiguration(agent="ppo",wb_group="Roach",wb_notes=f'Benchmark Roach on LeaderBoard-all.',test_suites=f'cc_test',agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0",bLB_all=True)
    benchmarkConfigurations[str('Roach_LB_all')] = Roach_LB_all
    Autopilot_LB_all = BenchmarkConfiguration(agent="roaming",wb_group="Autopilot",wb_notes=f'Benchmark Autopilot on LeaderBoard-all.',test_suites=f'cc_test',bLB_all=True)
    benchmarkConfigurations[str('Autopilot_LB_all')] = Autopilot_LB_all
    L_A_AP_LB_all = BenchmarkConfiguration(agent="cilrs",wb_group="L_A(AP)",wb_notes=f'Benchmark L_A(AP) trained on LeaderBoard benchmark on LeaderBoard-all.',test_suites=f'cc_test',agent_ppo_wb_run_path="iccv21-roach/trained-models/1myvm4mw",bLB_all=True)
    benchmarkConfigurations[str('L_A_AP_LB_all')] = L_A_AP_LB_all
    L_K_L_F_c_LB_all = BenchmarkConfiguration(agent="cilrs",wb_group="L_K+L_F(c)",wb_notes=f'Benchmark L_K+L_F(c) trained on LeaderBoard benchmark on LeaderBoard-all.',test_suites=f'cc_test',agent_ppo_wb_run_path="iccv21-roach/trained-models/zwadqx9z",bLB_all=True)
    benchmarkConfigurations[str('L_K_L_F_c_LB_all')] = L_K_L_F_c_LB_all
    # 10/23/2022 11:09:27 AM: Neil added LB-all: end
    return benchmarkConfigurations    
def ResultsLatex(dictBenchmarkConfigurations=None):
    # output = '\\begin{table*}[!t]\n\\begin{center}\n\\begin{tabular}{ |c|c|c|c|c|c| }\n \hline\n Suc. Rate \% & NCd-tt & NCd-tn & NCd-nt & NCd-nn & LB-all \\\ \n \hline\n PPO+exp & $99 \pm 0$ & $99 \pm 1$ & $97 \pm 1$ & $98 \pm 1$ & $ \pm $ \\\ \n \hline\n PPO+beta & $98 \pm 2$ & $100 \pm 0$ & $96 \pm 1$ & $97 \pm 0$ & $ \pm $ \\\ \n \hline\n Roach & $98 \pm 0$ & $100 \pm 0$ & $91 \pm 4$ & $85 \pm 0$ & $ \pm $ \\\ \n \hline\n AP (carla-roach) & $96 \pm 2$ & $99 \pm 1$ & $92 \pm 0$ & $87 \pm 3$ & $ \pm $ \\\ \n \hline\n carla-roach baseline, $L_A(AP)$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n carla-roach best, $L_K + L_F(c)$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n \hline\n Dri. Score \% & NCd-tt & NCd-tn & NCd-nt & NCd-nn & LB-all \\\ \n \hline\n PPO+exp & $94 \pm 0$ & $97 \pm 1$ & $87 \pm 1$ & $90 \pm 2$ & $ \pm $ \\\ \n \hline\n PPO+beta & $95 \pm 2$ & $97 \pm 1$ & $88 \pm 4$ & $92 \pm 3$ & $ \pm $ \\\ \n \hline\n Roach & $96 \pm 0$ & $97 \pm 1$ & $83 \pm 3$ & $80 \pm 0$ & $ \pm $ \\\ \n \hline\n AP (carla-roach) & $88 \pm 6$ & $85 \pm 0$ & $69 \pm 0$ & $78 \pm 4$ & $ \pm $ \\\ \n \hline\n carla-roach baseline, $L_A(AP)$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n carla-roach best, $L_K + L_F(c)$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n\end{tabular}\n\end{center}\n\end{table*}'
    output = '\\begin{{table*}}[!t]\n\\begin{{center}}\n\\begin{{tabular}}{{ |c|c|c|c|c|c| }}\n \hline\n Suc. Rate \% & NCd-tt & NCd-tn & NCd-nt & NCd-nn & LB-all \\\ \n \hline\n PPO+exp & $99 \pm 0$ & $99 \pm 1$ & $97 \pm 1$ & $98 \pm 1$ & $ \pm $ \\\ \n \hline\n PPO+beta & $98 \pm 2$ & $100 \pm 0$ & $96 \pm 1$ & $97 \pm 0$ & $ \pm $ \\\ \n \hline\n Roach & $98 \pm 0$ & $100 \pm 0$ & $91 \pm 4$ & $85 \pm 0$ & $ \pm $ \\\ \n \hline\n AP (carla-roach) & $96 \pm 2$ & $99 \pm 1$ & $92 \pm 0$ & $87 \pm 3$ & $ \pm $ \\\ \n \hline\n carla-roach baseline, $L_A(AP)$ & ${L_A_AP_NCd_tt_successRate} \pm {L_A_AP_NCd_tt_successRate_standardDeviation}$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n carla-roach best, $L_K + L_F(c)$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n \hline\n Dri. Score \% & NCd-tt & NCd-tn & NCd-nt & NCd-nn & LB-all \\\ \n \hline\n PPO+exp & $94 \pm 0$ & $97 \pm 1$ & $87 \pm 1$ & $90 \pm 2$ & $ \pm $ \\\ \n \hline\n PPO+beta & $95 \pm 2$ & $97 \pm 1$ & $88 \pm 4$ & $92 \pm 3$ & $ \pm $ \\\ \n \hline\n Roach & $96 \pm 0$ & $97 \pm 1$ & $83 \pm 3$ & $80 \pm 0$ & $ \pm $ \\\ \n \hline\n AP (carla-roach) & $88 \pm 6$ & $85 \pm 0$ & $69 \pm 0$ & $78 \pm 4$ & $ \pm $ \\\ \n \hline\n carla-roach baseline, $L_A(AP)$ & ${L_A_AP_NCd_tt_drivingScore} \pm {L_A_AP_NCd_tt_drivingScore_standardDeviation}$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n carla-roach best, $L_K + L_F(c)$ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ & $ \pm $ \\\ \n \hline\n\end{{tabular}}\n\end{{center}}\n\end{{table*}}'.format(
        L_A_AP_NCd_tt_successRate=round(dictBenchmarkConfigurations['L_A_AP_NCd_tt'].average_score_route()*100),
        L_A_AP_NCd_tt_successRate_standardDeviation=round(dictBenchmarkConfigurations['L_A_AP_NCd_tt'].standardDeviation_score_route()*100),
        L_A_AP_NCd_tt_drivingScore=round(dictBenchmarkConfigurations['L_A_AP_NCd_tt'].average_score_composed()*100),
        L_A_AP_NCd_tt_drivingScore_standardDeviation=round(dictBenchmarkConfigurations['L_A_AP_NCd_tt'].standardDeviation_score_composed()*100)
        )
    return output
if __name__ == '__main__':
    DeleteResultsFile()
    dictBenchmarkConfigurations = GenerateBenchmarkConfigurations()
    print(f'dictBenchmarkConfigurations: {dictBenchmarkConfigurations}')
    for keyBenchmarkConfiguration in dictBenchmarkConfigurations:
        dictBenchmarkConfigurations[keyBenchmarkConfiguration].Benchmark()
        print(f'results from {keyBenchmarkConfiguration}: success rate {dictBenchmarkConfigurations[keyBenchmarkConfiguration].average_score_route()} +/- {dictBenchmarkConfigurations[keyBenchmarkConfiguration].standardDeviation_score_route()}, driving score {dictBenchmarkConfigurations[keyBenchmarkConfiguration].average_score_composed()} +/- {dictBenchmarkConfigurations[keyBenchmarkConfiguration].standardDeviation_score_composed()}')
    # print(f'LaTeX-formatted results:\n{ResultsLatex(dictBenchmarkConfigurations)}')