import os
import subprocess
import pickle
import yaml
import marshal

# Single-line comment: unsafe functions below
"""
Block comment / docstring:
subprocess.Popen(["ls","-l"], shell=True)
pickle.loads(data)
"""

def main():
    # vulnerable: input() in Python 2 style (simulate)
    user = input("Username: ")

    # vulnerable: eval()
    result = eval("2 + 2")

    # vulnerable: exec()
    exec("print('exec called')")

    # vulnerable: os.system()
    os.system("echo test")

    # vulnerable: subprocess.Popen with shell=True
    subprocess.Popen("ls -la", shell=True)

    # vulnerable: pickle.loads
    data = open("dump.pkl", "rb").read()
    obj = pickle.loads(data)

    # vulnerable: marshal.loads
    obj2 = marshal.loads(data)

    # vulnerable: os.popen
    stream = os.popen("whoami")

    # vulnerable: commands.getoutput (Python 2)
    # output = commands.getoutput("pwd")

    # vulnerable: yaml.load
    y = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)

    # vulnerable: compile()
    code_obj = compile("print('compiled')", "<string>", "exec")
    exec(code_obj)

    # vulnerable: str.format injection
    s = "{user}".format(user=user)

    print("Done.")

if __name__ == "__main__":
    main()