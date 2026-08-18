from function_task_q2 import(

	final_cost


	)

class TestFinalCost:

	def test_final_cost(self):
		
		assert final_cost(12000, "sAVe10") == 10800

	def test_promo_code(self):
		
		assert final_cost(13000, "no3452") == 13000

	def test_case(self):

		assert final_cost(16000, "halfOFF") == 8000




