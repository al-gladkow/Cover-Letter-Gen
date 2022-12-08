# Cover Letter Generator


if __name__ == '__main__':

    # Imports

    import os
    import sys
    import json
    from pathlib import Path

    args = sys.argv

    inputs_path = None

    if len(args) > 0:
        inputs_path = Path(args[0])
        
    else:
        inputs_path = Path(input('Please enter the name of the inputs file: '))
        
    try:
        with open(file= inputs_path, mode='r'):
            
    except:
        