def repeat_to_length(string_to_expand, length):
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]

LARGE_DATA = {'details': repeat_to_length('abcdefgh', 256 * 1024)}
STANDARD_DATA = {
    'doc_type': 'ASSIGNMENT OIL & GAS LEASE',
    'instrument_id': '3029847',
    'recording_date': '07/03/2008 12:51:00 PM',
    'document_date': '06/25/2008 12:00:00 AM',
    'page_count': '3',
    'book_number': '',
    'page_number': '',
    'grantors': [
        'JOHN H. HOLT OIL PROPERTIES, INC.'
    ],
    'grantees': [
        'WOODSTONE RESOURCES, L.L.C.',
        'HOLT, JOHN TRUSTEE - LESSOR',
        'RENZ, DEBRA TRUSTEE - LESSOR',
        'HOLT, JANET L. MALLOY TRUST - LESSOR',
        'HOLT, JOHN H. - LESSOR',
        'RENZ, DEBRA HOLT - LESSOR',
        'MAAS, SUSAN HOLT - LESSOR',
        'EVARTS, SALLY HOLT - LESSOR',
        'JOHN H. HOLT OIL PROPERTIES, INC. - LESS'
    ],
    'return_address':
    'WOODSTONE RESOURCES, LLC\n7500 SAN FELIPE STREET, SUITE 475\n\nHOUSTON, TX 77063',
    'url': 'http://ndrinweb3.hplains.state.nd.us/recordernew/eagleweb/viewDoc.jsp?node=DOC1519106',
    'site': 'ndrin.document',
    'indexes': [
        '/ND/DUNN/143N-95W/21'
    ],
    'raw_legals': [
        'Quarter: NW Section: 21 Township: 143 Range: 95  Parcel:',
        'Quarter: SW Section: 21 Township: 143 Range: 95  Parcel:',
        'Quarter: SE Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: NW Quarter: NW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: NE Quarter: NW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: SW Quarter: NW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: SE Quarter: NW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: NW Quarter: SW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: NE Quarter: SW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: NW Quarter: SE Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: NE Quarter: SE Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: SW Quarter: SW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: SE Quarter: SW Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: SW Quarter: SE Section: 21 Township: 143 Range: 95  Parcel:',
        'Sixteenth: SE Quarter: SE Section: 21 Township: 143 Range: 95  Parcel:'
    ],
    'legals': [
        '/ND/DUNN/143N-95W/21/NW4',
        '/ND/DUNN/143N-95W/21/SW4',
        '/ND/DUNN/143N-95W/21/SE4'
    ],
    'cached': {
        'body_key': 'ndrin/Dunn/Dunn-3029847.html',
        'body_bucket': 'drillbit-upload',
        'doc_key': 'ndrin/Dunn/Dunn-3029847.pdf',
        'doc_bucket': 'drillbit-upload'
    }
}
