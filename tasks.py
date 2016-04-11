from invoke import run, task
import mojimoji

@task
def h2z(filename):
    with open(filename, "r") as f:
        for line in f:
            print(mojimoji.han_to_zen(line), end="")

@task
def z2h(filename):
    with open(filename, "r") as f:
        for line in f:
            print(mojimoji.zen_to_han(line), end="")

@task
def morph(filename, model = "short"):
    if model == "short":
        run("cat %s | /home/shen/Morph/morph -p /home/shen/Morph/data -d CTB5+flat+dic+wikipedia+edr+zh_dict_simple+NICTtr.pyg.v2.clean -m /home/shen/Morph_complementary/model/model.CTB5.NICTtr.pyg.v2.1024ver.zh_dict_simple.asi7.1.dat" % (filename,))  
    elif model == "long":
        run("cat %s | /home/shen/Morph/morph --master-path /home/nakazawa/tool/Morph/data --dics CTB5+flat+dic+wikipedia+edr+NICTtr-1024ver.aplc --model /home/nakazawa/tool/Morph/data/model.c5+nict1024.jun16.dat --unk_max_length 3" % (filename,))
    else:
        raise ValueError("short or long model is supported")
