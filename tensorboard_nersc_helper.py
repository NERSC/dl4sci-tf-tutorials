import os, pwd
from tensorboard import notebook
import getpass
from IPython.core.display import display, HTML

def get_pid_owner(pid):
    # the /proc/PID is owned by process creator
    proc_stat_file = os.stat("/proc/%d" % pid)
    # get UID via stat call
    uid = proc_stat_file.st_uid
    # look up the username from uid
    username = pwd.getpwuid(uid)[0]
    
    return username

def get_tb_port(username):
    
    for tb_nb in notebook.manager.get_all():
        if get_pid_owner(tb_nb.pid) == username:
            return tb_nb.port
    
def show_tb_address():
    
    username = getpass.getuser()
    tb_port = get_tb_port(username)
    
    address = "https://jupyter-dl.nersc.gov/user/" + "username" + "/proxy/" + str(tb_port) + "/"
    address = address.strip()
    
    display(HTML('<a href="%s">%s</a>'%(address,address)))
