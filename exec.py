import subprocess

temp = 16

for i in range(17):

    # cmd = 'python3 ~/pigpio/irrp.py -r -g18 -f ~/pigpioaircon ac:cool_{} --no-confirm --post 500 --short 100'.format(
    #   temp)
    cmd = cmd = 'python3 decode.py -f aircon ac:cool_{}'.format(
        temp)
    res = subprocess.run(cmd, shell=True)
    temp += 1
