
try:
        a, b = input("Enter two numbers, separated by a comma: ").split()
        a = int()
        print('try succeed')      
    except IndexError:
        result = 0
        print('Index out of range')
    except:        # run if other exception is raised
        result = 0
        print('other exception')
    else:          # run if no exception raised
        print('no exception raised')
    finally:       # always run regardless of whether exception is raised
        print('run finally')