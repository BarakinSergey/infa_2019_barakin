#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    wall=0
    while wall==0:
    	if (wall_is_beneath()==True and wall_is_above()==False):
    		fill_cell()
    	if wall_is_on_the_right()==False:
    		move_right()
    	if wall_is_on_the_right()==True:
    		wall=1
    if (wall_is_beneath()==True and wall_is_above()==False):
    		fill_cell()
    		

if __name__ == '__main__':
    run_tasks()
