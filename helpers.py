def copy(src, dest, size):
    while size > 0:
        bytes = size
        if bytes > 65536:
            bytes = 65536
        block = src.read(bytes)
        if not block:
            break
        dest.write(block)
        size -= len(block)
    return size
