
class Commands():


	def _finde_red_dot(): 

		print("The autopilot has taken Over.")

		command_list = [
    		(self._move_forward, 5),   # 5 Sekunden geradeaus fahren
		    (self._turn_left, 1.5),     # 1.5 Sekunden nach links drehen (90 Grad)
		    (self._move_forward, 2)     # 2 Sekunden geradeaus fahren
		]


