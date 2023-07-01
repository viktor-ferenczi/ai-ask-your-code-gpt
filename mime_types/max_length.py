# Official list: https://www.iana.org/assignments/media-types/media-types.xhtml

import os
import csv


def iter_len(rdr, fi):
	for row in rdr:
		if row and ''.join(row).strip():
			yield len(row[fi])


for fn in sorted(os.listdir('.')):
	if not fn.endswith('.csv'):
		continue
	with open(fn, 'rt', encoding='utf-8') as f:
		rdr = csv.reader(f)
		for header in rdr:
			break
		ml = max(iter_len(rdr, 1))
		print(fn, ml)
