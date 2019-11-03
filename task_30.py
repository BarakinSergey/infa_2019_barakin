#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
	n=0
	while not wall_is_on_the_right():
		move_right()
		n+=1
	while not wall_is_on_the_left():
		move_left()
	for i in range(n):
		for j in range(n):
			if i==j or i==n-j:
				move_right()
			else:
				fill_cell()
				move_right()	
		move_down()
		if not wall_is_beneath():
			fill_cell()
		while not wall_is_on_the_left():
			move_left()
	for i in range(n-1):
		move_right()
		fill_cell()
	while not wall_is_on_the_left():
			move_left()
			
			
if __name__ == '__main__':
    run_tasks()
