
from invoke import run, task
import mojimoji

@task
def h2z(filename):
    # run("cat %s | perl /home/chu/tools/scripts/z2h.pl" % (filename, ))
    with open(filename, "r") as f:
        for line in f:
            print(mojimoji.han_to_zen(line), end="")

@task
def z2h(filename):
    # run("cat %s | perl /home/chu/tools/scripts/h2z.pl" % (filename, ))
    with open(filename, "r") as f:
        for line in f:
            print(mojimoji.zen_to_han(line), end="")
