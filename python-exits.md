## Python Exits

### exit()
allowed to be replaced with other things by tools  
it works only if the site module is imported, so should be used in the interpreter only


### quit()
exit() synonym, made to make python more user friendly
has same specificities as exit()


### sys.exit()
exit cleanly/consistently, generally supposed to stay untouched
sys module is always available
> [!IMPORTANT]
> mostly prefered


### os._exit()
'unclean' exit, terminate abruptly -> kill workers in multiprocessing, avoid invoking cleanup
> [!WARNING]
> immediate exit   
