import subprocess


def run_command(cmd, get_output=False):
    "run command"

    if get_output == False:

        process = subprocess.Popen(cmd)

        process.wait()

    else:

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # wait for the process to terminate
        stdout, stderr = process.communicate()

        stdout = stdout.decode('UTF-8').strip()
        stderr = stderr.decode('UTF-8').strip()

        return stdout, stderr, process.returncode
