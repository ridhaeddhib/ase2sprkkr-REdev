import sys

def main():
    from ase2sprkkr.sprkkr.calculator import SPRKKR
    import os
    
    print("Starting SPRKKR calculation...")
    
    try:
        # Initialize calculator
        calculator = SPRKKR()
        
        # Set input parameters
        print("Setting up input parameters...")
        calculator.input_parameters = 'jxc'
        calculator.input_parameters.CONTROL.DATASET = 'Fe'
        #calculator.input_parameters.MODE.MDIR = [1.0, 0.0, 0.0]  # Using floats instead of integers
        #calculator.input_parameters.MODE.MALF = 0.0
        #calculator.input_parameters.MODE.MBET = 45.0
        #calculator.input_parameters.MODE.MGAM = 0.0
        current_dir = os.getcwd()
        
        try:
            result = calculator.calculate(potential='Fe.pot_new')
                
        except Exception as e:
            print(f"Error during calculation: {str(e)}")
            raise
        
    except Exception as e:
        print(f"Error during calculation: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    main()

