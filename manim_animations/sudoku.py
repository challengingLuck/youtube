from big_ol_pile_of_manim_imports import *

class sudoku(Scene):
	def construct(self):
		big_square = Square(stroke_width = 10, color = WHITE)
		big_square.scale(3) 
		normal_square = Square(stroke_width = 5, color = WHITE).shift([0,0,0])
		small_square = Square(stroke_width = 0.7, color = WHITE).shift([0/3,0/3,0/3])
		x = -3+1/3
		y = -3+1/3
		while y < 2.7:
			while x < 2.7:
				self.add(Square(stroke_width = 0.7, color = WHITE).scale(0.333).shift([x,y,0])) 
				x = x+2/3
			y = y+2/3
			x = -3+1/3

		x = -2
		y = -2
		while y < 3:
			while x < 3:
				self.add(Square(stroke_width=5, color = WHITE).shift([x,y,0])) 
				x = x+2
			y = y+2
			x = -2


		A_1 = TextMobject(" ", color = WHITE)
		A_1.shift(8/3*UP+8/3*LEFT)

		A_2 = TextMobject("2", color = WHITE)
		A_2.shift(8/3*UP+6/3*LEFT) 

		A_3 = TextMobject("4", color = WHITE)
		A_3.shift(8/3*UP + 4/3*LEFT)

		A_4 = TextMobject(" ", color = WHITE)
		A_4.shift(8/3*UP + 2/3*LEFT)

		A_5 = TextMobject(" ")
		A_5.shift(8/3*UP + 0/3*LEFT)

		A_6 = TextMobject("7", color = WHITE)
		A_6.shift(8/3*UP + 2/3*RIGHT)

		A_7 = TextMobject(" ", color = WHITE)
		A_7.shift(8/3*UP +4/3*RIGHT)

		A_8 = TextMobject(" ", color = WHITE)
		A_8.shift(8/3*UP + 6/3*RIGHT)

		A_9 = TextMobject(" ", color = WHITE)
		A_9.shift(8/3*UP + 8/3*RIGHT)
		row_1 = [A_1, A_2, A_3, A_4, A_5, A_6, A_7, A_8, A_9]


		B_1 = TextMobject("6", color = WHITE)
		B_1.shift(6/3*UP+8/3*LEFT)

		B_2 = TextMobject(" ", color = WHITE)
		B_2.shift(6/3*UP+6/3*LEFT) 

		B_3 = TextMobject(" ", color = WHITE)
		B_3.shift(6/3*UP + 4/3*LEFT)

		B_4 = TextMobject(" ", color = WHITE)
		B_4.shift(6/3*UP + 2/3*LEFT)

		B_5 = TextMobject(" ", color = WHITE)
		B_5.shift(6/3*UP + 0/3*LEFT)

		B_6 = TextMobject(" ", color = WHITE)
		B_6.shift(6/3*UP + 2/3*RIGHT)

		B_7 = TextMobject(" ", color = WHITE)
		B_7.shift(6/3*UP +4/3*RIGHT)

		B_8 = TextMobject(" ", color = WHITE)
		B_8.shift(6/3*UP + 6/3*RIGHT)

		B_9 = TextMobject(" ", color = WHITE)
		B_9.shift(6/3*UP + 8/3*RIGHT)
		row_2 = [B_1, B_2, B_3, B_4, B_5, B_6, B_7, B_8, B_9]





		C_1 = TextMobject(" ", color = WHITE)
		C_1.shift(4/3*UP+8/3*LEFT)

		C_2 = TextMobject(" ", color = WHITE)
		C_2.shift(4/3*UP+6/3*LEFT) 

		C_3 = TextMobject("3", color = WHITE)
		C_3.shift(4/3*UP + 4/3*LEFT)

		C_4 = TextMobject("6", color = WHITE)
		C_4.shift(4/3*UP + 2/3*LEFT)

		C_5 = TextMobject("8", color = WHITE)
		C_5.shift(4/3*UP + 0/3*LEFT)

		C_6 = TextMobject(" ", color = WHITE)
		C_6.shift(4/3*UP + 2/3*RIGHT)

		C_7 = TextMobject("4", color = WHITE)
		C_7.shift(4/3*UP +4/3*RIGHT)

		C_8 = TextMobject("1", color = WHITE)
		C_8.shift(4/3*UP + 6/3*RIGHT)

		C_9 = TextMobject("5", color = WHITE)
		C_9.shift(4/3*UP + 8/3*RIGHT)
		row_3 = [C_1, C_2, C_3, C_4, C_5, C_6, C_7, C_8, C_9]





		D_1 = TextMobject("4", color = WHITE)
		D_1.shift(2/3*UP+8/3*LEFT)

		D_2 = TextMobject("3", color = WHITE)
		D_2.shift(2/3*UP+6/3*LEFT) 

		D_3 = TextMobject("1", color = WHITE)
		D_3.shift(2/3*UP + 4/3*LEFT)

		D_4 = TextMobject(" ", color = WHITE)
		D_4.shift(2/3*UP + 2/3*LEFT)

		D_5 = TextMobject(" ", color = WHITE)
		D_5.shift(2/3*UP + 0/3*LEFT)

		D_6 = TextMobject("5", color = WHITE)
		D_6.shift(2/3*UP + 2/3*RIGHT)

		D_7 = TextMobject(" ", color = WHITE)
		D_7.shift(2/3*UP +4/3*RIGHT)

		D_8 = TextMobject(" ", color = WHITE)
		D_8.shift(2/3*UP + 6/3*RIGHT)

		D_9 = TextMobject(" ", color = WHITE)
		D_9.shift(2/3*UP + 8/3*RIGHT)
		row_4 = [D_1, D_2, D_3, D_4, D_5, D_6, D_7, D_8, D_9]






		E_1 = TextMobject("5", color = WHITE)
		E_1.shift(0/3*UP+8/3*LEFT)

		E_2 = TextMobject(" ", color = WHITE)
		E_2.shift(0/3*UP+6/3*LEFT) 

		E_3 = TextMobject(" ", color = WHITE)
		E_3.shift(0/3*UP + 4/3*LEFT)

		E_4 = TextMobject(" ", color = WHITE)
		E_4.shift(0/3*UP + 2/3*LEFT)

		E_5 = TextMobject(" ", color = WHITE)
		E_5.shift(0/3*UP + 0/3*LEFT)

		E_6 = TextMobject(" ", color = WHITE)
		E_6.shift(0/3*UP + 2/3*RIGHT)

		E_7 = TextMobject(" ", color = WHITE)
		E_7.shift(0/3*UP +4/3*RIGHT)

		E_8 = TextMobject("3", color = WHITE)
		E_8.shift(0/3*UP + 6/3*RIGHT)

		E_9 = TextMobject("2", color = WHITE)
		E_9.shift(0/3*UP + 8/3*RIGHT)
		row_5 = [E_1, E_2, E_3, E_4, E_5, E_6, E_7, E_8, E_9]





		F_1 = TextMobject("7", color = WHITE)
		F_1.shift(-2/3*UP+8/3*LEFT)

		F_2 = TextMobject("9", color = WHITE)
		F_2.shift(-2/3*UP+6/3*LEFT) 

		F_3 = TextMobject(" ", color = WHITE)
		F_3.shift(-2/3*UP + 4/3*LEFT)

		F_4 = TextMobject(" ", color = WHITE)
		F_4.shift(-2/3*UP + 2/3*LEFT)

		F_5 = TextMobject(" ", color = WHITE)
		F_5.shift(-2/3*UP + 0/3*LEFT)

		F_6 = TextMobject(" ", color = WHITE)
		F_6.shift(-2/3*UP + 2/3*RIGHT)

		F_7 = TextMobject(" ", color = WHITE)
		F_7.shift(-2/3*UP +4/3*RIGHT)

		F_8 = TextMobject("6", color = WHITE)
		F_8.shift(-2/3*UP + 6/3*RIGHT)

		F_9 = TextMobject(" ", color = WHITE)
		F_9.shift(-2/3*UP + 8/3*RIGHT)
		row_6 = [F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9]





		G_1 = TextMobject("2", color = WHITE)
		G_1.shift(-4/3*UP+8/3*LEFT)

		G_2 = TextMobject(" ", color = WHITE)
		G_2.shift(-4/3*UP+6/3*LEFT) 

		G_3 = TextMobject("9", color = WHITE)
		G_3.shift(-4/3*UP + 4/3*LEFT)

		G_4 = TextMobject("7", color = WHITE)
		G_4.shift(-4/3*UP + 2/3*LEFT)

		G_5 = TextMobject("1", color = WHITE)
		G_5.shift(-4/3*UP + 0/3*LEFT)

		G_6 = TextMobject(" ", color = WHITE)
		G_6.shift(-4/3*UP + 2/3*RIGHT)

		G_7 = TextMobject("8", color = WHITE)
		G_7.shift(-4/3*UP +4/3*RIGHT)

		G_8 = TextMobject(" ", color = WHITE)
		G_8.shift(-4/3*UP + 6/3*RIGHT)

		G_9 = TextMobject(" ", color = WHITE)
		G_9.shift(-4/3*UP + 8/3*RIGHT)
		row_7 = [G_1, G_2, G_3, G_4, G_5, G_6, G_7, G_8, G_9]






		H_1 = TextMobject(" ", color = WHITE)
		H_1.shift(-6/3*UP+8/3*LEFT)

		H_2 = TextMobject("4", color = WHITE)
		H_2.shift(-6/3*UP+6/3*LEFT) 

		H_3 = TextMobject(" ", color = WHITE)
		H_3.shift(-6/3*UP + 4/3*LEFT)

		H_4 = TextMobject(" ", color = WHITE)
		H_4.shift(-6/3*UP + 2/3*LEFT)

		H_5 = TextMobject("9", color = WHITE)
		H_5.shift(-6/3*UP + 0/3*LEFT)

		H_6 = TextMobject("3", color = WHITE)
		H_6.shift(-6/3*UP + 2/3*RIGHT)

		H_7 = TextMobject(" ", color = WHITE)
		H_7.shift(-6/3*UP +4/3*RIGHT)

		H_8 = TextMobject(" ", color = WHITE)
		H_8.shift(-6/3*UP + 6/3*RIGHT)

		H_9 = TextMobject(" ", color = WHITE)
		H_9.shift(-6/3*UP + 8/3*RIGHT)
		row_8 = [H_1, H_2, H_3, H_4, H_5, H_6, H_7, H_8, H_9]


		I_1 = TextMobject("3", color = WHITE)
		I_1.shift(-8/3*UP+8/3*LEFT)

		I_2 = TextMobject("1", color = WHITE)
		I_2.shift(-8/3*UP+6/3*LEFT) 

		I_3 = TextMobject(" ", color = WHITE)
		I_3.shift(-8/3*UP + 4/3*LEFT)

		I_4 = TextMobject(" ", color = WHITE)
		I_4.shift(-8/3*UP + 2/3*LEFT)

		I_5 = TextMobject(" ", color = WHITE)
		I_5.shift(-8/3*UP + 0/3*LEFT)

		I_6 = TextMobject("4", color = WHITE)
		I_6.shift(-8/3*UP + 2/3*RIGHT)

		I_7 = TextMobject("7", color = WHITE)
		I_7.shift(-8/3*UP +4/3*RIGHT)

		I_8 = TextMobject("5", color = WHITE)
		I_8.shift(-8/3*UP + 6/3*RIGHT)

		I_9 = TextMobject(" ", color = WHITE)
		I_9.shift(-8/3*UP + 8/3*RIGHT)
		row_9 = [I_1, I_2, I_3, I_4, I_5, I_6, I_7, I_8, I_9]
		final_sudoku = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

		self.add(big_square, normal_square, small_square)
		for row in final_sudoku:
			for entry in row:
				self.add(entry)

		self.wait()
