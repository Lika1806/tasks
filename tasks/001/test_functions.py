def test(text):
    print(f'\n_________{text}_________')

def done():
    print('the test was passed')

def print_result(text = 'RESULT'):
    RESULT_TEXT = '\033[1;34m'
    RESET = '\033[1;0m'
    print(f'{RESULT_TEXT}{text}{RESET}')
class Test:

    GREEN = '\033[1;92m'
    RED = '\033[1;91m'
    YELLOW = '\033[1;93m'
    RESET = '\033[1;0m'
    def __init__(self, text = 'testing', *, expect_error = False) -> None:
        self.text = text
        self.expect_error = expect_error

    def __enter__(self):
        print(f'\n{self.YELLOW}<<<<{self.text}>>>>{self.RESET}')
    
    def __exit__(self, exc_type,exc_value, traceback):
        if exc_type is not None:
            print(f'{self.RED}{exc_value}{self.RESET}')
            if self.expect_error:
                print(f'{self.GREEN}>>>>test is passed successfully<<<<{self.RESET}')
                return True
            else:
                print(f'{self.RED}>>>>test failed<<<<{self.RESET}')
                return
        print(f'{self.GREEN}>>>>test is passed successfully<<<<{self.RESET}')