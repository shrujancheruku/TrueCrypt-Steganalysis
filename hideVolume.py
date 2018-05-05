import sys
import os
import helpers
import Atom from atom

def analyze(file):
	flag = True
    atoms = {}
    offset = 0

    while flag is True:
        try:
            atom = Atom(file, offset)
        except EOFError:
            break
        if atom.atom in ('ftyp', 'moov', 'mdat'):
			atoms[atom.atom] = atom
        offset = atom.end

def embed(src, dest):

    ftyp, moov, mdat = analyze(src)

    dest.seek(0, 2)
    eof_pos = dest.tell() - 131072
    dest.seek(eof_pos)
    mdat.copy(src, dest, payload_only=True)
    mdat_end = dest.tell()
    moov.copy_moov(src, dest, eof_pos - mdat.offset - 8)

    head = ftyp.read(src) + "\0\0\0\x08free"
    dest.seek(0)
    dest.write(head)

    remain = 65536 - len(head)
    if remain >= 0:
        src.seek(mdat.offset + 8)
        dest.write(src.read(remain))

    return 0

if __name__ == "__main__":

    ext = os.path.splitext(src)[-1][1:].lower()
    src = open(src, "rb")
    dest = open(dest, "r+b")

    sys.exit(main(src, dest))
