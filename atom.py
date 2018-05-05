class Atom:
    def __init__(self, atom=None, offset=0, size=0):
        self.offset = offset
        if isinstance(atom, basestring):
            self.atom = atom
            self.size = size
        else:
            atom.seek(offset)
            s = atom.read(8)
            if len(s) < 8:
                raise EOFError("EOF")
            self.size = r_u32(s)
            self.atom = s[4:]
            if not self.size:
                atom.seek(0, 2)
                self.size = atom.tell() - offset
        self.end = self.offset + self.size

    def read(self, file):
        file.seek(self.offset)
        data = file.read(self.size)
        if len(data) != self.size:
            raise IOError("EOF")
        return data

    def copy(self, src, dest, payload_only=False):
        offset = self.offset
        size = self.size
        if payload_only:
            offset += 8
            size -= 8
        src.seek(offset)
        if copy_block(src, dest, size):
            raise IOError("EOF")
