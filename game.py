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

		elif inStr == 's' or inStr == 'S':
			print("-----your score-----")
			# TODO: show score list

		elif inStr == 'm' or inStr == 'M':
			print("please change game mode")
			print("easy mode: type 'e' | middle mode: type 'm' | hard mode: type 'h'")
			inMode = raw_input("please type game mode:")
			if inMode == 'e' or inMode == 'E':
				mode = "easy"
			elif inMode == 'm' or inMode == 'M':
				mode = "middle"
			elif inMode == 'h' or inMode == 'H':
				mode = "hard"
			else:
				print("sorry, your type is " + inMode + ". this is no matching..." )
		elif inStr == 'g' or inStr == 'G':
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
