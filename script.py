import subprocess
import platform
import os

data_dir = 'data'
output_file = os.path.join(data_dir, 'connections.txt')

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

os_type = platform.system()
print(f"Detected OS: {os_type}")

try:
    if os_type == 'Windows':
        print("Running: netstat -ano")
        result = subprocess.run(['netstat', '-ano'], stdout=subprocess.PIPE, text=True)
        filtered_lines = [line for line in result.stdout.splitlines() if 'ESTABLISHED' in line]
    elif os_type in ['Linux', 'Darwin']:  
        print("Running: ss -ant")
        result = subprocess.run(['ss', '-ant'], stdout=subprocess.PIPE, text=True)
        filtered_lines = [line for line in result.stdout.splitlines() if 'ESTAB' in line]
    else:
        print(f"Unsupported OS: {os_type}")
        exit(1)

    with open(output_file, 'w') as f:
        f.write('\n'.join(filtered_lines))

    print(f"Filtered network connections saved to: {output_file}")

except Exception as e:
    print("Error collecting network data:", e)
    exit(1)

NODE = []
EDGE = []

file_path = os.path.join('data', 'connections.txt')

try:
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
        for l in lines:
            if 'TCP' in l or 'ESTABLISHED' in l or 'ESTAB' in l:
                line = l.split()
                if os_type == 'Windows':
                    if len(line) < 4:
                        continue
                    src = line[1].split(':')
                    dst = line[2].split(':')
                else:
                    if len(line) < 5:
                        continue
                    src = line[3].split(':')
                    dst = line[4].split(':')

                if len(src) == 2 and len(dst) == 2:
                    if src[0] not in ('0.0.0.0', '127.0.0.1') and dst[0] not in ('0.0.0.0', '127.0.0.1'):
                        src_ip = src[0]
                        dst_ip = dst[0]
                        proto = dst[1]
                        internal = False
                        if (
                            dst_ip.startswith('10.') or
                            dst_ip.startswith('192.168.') or
                            (dst_ip.startswith('172.') and 16 <= int(dst_ip.split('.')[1]) <= 32)
                        ):
                            internal = True

                        print(src_ip, dst_ip, proto, internal)

                        if src_ip not in NODE:
                            NODE.append(src_ip)
                        if dst_ip not in NODE:
                            NODE.append(dst_ip)

                        EDGE.append([src_ip, dst_ip, proto, internal])
except Exception as e:
    print("Error processing connection data:", e)
    exit(1)

try:
    with open('NODE.csv', 'w') as fp:
        fp.write('Id,Label,Internal\r\n')
        for N in NODE:
            try:
                internal = False
                if (
                    N.startswith('10.') or
                    N.startswith('192.168.') or
                    (N.startswith('172.') and 16 <= int(N.split('.')[1]) <= 32)
                ):
                    internal = True
                fp.write(f'{N},{N},{internal}\r\n')
            except:
                pass
except Exception as e:
    print("Error writing NODE.csv:", e)

try:
    with open('EDGE.csv', 'w') as fp:
        fp.write('Source,Target,Protocol,Internal,Label,Type,Weight\r\n')
        for E in EDGE:
            fp.write(f'{E[0]},{E[1]},{E[2]},{E[3]},{E[2]},Direct,1.0\r\n')
except Exception as e:
    print("Error writing EDGE.csv:", e)

print("Parsing complete. Files generated: NODE.csv and EDGE.csv")
