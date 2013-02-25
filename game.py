#! /usr/bin/python
# -*- coding:utf-8 -*-

import random

if __name__ == "__main__":
	print("----ASCII charset Memory Game----")
	print("ver 0.1")
	print("auther: KentaKomai")
	print("url: http://tamago.servehttp.com")
	print("")

	mode = "middle"

	while(True):
		print("<usage>")
		print("start game: type 'g' | show score: type 's' | change game mode: type 'm' | exit this script: type 'e'")
		print("game mode: " + mode)
		inStr = raw_input("please type key:")

		if inStr == 'e' or inStr == 'E':
			# exit script
			print("thank you playing! bye :) ")
			exit()

		if inStr == 's' or inStr == 'S':
			print("-----your score-----")
			# TODO: show score list

		if inStr == 'm' or inStr == 'M':
			print("please change game mode")
			print("easy mode: type 'e' | middle mode: type 'm' | hard mode: type 'h'")
			inMode = raw_input("please type game mode:")
			if inMode == 'e' or inMode == 'E':
				mode = "easy"
			if inMode == 'm' or inMode == 'M':
				mode = "middle"
			if inMode == 'h' or inMode == 'H':
				mode = "hard"
			else:
				print("sorry, your type is " + inMode + ". this is no matching..." )
		if inStr == 'g' or inStr == 'G':
			# start game
			print(inStr) # for debug
