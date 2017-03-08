import json
import os


def execute_syscall():
    '''
    Executes a system call, returns json.
    '''
    syscall = "speedtest-cli --json"
    return json.loads(os.popen(syscall).read())


def main():
    response = execute_syscall()
    print(json.dumps(response, indent=4))


if __name__ == '__main__':
    main()
