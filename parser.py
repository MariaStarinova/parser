
import json
import sys

if len(sys.argv) != 5:
    print("Usage: python program.py input_file output_file timestamp_start timestamp_end")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
timestamp_start = int(sys.argv[3])
timestamp_end = int(sys.argv[4])

timestamp_start = (timestamp_start//1000) * 1000
timestamp_end = ((timestamp_end//1000)+1) * 1000

found_data = False

with open(input_file, "r") as f:
    for stri in f:
        try:
            str = json.loads(stri)
            if 'timestamp' in str:
                if int(str['timestamp']) > timestamp_start and int(str['timestamp']) < timestamp_end:
                    with open(output_file, "a") as o:
                        o.write(stri)
                    found_data = True
            if 'currentTimeMs' in str:
                if int(str['currentTimeMs']) > timestamp_start and int(str['currentTimeMs']) < timestamp_end:
                    with open(output_file, "a") as o:
                        o.write(stri)
                    found_data = True
        except json.decoder.JSONDecodeError:
            pass

if not found_data:
    print("No data found in file")
else:
    print(f"Filtered data saved to {output_file}")

f.close()






