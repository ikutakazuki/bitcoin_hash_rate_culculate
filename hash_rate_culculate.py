import datetime
import csv
import time

csv_header = ['height', 'utc_time', 'bits', 'hex_bits', 'exponent', 'coefficient', 'difficulty_target', 'bin_difficulty_target', 'computational_complexity', 'hash_rate_tera']

with open('bitcoin_blockheader.csv') as f:
    reader = csv.reader(f)
    header = next(reader)

    with open('bitcoin_hash_rate.csv', 'w') as w:
        writer = csv.writer(w, lineterminator='\n')
        writer.writerow(csv_header)

        for row in reader:
            unix_time = int(row[4])
            bits = int(row[5])
            height = int(row[12])
            hex_bits = hex(bits)
            tz = datetime.timezone.utc
            utc = datetime.datetime.fromtimestamp(unix_time, tz).strftime('%Y-%m-%d %H:%M:%S')
            exponent = hex_bits[2:4]
            coefficient = hex_bits[4:]
            target = int(coefficient, 16) * 2 ** (8 * (int(exponent, 16) - 3))
            bin_target = bin(target)
            computational_complexity = 2 ** (258 - len(bin_target)) / (int(coefficient, 16) / 2 ** (len(bin(int(coefficient, 16))) - 2))
            hash_rate_tera = computational_complexity / 600 / (1000 ** 4)
            list = [height, utc, bits, hex_bits, exponent, coefficient, target, bin_target, computational_complexity, hash_rate_tera]
            writer.writerow(list)
            print(list)