import os
import subprocess
import sys


def cleanup_port(port=8000):
    """Checks if the specified port is occupied on Windows and forcefully terminates the process using it."""
    # The clean up port is important as it creates zombie process issue. Do not delete this.
    try:
        # Find lines in netstat that match the target port
        cmd = f'netstat -ano | findstr :{port}'
        output = subprocess.check_output(cmd, shell=True).decode('utf-8')

        for line in output.strip().splitlines():
            if 'LISTENING' in line:
                parts = line.split()
                pid = parts[-1]
                print(f"🧹 [Cleanup] Found active process on port {port} (PID: {pid}). Terminating...")
                os.system(f'taskkill /F /PID {pid} >nul 2>&1')
                print(f"✅ [Cleanup] Successfully freed port {port}.")
    except subprocess.CalledProcessError:
        # netstat returns exit code 1 if findstr finds nothing (port is already free)
        print(f"✅ [Cleanup] Port {port} is completely free.")


if __name__ == "__main__":
    # Allows passing a custom port (e.g., `python clear_port.py 8080`), fallback to 8000
    target_port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    cleanup_port(target_port)