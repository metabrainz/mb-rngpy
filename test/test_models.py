import xml.etree.ElementTree as ElementTree

from mbrng import models


def xml_elements_equal(e1, e2):
    if (e1.tag != e2.tag or
            (e1.text or '').strip() != (e2.text or '').strip() or
            (e1.tail or '').strip() != (e2.tail or '').strip() or
            e1.attrib != e2.attrib or
            len(e1) != len(e2)):
        return False
    return all(xml_elements_equal(c1, c2) for c1, c2 in zip(e1, e2))


def test_packaging():
    actual_model = models.packaging(
        id='ec27701a-4a22-37f4-bfac-6616e0f9750a',
        valueOf_='Jewel Case',
    )
    expected_xml_string = '''
    <packaging xmlns="http://musicbrainz.org/ns/mmd-2.0#"
               id="ec27701a-4a22-37f4-bfac-6616e0f9750a"
    >Jewel Case</packaging>
    '''
    assert xml_elements_equal(
        actual_model.to_etree(),
        ElementTree.fromstring(expected_xml_string),
    )
