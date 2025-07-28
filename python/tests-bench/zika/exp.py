import os, subprocess, re
from datetime import datetime

def run(cmd):    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = [ b.decode('UTF-8') for b in process.communicate() ]
    
    if error.strip() != "":
        print(error)

    print(out)

def __do_runNSave(cmd, out_path, ret_times, get_times_eye=True):
     # result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = [ b.decode('UTF-8') for b in process.communicate() ]
    out = out.rstrip()
    # print("out:", out)
    # print("error:", error)
        
    with open(out_path, 'w') as fh:
        fh.write(out)
    
    if "** ERROR **" in error:
        print("ERROR:", error)
    
    elif get_times_eye:
        netw_time = int(re.search("networking \d+ \[msec cputime\] (\d+) \[msec walltime\]", error).group(1))
        reas_time = int(re.search("reasoning \d+ \[msec cputime\] (\d+) \[msec walltime\]", error).group(1))
        ret_times.append(netw_time); ret_times.append(reas_time)
        # return netw_time, reas_time

def runNSave_timed(cmd, out_path, max_time, get_times_eye=True):
    mngr = multiprocess.Manager()
    ret_times = mngr.list()
    
    p = multiprocess.Process(target=__do_runNSave, args=(cmd, out_path, ret_times, get_times_eye))
    p.start()
    
    p.join(max_time)
    if p.is_alive():
        p.kill()
        return (-1, -1)
    else:
        return ret_times
        
def runNSave(cmd, out_path, get_times_eye=True):
   ret_times = []
   __do_runNSave(cmd, out_path, ret_times, get_times_eye)
   
   return ret_times

def record_eye(times_file, run, query, data, netw_time, reas_time):
    times_file.write(f"{run},{query},{data},{netw_time},{reas_time}\n")