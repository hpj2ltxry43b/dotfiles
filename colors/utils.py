
def chunkOut(contents, startmarker, endmarker, replacement):
    contents = str(contents)
    startin = contents.find(startmarker)
    endin   = contents.find(endmarker  )

    if startin == -1:
        raise Exception(f'Start marker {startmarker} not found in contents')

    if endin == -1:
        raise Exception(f'End marker {endmarker} not found in contents')

    contents = contents[:startin + len(startmarker)] + replacement + contents[endin:]

    return contents
