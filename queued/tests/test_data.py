def repeat_to_length(string_to_expand, length):
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]

LARGE_DATA = {'details': repeat_to_length('abcdefgh', 256 * 1024)}
STANDARD_DATA = {
    'doc_type': 'stuff and such',
}
