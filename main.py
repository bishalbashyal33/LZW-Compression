def compress(data):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    pattern = ""
    for symbol in data:
        pattern_plus_symbol = pattern + symbol
        if pattern_plus_symbol in dictionary:
            pattern = pattern_plus_symbol
        else:
            result.append(dictionary[pattern])
            dictionary[pattern_plus_symbol] = len(dictionary)
            pattern = symbol
    if pattern:
        result.append(dictionary[pattern])
    return result

def decompress(data):
    dictionary = {i: chr(i) for i in range(256)}
    result = ""
    pattern = chr(data.pop(0))
    result += pattern
    for code in data:
        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = pattern + pattern[0]
        else:
            raise ValueError("Bad compressed code")
        result += entry
        dictionary[len(dictionary)] = pattern + entry[0]
        pattern = entry
    return result


uncompressed_data = "ABAABABAABAB"
compressed_data = compress(uncompressed_data)
decompressed_data = decompress(compressed_data)
print(f"Uncompressed size: {len(uncompressed_data)} bytes")
print(f"Compressed size: {len(compressed_data)} bytes")
print(f"Compressed data: {compressed_data}")
print(f"DeCompressed data: {decompressed_data}")


