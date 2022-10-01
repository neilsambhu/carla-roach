import subprocess,os,time,glob,statistics
class BenchmarkConfiguration:
    # various parameters when calling benchmark_NeilBranch0.sh
    def __init__(self,agent,wb_group,wb_notes,test_suites,agent_ppo_wb_run_path=None):
        self.agent = agent
        self.wb_group = wb_group
        self.wb_notes = wb_notes
        self.test_suites = test_suites
        # self.seed = seed
        self.wb_sub_group = ""
        if agent=="roaming":
            # benchmark Autopilot
            pass
        elif agent=="ppo":
            # benchmark RL experts
            self.agent_ppo_wb_run_path = agent_ppo_wb_run_path
        self.score_composed = []
        self.score_route = []
    def stringConfiguration(self):
        return f'{self.wb_group} {self.test_suites}'
    def average_score_composed(self):
        return round(sum(self.score_composed)/len(self.score_composed))
    def average_score_route(self):
        return round(sum(self.score_route)/len(self.score_route),4)
    def standardDeviation_score_composed(self):
        return round(statistics.pstdev(self.score_composed),4)
    def standardDeviation_score_route(self):
        return round(statistics.pstdev(self.score_route),4)
    def Benchmark(self):
        for seed in [2021,2022,2023]:
            DeleteCheckpointFiles()
            self.wb_sub_group = f'{self.test_suites}-{seed}'
            print(f'benchmark configuration: {self.wb_group} {self.wb_sub_group}')
            benchmarkProcess = subprocess.Popen([f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={self.agent} actors.hero.agent={self.agent} agent.ppo.wb_run_path={self.agent_ppo_wb_run_path} wb_group=\"{self.wb_group}\" wb_notes="{self.wb_notes}" test_suites={self.test_suites} seed={seed} +wb_sub_group={self.wb_sub_group} no_rendering=true'],shell=True)
            benchmarkProcess.wait()
            with open("score_composed.txt","r") as f:
                self.score_composed.append(float(f.read()))
            with open("score_route.txt","r") as f:
                self.score_route.append(float(f.read()))
            print(f'score_composed: {self.score_composed}, score_route: {self.score_route}')
        with open("results.txt","a") as f:
            f.write(f'{self.stringConfiguration()}\n')
            f.write(f'\tsuccess rate (average, standard deviation): {self.average_score_route()}, {self.standardDeviation_score_route()}\n')
            f.write(f'\tdriving score (average, standard deviation): {self.average_score_composed()}, {self.standardDeviation_score_composed()}\n')

def DeleteScoreFiles():
    if os.path.exists("score_composed.txt"):
        os.remove("score_composed.txt")
    if os.path.exists("score_route.txt"):
        os.remove("score_route.txt")
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
def GenerateBenchmarkConfigurations():
    benchmarkConfigurations = []
    for environment in ["tt","tn","nt"]
        # PPO+exp: NCd-tt
        PPO_exp_NCd_tt = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes="Benchmark PPO+exp on NoCrash-dense-tt.",test_suites="nocrash_dense_tt",agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
        benchmarkConfigurations.append(PPO_exp_NCd_tt)
        # PPO+exp: NCd-tn
        PPO_exp_NCd_tn = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes="Benchmark PPO+exp on NoCrash-dense-tn.",test_suites="nocrash_dense_tn",agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
        benchmarkConfigurations.append(PPO_exp_NCd_tn)
        # PPO+exp: NCd-nt
        PPO_exp_NCd_nt = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes="Benchmark PPO+exp on NoCrash-dense-nt.",test_suites="nocrash_dense_nt",agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
        benchmarkConfigurations.append(PPO_exp_NCd_nt)
        # PPO+exp: NCd-nn
        PPO_exp_NCd_tn = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes="Benchmark PPO+exp on NoCrash-dense-nn.",test_suites="nocrash_dense_nn",agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
        benchmarkConfigurations.append(PPO_exp_NCd_nn)
    return benchmarkConfigurations
if __name__ == '__main__':
    DeleteResultsFile()
    benchmarkConfigurations = GenerateBenchmarkConfigurations()
    for benchmarkConfiguration in benchmarkConfigurations:
        benchmarkConfiguration.Benchmark()