#! /usr/bin/python
# -*- coding:utf-8 -*-

import random

if __name__ == "__main__":
	print("----ASCII charset Memory Game----")
	print("ver 0.1")
	print("auther: KentaKomai")
	print("url: http://tamago.servehttp.com")
	print("")

	while(True):
		print("<usage>")
		print("start game: type 'g' | show score: type 's' | exit this script: type 'e'")
		inStr = raw_input("please type key:")

		if inStr == 'e' or inStr == 'E':
			# exit script
			print("thank you playing! bye :) ")
			exit()
		if inStr == 's' or inStr == 'S':
			print("-----your score-----")
			# TODO: show score list
			continue
		if inStr == 'g' or inStr == 'G':
			# start game
			print(inStr) # debug script
		else:
			continue
