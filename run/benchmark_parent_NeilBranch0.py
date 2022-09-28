import subprocess
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
if __name__ == '__main__':
	# PPO+exp: NCd-tt
	PPO_exp_NCd_tt = BenchmarkConfiguration(agent="ppo",wb_group="PPO+exp",wb_notes="Benchmark PPO+exp on NoCrash-dense-tt.",test_suites="nocrash_dense_tt",seed="2021",
		wb_sub_group="nocrash_dense_tt-2021",agent_ppo_wb_run_path="iccv21-roach/trained-models/1929isj0")
	subprocess.run("python","-u","benchmark_NeilBranch0.py","resume=true","log_video=true","wb_project=iccv21-roach-benchmark",
		f'agent={PPO_exp_NCd_tt.agent}',f'actors.hero.agent={PPO_exp_NCd_tt.agent}',
		f'agent.ppo.wb_run_path={PPO_exp_NCd_tt.agent_ppo_wb_run_path}',f'\'wb_group="{PPO_exp_NCd_tt.wb_group}"\'',
		f'\'wb_notes="{PPO_exp_NCd_tt.wb_notes}"\'',f'test_suites={PPO_exp_NCd_tt.test_suites}',f'seed={PPO_exp_NCd_tt.seed}',
		f'+wb_sub_group={PPO_exp_NCd_tt.wb_sub_group}',"no_rendering=true")