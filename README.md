# pdfstream
decode / encode pdfstreams (flatdecode)

<p>
# pdfstream - 0.1a - zaphoxx - <br>
[+] init parser.<br>
usage: pdfstream.py [-h] -in FILEIN -out FILEOUT [-encode] [-v]<br>
pdfstream.py: error: the following arguments are required: -in, -out<br>
>>> <br>
</p>
<h3>Decode pdfstream</h3>
<p>
To decode a pdfstream select the data inbetween 'stream' and 'endstream' and save it in a seperate file (input file).<br>
use:
<code>
# pdfstream.py -in FILEIN -out FILEOUT
<code>
<br>
The stream will then be decompressed and saved in FILEOUT.
</p>

<h3>Encode data as pdfstream (flatdecode)</h3>
<p>
To encode same data, save the data in a textfile (input file).<br>
use:
<code>
# pdfstream.py -in FILEIN -out FILEOUT -encode
</code>
<br>
Data will then be compressed (zlib.compress) and saved in FILEOUT.
</p>


