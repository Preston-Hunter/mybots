import os

constants_name = "constants.py"
without_cpg_name = "constants_no_cpg.py"
with_cpg_name = "constants_cpg.py"


def rename_constants_to_constants_with_cpg():
    os.system("rename " + constants_name + " " + with_cpg_name)
    os.system("rename " + without_cpg_name + " " + constants_name)


def rename_constants_to_constants_without_cpg():
    os.system("rename " + constants_name + " " + without_cpg_name)
    os.system("rename " + with_cpg_name + " " + constants_name)

def swap_names():
    if os.path.exists(constants_name):
        cpg_exists = os.path.exists(with_cpg_name)
        without_cpg_exists = os.path.exists(without_cpg_name)
        if cpg_exists and not without_cpg_exists:
            rename_constants_to_constants_without_cpg()
            return True
        elif without_cpg_exists and not cpg_exists:
            rename_constants_to_constants_with_cpg()
            return True
    return False
