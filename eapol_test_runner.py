import subprocess
import time
import re
import os
from datetime import datetime

def measure_eap_phases(eapol_test_path, config_file, radius_ip, secret, timeout=30):
    cmd = [eapol_test_path, '-c', config_file, '-a', radius_ip, '-s', secret, '-t', str(timeout)]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    handshake_time = None
    total_time = None
    log_lines = []

    for line in proc.stdout:
        log_lines.append(line)
        # Look for TLS handshake completion
        if 'Handshake finished' in line or 'TLS done' in line:
            handshake_time = time.time() - start_time
        # Look for final SUCCESS
        if re.search(r'EAP authentication completed|SUCCESS', line):
            total_time = time.time() - start_time
    
    proc.wait()
    end_time = time.time()
    if total_time is None:
        total_time = end_time - start_time
    
    log_dir = "eap_logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"eap_test_log_{timestamp}.txt")

    with open (log_file, 'w') as f:
        # Summarize metrics
        f.write(f"Start Time: {datetime.fromtimestamp(start_time)}\n")
        if handshake_time:
            f.write(f"Handshake Time: {handshake_time:.2f} seconds\n")
        f.write(f"Total Authentication Time: {total_time:.2f} seconds\n")
        f.write("\nKey Log Snippets:\n\n")

        important_keywords = [
            'EAPOL: SUPP_PAE entering state',
            'EAPOL: SUPP_BE entering state',
            'EAP authentication completed',
            'EAP: EAP entering state',
            'EAP-Response',
            'EAP-Request',
            'Handshake',
            'SUCCESS',
            'FAILURE',
            'timeout'
        ]

        for line in log_lines:
            if any(keyword in line for keyword in important_keywords):
                f.write(line.strip() + "\n")




if __name__ == "__main__":
    measure_eap_phases(
        eapol_test_path='eapol_test',
        config_file='ttls-pap.conf',
        radius_ip='127.0.0.1',
        secret='symbol123',
        timeout=30
    )
