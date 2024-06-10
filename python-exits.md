# Python Exits

"The exit() "built-in" (it's not actually a built-in all the time; e.g. it won't exist when Python is run with the -S switch) is the wrong solution; 
you want sys.exit() (which does in fact exit cleanly/consistently), not exit() (which is allowed to be replaced with weird things by tools, 
where sys.exit is generally supposed to stay untouched). The "unclean exit" function is os._exit(), which does terminate abruptly (it's used largely to kill workers 
in fork-based multiprocessing scenarios to avoid invoking cleanup that the parent process set up before the fork)."
- <cite>StackOverflow</cite>

## exit()
allowed to be replaced with other things by tools

## sys.exit()
exit cleanly/consistently, generally supposed to stay untouched

## os._exit()
'unclean' exit, terminate abruptly -> kill workers in multiprocessing, avoid invoking cleanup
