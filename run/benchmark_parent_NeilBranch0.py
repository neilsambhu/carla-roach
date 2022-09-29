import subprocess,os,time,glob
class BenchmarkConfiguration:
    # various parameters when calling benchmark_NeilBranch0.sh
    def __init__(self,agent,wb_group,wb_notes,test_suites,seed,wb_sub_group,agent_ppo_wb_run_path=None):
    	if agent=="roaming":
    		# benchmark Autopilot
    		self.agent = agent
    		self.wb_group = wb_group
    		self.wb_notes = wb_notes
    		self.test_suites = test_suites
    		self.seed = seed
    		self.wb_sub_group = wb_sub_group
    	elif agent=="ppo":
    		# benchmark RL experts
    		self.agent = agent
    		self.wb_group = wb_group
    		self.wb_notes = wb_notes
    		self.test_suites = test_suites
    		self.seed = seed
    		self.wb_sub_group = wb_sub_group
    		self.agent_ppo_wb_run_path = agent_ppo_wb_run_path
# class ResultsTable:
# 	def __init__():
# 		self.
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
if __name__ == '__main__':
	DeleteCheckpointFiles()
	secondsIn365Days = 365*86400
	score_composed = []
	score_route = []
	for seed in [2021,2022,2023]:
		# PPO+exp: NCd-tt
		DeleteScoreFiles()
		PPO_exp_NCd_tt = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes="Benchmark PPO+exp on NoCrash-dense-tt.",test_suites="nocrash_dense_tt",seed=seed,
			wb_sub_group="nocrash_dense_tt-2021",agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
		benchmarkProcess = subprocess.Popen([f'python -u benchmark_NeilBranch0.py resume=true log_video=true wb_project=iccv21-roach-benchmark agent={PPO_exp_NCd_tt.agent} actors.hero.agent={PPO_exp_NCd_tt.agent} agent.ppo.wb_run_path={PPO_exp_NCd_tt.agent_ppo_wb_run_path} wb_group=\"{PPO_exp_NCd_tt.wb_group}\" wb_notes="{PPO_exp_NCd_tt.wb_notes}" test_suites={PPO_exp_NCd_tt.test_suites} seed={PPO_exp_NCd_tt.seed} +wb_sub_group={PPO_exp_NCd_tt.wb_sub_group} no_rendering=true'],shell=True)
		benchmarkProcess.wait()
		with open("score_composed.txt","r") as f:
			score_composed.append(float(f.read()))
		with open("score_route.txt","r") as f:
			score_route.append(float(f.read()))
		print(f'score_composed: {score_composed}, score_route: {score_route}')