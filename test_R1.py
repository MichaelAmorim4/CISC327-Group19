import tempfile
from importlib import reload
import os
import io
import sys
import src.main as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R1.1 by checking if the output is correct for when logged in
def test_r1_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        expected_output_transactions=[
        ]
    )

#tests all of R1.2 by checking if the output is correct for when not logged in
def test_r1_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        expected_output_transactions=[
        ]
    )

#goes to all pages fails something to get sent back to landing and then goes to another
def test_r1_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            '123',
            "login",
            'aaa@gmail.com',
            'aaa45',
            'buy',
            ' ',
            'sell',
            ' ',
            'update',
            '%',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: '
            'Email format is incorrect',
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            "---BUY---",
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---UPDATE---',
            'Enter the ticket name: Name is invalid',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        expected_output_transactions=[
        ]
    )

#tests when an invalid input is sent when not logged in
def test_r1_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'a',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            "Command invalid",
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        expected_output_transactions=[
        ]
    )

#tests when in invalid input is sent on the login screen
def test_r1_5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'a',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Command invalid',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        expected_output_transactions=[
        ]
    )

#test that command invalid when user is logged in
def test_r2_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'register',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Command invalid',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        expected_output_transactions=[]
    )

# start registration if command is valid
def test_r2_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            ' ',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        expected_output_transactions=[]
    )

# should ask for email, user name, password, password2
def test_r2_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'zzz@gmail.com',
            'zzzzz',
            'Zz.45',
            'Zz.45',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Confirm your password: Account registered',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        expected_output_transactions=[]
    )

def helper(
        capsys,
        terminal_input,
        input_valid_accounts,
        input_valid_tickets,
        expected_tail_of_terminal_output,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        input_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(input_valid_accounts))

    # temp file to store ticket list
    temp_fd3, temp_file3 = tempfile.mkstemp()
    valid_ticket_list_file = temp_file3
    with open(valid_ticket_list_file, 'w') as wf:
        wf.write('\n'.join(input_valid_tickets))

    # prepare program parameters
    sys.argv = [
        'main.py',
        'testCity',
        valid_account_list_file,
        valid_ticket_list_file
    ]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()
    
    # print out the testing information for debugging
    # the following print content will only display if a 
    # test case failed:
    print()
    print('STD.IN:', terminal_input)
    print('VALID ACCOUNTS:', input_valid_accounts)
    print('VALID TICKETS: ', input_valid_tickets)
    print()
    # formatted output comparison
    outLen = len(out_lines)
    expLen = len(expected_tail_of_terminal_output)
    endInd = outLen-expLen
    formatShort = '\033[91m'+'{:<1s}'+'\x1b[0m'+'{:<35.34s}{:<35.35s}'
    formatLong = '\033[91m'+'{:<1s}'+'\x1b[0m'+'{:<80.79s}{:<80}'
    
    #-------- CHANGE FormatShort to FormatLong if outputs are cut off. Widen the console.
    formatStr = formatShort
    #------------------------
    print(formatStr.format('', 'EXPECTED:', 'STD.OUT:'))
    print('===============================================')
    if (endInd > 0):
        for i in range(expLen):
            print(formatStr.format('' if expected_tail_of_terminal_output[i] == out_lines[i] else '*', expected_tail_of_terminal_output[i], out_lines[i]))
        for o in range(expLen, outLen):
            print(formatStr.format('', '', out_lines[o]))
    elif (endInd < 0):
        for i in range(outLen):
            print(formatStr.format('' if expected_tail_of_terminal_output[i] == out_lines[i] else '*', expected_tail_of_terminal_output[i], out_lines[i]))
        for e in range(outLen, expLan):
            print(formatStr.format('', expected_tail_of_terminal_output[i], ''))
    else:
        for i in range(outLen):
            print(formatStr.format('' if expected_tail_of_terminal_output[i] == out_lines[i] else '*', expected_tail_of_terminal_output[i], out_lines[i]))
    
    # print('terminal output:', out_lines)
    # print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]
    
    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read().splitlines()
        
        # print out the testing information for debugging
        # the following print content will only display if a 
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_output_transactions)
        
        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    # remove transaction file
    os.remove(sys.argv[1]+'_transactions.csv')