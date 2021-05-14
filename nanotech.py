def nanotech(n):
    '''
    In Ray Kurzweil's book The Singularity Is Now, he details how nanotechnology will change the industry of manufacturing. 
    Kurzweil specifies how nanotechnology will enable nanobots to create anything, including other nanobots.
    This script creates a program that shows the amount of nanobots created given that each nanobot creates one or all nanobots help eachother build the next step in unison.
    variable n decides how many nanobots start the process
    '''
    if n >= 3000000:
        print('Simulation complete')
    else:
        print(n)
        nanotech(n+n)


