#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
	c=0
	while wall_is_on_the_right()==False and c<3:
		if cell_is_filled()==True:
			co=c+1
			c=co
		if cell_is_filled()==False:
			c=0
		if c<3:
			move_right()

if __name__ == '__main__':
    run_tasks()
