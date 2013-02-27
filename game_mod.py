#! /usr/bin/python
# -*- coding:utf-8 -*-

# Copyright 2013 Kenta Komai
# coding by Kenta Komai

import random

MENU_SELECT_EXIT = 'e'
MENU_SELECT_SCORE = 's'
MENU_SELECT_MODE = 'm'
MENU_SELECT_GAME = 'g'

MODE_SELECT_VERY_EASY_1 = 've1'
MODE_SELECT_VERY_EASY_2 = 've2'
MODE_SELECT_EASY = 'e'
MODE_SELECT_MIDDLE = 'm'
MODE_SELECT_HARD = 'h'

MODE_VERY_EASY_1 = "very easy(only upper)"
MODE_VERY_EASY_2 = "very easy(only lower)"
MODE_EASY = "easy"
MODE_MIDDLE = "middle"
MODE_HARD = "hard"


def check_selected_menu(input_type):
	if input_type == MENU_SELECT_EXIT:
		# exit script
		print("thank you playing! bye :) ")
		exit()

	elif input_type == MENU_SELECT_SCORE:
		show_score()

	elif input_type == MENU_SELECT_MODE:
		change_geme_mode()

	elif input_type == MENU_SELECT_GAME:
		game(mode)


def change_geme_mode():
	print("please change game mode")
	print("very easy mode(only upper alphabet): type 've1' | very easy mode(only lower alphabet): type 've2' | easy mode: type 'e' | middle mode: type 'm' | hard mode: type 'h'")

	inMode = raw_input("please type game mode: ")
	if inMode == MODE_SELECT_VERY_EASY_1:
		return_mode = MODE_VERY_EASY_1

	elif inMode == MODE_SELECT_VERY_EASY_2:
		return_mode = MODE_VERY_EASY_2

	elif inMode == MODE_SELECT_EASY:
		return_mode = MODE_EASY

	elif inMode == MODE_SELECT_MIDDLE:
		return_mode = MODE_MIDDLE

	elif inMode == MODE_SELECT_HARD:
		return_mode = MODE_HARD

	else:
		print("sorry, your type is " + inMode + ". this is no matching..." )

	return return_mode


def show_score():
	print("-----your score-----")
	# TODO: show score list


def game_start(mode):
	print("hoge")
	# start game
	correct = 0;
	failed = 0

	if mode == "easy":
		start = 65
		end = 122
	elif mode == "middle":
		start = 48
		end = 126
	elif mode == "hard":
		start = 33
		end = 126
	elif mode == "very easy(only upper)":
		start = 65
		end = 90
	elif mode == "very easy(only lower)":
		start = 97
		end = 122

	for i in range(10):
		ch = chr(random.randint(start, end))
		ans = raw_input("is " + str(ord(ch)) + ":" + str(hex(ord(ch))) + " be ascii charset? :")
		if ans == ch:
			print "GREAT!"
			correct+=1
		else:
			print "Failed...answer is " + str(ch)
			failed+=1
	print("your score is correct:" + str(correct) + " | failed:" + str(failed))
	save_result()


def save_result():
	print("game result saving ok.")


def main():
	print("----ASCII charset Memory Game----")
	print("ver 0.1")
	print("auther: KentaKomai")
	print("url: http://tamago.servehttp.com")
	print("")

	mode = "middle"

	print("<usage>")
	print("start game: type 'g' | show score: type 's' | change game mode: type 'm' | exit this script: type 'e'")
	print("game mode: " + mode)

	while(True):
		input_type = raw_input("please type key from menu: ")
		if input_type == MENU_SELECT_EXIT:
			# exit script
			print("thank you playing! bye :) ")
			exit()

		elif input_type == MENU_SELECT_SCORE:
			show_score()

		elif input_type == MENU_SELECT_MODE:
			mode = change_geme_mode()
			print("mode was changed to \"" + mode + "\"")

		elif input_type == MENU_SELECT_GAME:
			game_start(mode)


if __name__ == "__main__":
	main()
