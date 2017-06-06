#!/usr/bin/env python

#
# Generated Tue Jun  6 14:50:50 2017 by generateDS.py version 2.26a.
#
# Command line options:
#   ('-o', 'mbrng/models.py')
#   ('-s', 'mbrng/mb_mmd_subs.py')
#   ('--super', 'mb')
#   ('--external-encoding', 'utf-8')
#   ('--export', 'write etree')
#
# Command line arguments:
#   musicbrainz_mmd.xsd
#
# Command line:
#   /usr/bin/generateDS.py -o "mbrng/models.py" -s "mbrng/mb_mmd_subs.py" --super="mb" --external-encoding="utf-8" --export="write etree" musicbrainz_mmd.xsd
#
# Current working directory (os.getcwd()):
#   mb-rngpy
#

import sys
from lxml import etree as etree_

import mb as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class def_area_element_innerSub(supermod.def_area_element_inner):
    def __init__(self, id=None, type_=None, type_id=None, name=None, sort_name=None, disambiguation=None, iso_3166_1_code_list=None, iso_3166_2_code_list=None, iso_3166_3_code_list=None, annotation=None, life_span=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, anytypeobjs_=None):
        super(def_area_element_innerSub, self).__init__(id, type_, type_id, name, sort_name, disambiguation, iso_3166_1_code_list, iso_3166_2_code_list, iso_3166_3_code_list, annotation, life_span, alias_list, relation_list, tag_list, user_tag_list, anytypeobjs_, )
supermod.def_area_element_inner.subclass = def_area_element_innerSub
# end class def_area_element_innerSub


class def_track_dataSub(supermod.def_track_data):
    def __init__(self, id=None, position=None, number=None, title=None, length=None, artist_credit=None, recording=None):
        super(def_track_dataSub, self).__init__(id, position, number, title, length, artist_credit, recording, )
supermod.def_track_data.subclass = def_track_dataSub
# end class def_track_dataSub


class metadataSub(supermod.metadata):
    def __init__(self, generator=None, created=None, artist=None, release=None, release_group=None, recording=None, label=None, work=None, area=None, place=None, instrument=None, series=None, event=None, url=None, puid=None, isrc=None, disc=None, rating=None, user_rating=None, collection=None, editor=None, artist_list=None, release_list=None, release_group_list=None, recording_list=None, label_list=None, work_list=None, area_list=None, place_list=None, instrument_list=None, series_list=None, event_list=None, url_list=None, isrc_list=None, annotation_list=None, cdstub_list=None, freedb_disc_list=None, tag_list=None, user_tag_list=None, collection_list=None, editor_list=None, entity_list=None, def_extension_element=None):
        super(metadataSub, self).__init__(generator, created, artist, release, release_group, recording, label, work, area, place, instrument, series, event, url, puid, isrc, disc, rating, user_rating, collection, editor, artist_list, release_list, release_group_list, recording_list, label_list, work_list, area_list, place_list, instrument_list, series_list, event_list, url_list, isrc_list, annotation_list, cdstub_list, freedb_disc_list, tag_list, user_tag_list, collection_list, editor_list, entity_list, def_extension_element, )
supermod.metadata.subclass = metadataSub
# end class metadataSub


class artistSub(supermod.artist):
    def __init__(self, id=None, type_=None, type_id=None, name=None, sort_name=None, gender=None, country=None, area=None, begin_area=None, end_area=None, annotation=None, disambiguation=None, ipi=None, ipi_list=None, life_span=None, alias_list=None, recording_list=None, release_list=None, release_group_list=None, label_list=None, work_list=None, relation_list=None, tag_list=None, user_tag_list=None, rating=None, user_rating=None, def_extension_element=None):
        super(artistSub, self).__init__(id, type_, type_id, name, sort_name, gender, country, area, begin_area, end_area, annotation, disambiguation, ipi, ipi_list, life_span, alias_list, recording_list, release_list, release_group_list, label_list, work_list, relation_list, tag_list, user_tag_list, rating, user_rating, def_extension_element, )
supermod.artist.subclass = artistSub
# end class artistSub


class genderSub(supermod.gender):
    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(genderSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.gender.subclass = genderSub
# end class genderSub


class life_spanSub(supermod.life_span):
    def __init__(self, begin=None, end=None, ended=None):
        super(life_spanSub, self).__init__(begin, end, ended, )
supermod.life_span.subclass = life_spanSub
# end class life_spanSub


class releaseSub(supermod.release):
    def __init__(self, id=None, title=None, status=None, quality=None, annotation=None, disambiguation=None, packaging=None, text_representation=None, artist_credit=None, alias_list=None, release_group=None, date=None, country=None, release_event_list=None, barcode=None, asin=None, cover_art_archive=None, label_info_list=None, medium_list=None, relation_list=None, tag_list=None, user_tag_list=None, collection_list=None, def_extension_element=None):
        super(releaseSub, self).__init__(id, title, status, quality, annotation, disambiguation, packaging, text_representation, artist_credit, alias_list, release_group, date, country, release_event_list, barcode, asin, cover_art_archive, label_info_list, medium_list, relation_list, tag_list, user_tag_list, collection_list, def_extension_element, )
supermod.release.subclass = releaseSub
# end class releaseSub


class statusSub(supermod.status):
    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(statusSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.status.subclass = statusSub
# end class statusSub


class text_representationSub(supermod.text_representation):
    def __init__(self, language=None, script=None):
        super(text_representationSub, self).__init__(language, script, )
supermod.text_representation.subclass = text_representationSub
# end class text_representationSub


class release_groupSub(supermod.release_group):
    def __init__(self, id=None, type_=None, type_id=None, title=None, annotation=None, disambiguation=None, first_release_date=None, primary_type=None, secondary_type_list=None, artist_credit=None, release_list=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, rating=None, user_rating=None, def_extension_element=None):
        super(release_groupSub, self).__init__(id, type_, type_id, title, annotation, disambiguation, first_release_date, primary_type, secondary_type_list, artist_credit, release_list, alias_list, relation_list, tag_list, user_tag_list, rating, user_rating, def_extension_element, )
supermod.release_group.subclass = release_groupSub
# end class release_groupSub


class primary_typeSub(supermod.primary_type):
    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(primary_typeSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.primary_type.subclass = primary_typeSub
# end class primary_typeSub


class secondary_type_listSub(supermod.secondary_type_list):
    def __init__(self, secondary_type=None):
        super(secondary_type_listSub, self).__init__(secondary_type, )
supermod.secondary_type_list.subclass = secondary_type_listSub
# end class secondary_type_listSub


class secondary_typeSub(supermod.secondary_type):
    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(secondary_typeSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.secondary_type.subclass = secondary_typeSub
# end class secondary_typeSub


class recordingSub(supermod.recording):
    def __init__(self, id=None, title=None, length=None, annotation=None, disambiguation=None, video=None, artist_credit=None, release_list=None, alias_list=None, puid_list=None, isrc_list=None, relation_list=None, tag_list=None, user_tag_list=None, rating=None, user_rating=None, def_extension_element=None):
        super(recordingSub, self).__init__(id, title, length, annotation, disambiguation, video, artist_credit, release_list, alias_list, puid_list, isrc_list, relation_list, tag_list, user_tag_list, rating, user_rating, def_extension_element, )
supermod.recording.subclass = recordingSub
# end class recordingSub


class labelSub(supermod.label):
    def __init__(self, id=None, type_=None, type_id=None, name=None, sort_name=None, label_code=None, ipi=None, ipi_list=None, annotation=None, disambiguation=None, country=None, area=None, life_span=None, alias_list=None, release_list=None, relation_list=None, tag_list=None, user_tag_list=None, rating=None, user_rating=None, def_extension_element=None):
        super(labelSub, self).__init__(id, type_, type_id, name, sort_name, label_code, ipi, ipi_list, annotation, disambiguation, country, area, life_span, alias_list, release_list, relation_list, tag_list, user_tag_list, rating, user_rating, def_extension_element, )
supermod.label.subclass = labelSub
# end class labelSub


class workSub(supermod.work):
    def __init__(self, id=None, type_=None, type_id=None, title=None, language=None, language_list=None, artist_credit=None, iswc=None, iswc_list=None, attribute_list=None, annotation=None, disambiguation=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, rating=None, user_rating=None, def_extension_element=None):
        super(workSub, self).__init__(id, type_, type_id, title, language, language_list, artist_credit, iswc, iswc_list, attribute_list, annotation, disambiguation, alias_list, relation_list, tag_list, user_tag_list, rating, user_rating, def_extension_element, )
supermod.work.subclass = workSub
# end class workSub


class placeSub(supermod.place):
    def __init__(self, id=None, type_=None, type_id=None, name=None, disambiguation=None, address=None, coordinates=None, annotation=None, area=None, life_span=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, def_extension_element=None):
        super(placeSub, self).__init__(id, type_, type_id, name, disambiguation, address, coordinates, annotation, area, life_span, alias_list, relation_list, tag_list, user_tag_list, def_extension_element, )
supermod.place.subclass = placeSub
# end class placeSub


class coordinatesSub(supermod.coordinates):
    def __init__(self, latitude=None, longitude=None):
        super(coordinatesSub, self).__init__(latitude, longitude, )
supermod.coordinates.subclass = coordinatesSub
# end class coordinatesSub


class instrumentSub(supermod.instrument):
    def __init__(self, id=None, type_=None, type_id=None, name=None, disambiguation=None, description=None, annotation=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, def_extension_element=None):
        super(instrumentSub, self).__init__(id, type_, type_id, name, disambiguation, description, annotation, alias_list, relation_list, tag_list, user_tag_list, def_extension_element, )
supermod.instrument.subclass = instrumentSub
# end class instrumentSub


class seriesSub(supermod.series):
    def __init__(self, id=None, type_=None, type_id=None, name=None, disambiguation=None, ordering_attribute=None, annotation=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, def_extension_element=None):
        super(seriesSub, self).__init__(id, type_, type_id, name, disambiguation, ordering_attribute, annotation, alias_list, relation_list, tag_list, user_tag_list, def_extension_element, )
supermod.series.subclass = seriesSub
# end class seriesSub


class eventSub(supermod.event):
    def __init__(self, id=None, type_=None, type_id=None, name=None, disambiguation=None, cancelled=None, life_span=None, time=None, setlist=None, annotation=None, alias_list=None, relation_list=None, tag_list=None, user_tag_list=None, rating=None, user_rating=None, def_extension_element=None):
        super(eventSub, self).__init__(id, type_, type_id, name, disambiguation, cancelled, life_span, time, setlist, annotation, alias_list, relation_list, tag_list, user_tag_list, rating, user_rating, def_extension_element, )
supermod.event.subclass = eventSub
# end class eventSub


class urlSub(supermod.url):
    def __init__(self, id=None, resource=None, relation_list=None):
        super(urlSub, self).__init__(id, resource, relation_list, )
supermod.url.subclass = urlSub
# end class urlSub


class discSub(supermod.disc):
    def __init__(self, id=None, sectors=None, offset_list=None, release_list=None, def_extension_element=None):
        super(discSub, self).__init__(id, sectors, offset_list, release_list, def_extension_element, )
supermod.disc.subclass = discSub
# end class discSub


class puidSub(supermod.puid):
    def __init__(self, id=None, recording_list=None, def_extension_element=None):
        super(puidSub, self).__init__(id, recording_list, def_extension_element, )
supermod.puid.subclass = puidSub
# end class puidSub


class isrcSub(supermod.isrc):
    def __init__(self, id=None, recording_list=None, def_extension_element=None):
        super(isrcSub, self).__init__(id, recording_list, def_extension_element, )
supermod.isrc.subclass = isrcSub
# end class isrcSub


class artist_creditSub(supermod.artist_credit):
    def __init__(self, name_credit=None):
        super(artist_creditSub, self).__init__(name_credit, )
supermod.artist_credit.subclass = artist_creditSub
# end class artist_creditSub


class name_creditSub(supermod.name_credit):
    def __init__(self, joinphrase=None, name=None, artist=None):
        super(name_creditSub, self).__init__(joinphrase, name, artist, )
supermod.name_credit.subclass = name_creditSub
# end class name_creditSub


class relationSub(supermod.relation):
    def __init__(self, type_=None, type_id=None, target=None, ordering_key=None, direction=None, attribute_list=None, begin=None, end=None, ended=None, artist=None, release=None, release_group=None, recording=None, label=None, work=None, area=None, place=None, instrument=None, series=None, event=None, def_extension_element=None, source_credit=None, target_credit=None):
        super(relationSub, self).__init__(type_, type_id, target, ordering_key, direction, attribute_list, begin, end, ended, artist, release, release_group, recording, label, work, area, place, instrument, series, event, def_extension_element, source_credit, target_credit, )
supermod.relation.subclass = relationSub
# end class relationSub


class targetSub(supermod.target):
    def __init__(self, id=None, valueOf_=None):
        super(targetSub, self).__init__(id, valueOf_, )
supermod.target.subclass = targetSub
# end class targetSub


class aliasSub(supermod.alias):
    def __init__(self, locale=None, sort_name=None, type_=None, type_id=None, primary=None, begin_date=None, end_date=None, valueOf_=None, mixedclass_=None, content_=None):
        super(aliasSub, self).__init__(locale, sort_name, type_, type_id, primary, begin_date, end_date, valueOf_, mixedclass_, content_, )
supermod.alias.subclass = aliasSub
# end class aliasSub


class tagSub(supermod.tag):
    def __init__(self, count=None, name=None):
        super(tagSub, self).__init__(count, name, )
supermod.tag.subclass = tagSub
# end class tagSub


class user_tagSub(supermod.user_tag):
    def __init__(self, name=None):
        super(user_tagSub, self).__init__(name, )
supermod.user_tag.subclass = user_tagSub
# end class user_tagSub


class ratingSub(supermod.rating):
    def __init__(self, votes_count=None, valueOf_=None):
        super(ratingSub, self).__init__(votes_count, valueOf_, )
supermod.rating.subclass = ratingSub
# end class ratingSub


class label_infoSub(supermod.label_info):
    def __init__(self, catalog_number=None, label=None):
        super(label_infoSub, self).__init__(catalog_number, label, )
supermod.label_info.subclass = label_infoSub
# end class label_infoSub


class mediumSub(supermod.medium):
    def __init__(self, title=None, position=None, format=None, disc_list=None, pregap=None, track_list=None, data_track_list=None):
        super(mediumSub, self).__init__(title, position, format, disc_list, pregap, track_list, data_track_list, )
supermod.medium.subclass = mediumSub
# end class mediumSub


class formatSub(supermod.format):
    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(formatSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.format.subclass = formatSub
# end class formatSub


class annotationSub(supermod.annotation):
    def __init__(self, type_=None, entity=None, name=None, text=None, def_extension_element=None):
        super(annotationSub, self).__init__(type_, entity, name, text, def_extension_element, )
supermod.annotation.subclass = annotationSub
# end class annotationSub


class cdstubSub(supermod.cdstub):
    def __init__(self, id=None, title=None, artist=None, barcode=None, comment=None, track_list=None, def_extension_element=None):
        super(cdstubSub, self).__init__(id, title, artist, barcode, comment, track_list, def_extension_element, )
supermod.cdstub.subclass = cdstubSub
# end class cdstubSub


class freedb_discSub(supermod.freedb_disc):
    def __init__(self, id=None, title=None, artist=None, category=None, year=None, track_list=None, def_extension_element=None):
        super(freedb_discSub, self).__init__(id, title, artist, category, year, track_list, def_extension_element, )
supermod.freedb_disc.subclass = freedb_discSub
# end class freedb_discSub


class collectionSub(supermod.collection):
    def __init__(self, id=None, type_=None, type_id=None, entity_type=None, name=None, editor=None, area_list=None, artist_list=None, event_list=None, instrument_list=None, label_list=None, place_list=None, recording_list=None, release_list=None, release_group_list=None, series_list=None, work_list=None):
        super(collectionSub, self).__init__(id, type_, type_id, entity_type, name, editor, area_list, artist_list, event_list, instrument_list, label_list, place_list, recording_list, release_list, release_group_list, series_list, work_list, )
supermod.collection.subclass = collectionSub
# end class collectionSub


class editorSub(supermod.editor):
    def __init__(self, id=None, name=None, member_since=None, privs=None, gender=None, age=None, homepage=None, bio=None, area=None, language_list=None, edit_information=None):
        super(editorSub, self).__init__(id, name, member_since, privs, gender, age, homepage, bio, area, language_list, edit_information, )
supermod.editor.subclass = editorSub
# end class editorSub


class edit_informationSub(supermod.edit_information):
    def __init__(self, edits_accepted=None, edits_rejected=None, auto_edits_accepted=None, edits_failed=None):
        super(edit_informationSub, self).__init__(edits_accepted, edits_rejected, auto_edits_accepted, edits_failed, )
supermod.edit_information.subclass = edit_informationSub
# end class edit_informationSub


class language_listSub(supermod.language_list):
    def __init__(self, count=None, offset=None, language=None):
        super(language_listSub, self).__init__(count, offset, language, )
supermod.language_list.subclass = language_listSub
# end class language_listSub


class release_eventSub(supermod.release_event):
    def __init__(self, date=None, area=None):
        super(release_eventSub, self).__init__(date, area, )
supermod.release_event.subclass = release_eventSub
# end class release_eventSub


class artist_listSub(supermod.artist_list):
    def __init__(self, count=None, offset=None, artist=None):
        super(artist_listSub, self).__init__(count, offset, artist, )
supermod.artist_list.subclass = artist_listSub
# end class artist_listSub


class medium_listSub(supermod.medium_list):
    def __init__(self, count=None, offset=None, track_count=None, medium=None):
        super(medium_listSub, self).__init__(count, offset, track_count, medium, )
supermod.medium_list.subclass = medium_listSub
# end class medium_listSub


class release_listSub(supermod.release_list):
    def __init__(self, count=None, offset=None, release=None):
        super(release_listSub, self).__init__(count, offset, release, )
supermod.release_list.subclass = release_listSub
# end class release_listSub


class release_group_listSub(supermod.release_group_list):
    def __init__(self, count=None, offset=None, release_group=None):
        super(release_group_listSub, self).__init__(count, offset, release_group, )
supermod.release_group_list.subclass = release_group_listSub
# end class release_group_listSub


class alias_listSub(supermod.alias_list):
    def __init__(self, count=None, offset=None, alias=None):
        super(alias_listSub, self).__init__(count, offset, alias, )
supermod.alias_list.subclass = alias_listSub
# end class alias_listSub


class recording_listSub(supermod.recording_list):
    def __init__(self, count=None, offset=None, recording=None):
        super(recording_listSub, self).__init__(count, offset, recording, )
supermod.recording_list.subclass = recording_listSub
# end class recording_listSub


class data_track_listSub(supermod.data_track_list):
    def __init__(self, count=None, offset=None, track=None):
        super(data_track_listSub, self).__init__(count, offset, track, )
supermod.data_track_list.subclass = data_track_listSub
# end class data_track_listSub


class offset_listSub(supermod.offset_list):
    def __init__(self, count=None, offset_attr=None, offset=None):
        super(offset_listSub, self).__init__(count, offset_attr, offset, )
supermod.offset_list.subclass = offset_listSub
# end class offset_listSub


class offsetSub(supermod.offset):
    def __init__(self, position=None, valueOf_=None):
        super(offsetSub, self).__init__(position, valueOf_, )
supermod.offset.subclass = offsetSub
# end class offsetSub


class label_listSub(supermod.label_list):
    def __init__(self, count=None, offset=None, label=None):
        super(label_listSub, self).__init__(count, offset, label, )
supermod.label_list.subclass = label_listSub
# end class label_listSub


class label_info_listSub(supermod.label_info_list):
    def __init__(self, count=None, offset=None, label_info=None):
        super(label_info_listSub, self).__init__(count, offset, label_info, )
supermod.label_info_list.subclass = label_info_listSub
# end class label_info_listSub


class work_listSub(supermod.work_list):
    def __init__(self, count=None, offset=None, work=None):
        super(work_listSub, self).__init__(count, offset, work, )
supermod.work_list.subclass = work_listSub
# end class work_listSub


class area_listSub(supermod.area_list):
    def __init__(self, count=None, offset=None, area=None):
        super(area_listSub, self).__init__(count, offset, area, )
supermod.area_list.subclass = area_listSub
# end class area_listSub


class place_listSub(supermod.place_list):
    def __init__(self, count=None, offset=None, place=None):
        super(place_listSub, self).__init__(count, offset, place, )
supermod.place_list.subclass = place_listSub
# end class place_listSub


class instrument_listSub(supermod.instrument_list):
    def __init__(self, count=None, offset=None, instrument=None):
        super(instrument_listSub, self).__init__(count, offset, instrument, )
supermod.instrument_list.subclass = instrument_listSub
# end class instrument_listSub


class series_listSub(supermod.series_list):
    def __init__(self, count=None, offset=None, series=None):
        super(series_listSub, self).__init__(count, offset, series, )
supermod.series_list.subclass = series_listSub
# end class series_listSub


class event_listSub(supermod.event_list):
    def __init__(self, count=None, offset=None, event=None):
        super(event_listSub, self).__init__(count, offset, event, )
supermod.event_list.subclass = event_listSub
# end class event_listSub


class url_listSub(supermod.url_list):
    def __init__(self, count=None, offset=None, url=None):
        super(url_listSub, self).__init__(count, offset, url, )
supermod.url_list.subclass = url_listSub
# end class url_listSub


class release_event_listSub(supermod.release_event_list):
    def __init__(self, count=None, offset=None, release_event=None):
        super(release_event_listSub, self).__init__(count, offset, release_event, )
supermod.release_event_list.subclass = release_event_listSub
# end class release_event_listSub


class annotation_listSub(supermod.annotation_list):
    def __init__(self, count=None, offset=None, annotation=None):
        super(annotation_listSub, self).__init__(count, offset, annotation, )
supermod.annotation_list.subclass = annotation_listSub
# end class annotation_listSub


class cdstub_listSub(supermod.cdstub_list):
    def __init__(self, count=None, offset=None, cdstub=None):
        super(cdstub_listSub, self).__init__(count, offset, cdstub, )
supermod.cdstub_list.subclass = cdstub_listSub
# end class cdstub_listSub


class freedb_disc_listSub(supermod.freedb_disc_list):
    def __init__(self, count=None, offset=None, freedb_disc=None):
        super(freedb_disc_listSub, self).__init__(count, offset, freedb_disc, )
supermod.freedb_disc_list.subclass = freedb_disc_listSub
# end class freedb_disc_listSub


class disc_listSub(supermod.disc_list):
    def __init__(self, count=None, offset=None, disc=None):
        super(disc_listSub, self).__init__(count, offset, disc, )
supermod.disc_list.subclass = disc_listSub
# end class disc_listSub


class puid_listSub(supermod.puid_list):
    def __init__(self, count=None, offset=None, puid=None):
        super(puid_listSub, self).__init__(count, offset, puid, )
supermod.puid_list.subclass = puid_listSub
# end class puid_listSub


class isrc_listSub(supermod.isrc_list):
    def __init__(self, count=None, offset=None, isrc=None):
        super(isrc_listSub, self).__init__(count, offset, isrc, )
supermod.isrc_list.subclass = isrc_listSub
# end class isrc_listSub


class relation_listSub(supermod.relation_list):
    def __init__(self, target_type=None, count=None, offset=None, relation=None):
        super(relation_listSub, self).__init__(target_type, count, offset, relation, )
supermod.relation_list.subclass = relation_listSub
# end class relation_listSub


class tag_listSub(supermod.tag_list):
    def __init__(self, count=None, offset=None, tag=None):
        super(tag_listSub, self).__init__(count, offset, tag, )
supermod.tag_list.subclass = tag_listSub
# end class tag_listSub


class iswc_listSub(supermod.iswc_list):
    def __init__(self, count=None, offset=None, iswc=None):
        super(iswc_listSub, self).__init__(count, offset, iswc, )
supermod.iswc_list.subclass = iswc_listSub
# end class iswc_listSub


class user_tag_listSub(supermod.user_tag_list):
    def __init__(self, count=None, offset=None, user_tag=None):
        super(user_tag_listSub, self).__init__(count, offset, user_tag, )
supermod.user_tag_list.subclass = user_tag_listSub
# end class user_tag_listSub


class collection_listSub(supermod.collection_list):
    def __init__(self, count=None, offset=None, collection=None):
        super(collection_listSub, self).__init__(count, offset, collection, )
supermod.collection_list.subclass = collection_listSub
# end class collection_listSub


class editor_listSub(supermod.editor_list):
    def __init__(self, count=None, offset=None, editor=None):
        super(editor_listSub, self).__init__(count, offset, editor, )
supermod.editor_list.subclass = editor_listSub
# end class editor_listSub


class entity_listSub(supermod.entity_list):
    def __init__(self, count=None, offset=None, artist=None, release=None, release_group=None, recording=None, label=None, work=None, area=None, place=None, instrument=None, series=None, event=None):
        super(entity_listSub, self).__init__(count, offset, artist, release, release_group, recording, label, work, area, place, instrument, series, event, )
supermod.entity_list.subclass = entity_listSub
# end class entity_listSub


class cover_art_archiveSub(supermod.cover_art_archive):
    def __init__(self, artwork=None, count=None, front=None, back=None, darkened=None):
        super(cover_art_archiveSub, self).__init__(artwork, count, front, back, darkened, )
supermod.cover_art_archive.subclass = cover_art_archiveSub
# end class cover_art_archiveSub


class ipi_listSub(supermod.ipi_list):
    def __init__(self, ipi=None):
        super(ipi_listSub, self).__init__(ipi, )
supermod.ipi_list.subclass = ipi_listSub
# end class ipi_listSub


class iso_3166_1_code_listSub(supermod.iso_3166_1_code_list):
    def __init__(self, iso_3166_1_code=None):
        super(iso_3166_1_code_listSub, self).__init__(iso_3166_1_code, )
supermod.iso_3166_1_code_list.subclass = iso_3166_1_code_listSub
# end class iso_3166_1_code_listSub


class iso_3166_2_code_listSub(supermod.iso_3166_2_code_list):
    def __init__(self, iso_3166_2_code=None):
        super(iso_3166_2_code_listSub, self).__init__(iso_3166_2_code, )
supermod.iso_3166_2_code_list.subclass = iso_3166_2_code_listSub
# end class iso_3166_2_code_listSub


class iso_3166_3_code_listSub(supermod.iso_3166_3_code_list):
    def __init__(self, iso_3166_3_code=None):
        super(iso_3166_3_code_listSub, self).__init__(iso_3166_3_code, )
supermod.iso_3166_3_code_list.subclass = iso_3166_3_code_listSub
# end class iso_3166_3_code_listSub


class attribute_listTypeSub(supermod.attribute_listType):
    def __init__(self, attribute=None):
        super(attribute_listTypeSub, self).__init__(attribute, )
supermod.attribute_listType.subclass = attribute_listTypeSub
# end class attribute_listTypeSub


class attributeTypeSub(supermod.attributeType):
    def __init__(self, type_=None, type_id=None, value_id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeTypeSub, self).__init__(type_, type_id, value_id, valueOf_, mixedclass_, content_, )
supermod.attributeType.subclass = attributeTypeSub
# end class attributeTypeSub


class life_spanTypeSub(supermod.life_spanType):
    def __init__(self, begin=None, end=None):
        super(life_spanTypeSub, self).__init__(begin, end, )
supermod.life_spanType.subclass = life_spanTypeSub
# end class life_spanTypeSub


class attribute_listType1Sub(supermod.attribute_listType1):
    def __init__(self, attribute=None):
        super(attribute_listType1Sub, self).__init__(attribute, )
supermod.attribute_listType1.subclass = attribute_listType1Sub
# end class attribute_listType1Sub


class attributeType2Sub(supermod.attributeType2):
    def __init__(self, value=None, credited_as=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType2Sub, self).__init__(value, credited_as, valueOf_, mixedclass_, content_, )
supermod.attributeType2.subclass = attributeType2Sub
# end class attributeType2Sub


class track_listTypeSub(supermod.track_listType):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listTypeSub, self).__init__(count, offset, track, )
supermod.track_listType.subclass = track_listTypeSub
# end class track_listTypeSub


class track_listType3Sub(supermod.track_listType3):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType3Sub, self).__init__(count, offset, track, )
supermod.track_listType3.subclass = track_listType3Sub
# end class track_listType3Sub


class track_listType4Sub(supermod.track_listType4):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType4Sub, self).__init__(count, offset, track, )
supermod.track_listType4.subclass = track_listType4Sub
# end class track_listType4Sub


class trackTypeSub(supermod.trackType):
    def __init__(self, title=None, artist=None, length=None):
        super(trackTypeSub, self).__init__(title, artist, length, )
supermod.trackType.subclass = trackTypeSub
# end class trackTypeSub


class languageTypeSub(supermod.languageType):
    def __init__(self, fluency=None, valueOf_=None):
        super(languageTypeSub, self).__init__(fluency, valueOf_, )
supermod.languageType.subclass = languageTypeSub
# end class languageTypeSub


class track_listType5Sub(supermod.track_listType5):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType5Sub, self).__init__(count, offset, track, )
supermod.track_listType5.subclass = track_listType5Sub
# end class track_listType5Sub


class track_listType6Sub(supermod.track_listType6):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType6Sub, self).__init__(count, offset, track, )
supermod.track_listType6.subclass = track_listType6Sub
# end class track_listType6Sub


class trackType7Sub(supermod.trackType7):
    def __init__(self, title=None, artist=None, length=None):
        super(trackType7Sub, self).__init__(title, artist, length, )
supermod.trackType7.subclass = trackType7Sub
# end class trackType7Sub


class attribute_listType8Sub(supermod.attribute_listType8):
    def __init__(self, attribute=None):
        super(attribute_listType8Sub, self).__init__(attribute, )
supermod.attribute_listType8.subclass = attribute_listType8Sub
# end class attribute_listType8Sub


class attributeType9Sub(supermod.attributeType9):
    def __init__(self, value=None, credited_as=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType9Sub, self).__init__(value, credited_as, valueOf_, mixedclass_, content_, )
supermod.attributeType9.subclass = attributeType9Sub
# end class attributeType9Sub


class attribute_listType10Sub(supermod.attribute_listType10):
    def __init__(self, attribute=None):
        super(attribute_listType10Sub, self).__init__(attribute, )
supermod.attribute_listType10.subclass = attribute_listType10Sub
# end class attribute_listType10Sub


class attributeType11Sub(supermod.attributeType11):
    def __init__(self, type_=None, type_id=None, value_id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType11Sub, self).__init__(type_, type_id, value_id, valueOf_, mixedclass_, content_, )
supermod.attributeType11.subclass = attributeType11Sub
# end class attributeType11Sub


class attribute_listType12Sub(supermod.attribute_listType12):
    def __init__(self, attribute=None):
        super(attribute_listType12Sub, self).__init__(attribute, )
supermod.attribute_listType12.subclass = attribute_listType12Sub
# end class attribute_listType12Sub


class attributeType13Sub(supermod.attributeType13):
    def __init__(self, type_=None, type_id=None, value_id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType13Sub, self).__init__(type_, type_id, value_id, valueOf_, mixedclass_, content_, )
supermod.attributeType13.subclass = attributeType13Sub
# end class attributeType13Sub


class life_spanType14Sub(supermod.life_spanType14):
    def __init__(self, begin=None, end=None):
        super(life_spanType14Sub, self).__init__(begin, end, )
supermod.life_spanType14.subclass = life_spanType14Sub
# end class life_spanType14Sub


class attribute_listType15Sub(supermod.attribute_listType15):
    def __init__(self, attribute=None):
        super(attribute_listType15Sub, self).__init__(attribute, )
supermod.attribute_listType15.subclass = attribute_listType15Sub
# end class attribute_listType15Sub


class attributeType16Sub(supermod.attributeType16):
    def __init__(self, value=None, credited_as=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType16Sub, self).__init__(value, credited_as, valueOf_, mixedclass_, content_, )
supermod.attributeType16.subclass = attributeType16Sub
# end class attributeType16Sub


class track_listType17Sub(supermod.track_listType17):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType17Sub, self).__init__(count, offset, track, )
supermod.track_listType17.subclass = track_listType17Sub
# end class track_listType17Sub


class track_listType18Sub(supermod.track_listType18):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType18Sub, self).__init__(count, offset, track, )
supermod.track_listType18.subclass = track_listType18Sub
# end class track_listType18Sub


class track_listType19Sub(supermod.track_listType19):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType19Sub, self).__init__(count, offset, track, )
supermod.track_listType19.subclass = track_listType19Sub
# end class track_listType19Sub


class trackType20Sub(supermod.trackType20):
    def __init__(self, title=None, artist=None, length=None):
        super(trackType20Sub, self).__init__(title, artist, length, )
supermod.trackType20.subclass = trackType20Sub
# end class trackType20Sub


class languageType21Sub(supermod.languageType21):
    def __init__(self, fluency=None, valueOf_=None):
        super(languageType21Sub, self).__init__(fluency, valueOf_, )
supermod.languageType21.subclass = languageType21Sub
# end class languageType21Sub


class track_listType22Sub(supermod.track_listType22):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType22Sub, self).__init__(count, offset, track, )
supermod.track_listType22.subclass = track_listType22Sub
# end class track_listType22Sub


class track_listType23Sub(supermod.track_listType23):
    def __init__(self, count=None, offset=None, track=None):
        super(track_listType23Sub, self).__init__(count, offset, track, )
supermod.track_listType23.subclass = track_listType23Sub
# end class track_listType23Sub


class trackType24Sub(supermod.trackType24):
    def __init__(self, title=None, artist=None, length=None):
        super(trackType24Sub, self).__init__(title, artist, length, )
supermod.trackType24.subclass = trackType24Sub
# end class trackType24Sub


class attribute_listType25Sub(supermod.attribute_listType25):
    def __init__(self, attribute=None):
        super(attribute_listType25Sub, self).__init__(attribute, )
supermod.attribute_listType25.subclass = attribute_listType25Sub
# end class attribute_listType25Sub


class attributeType26Sub(supermod.attributeType26):
    def __init__(self, value=None, credited_as=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType26Sub, self).__init__(value, credited_as, valueOf_, mixedclass_, content_, )
supermod.attributeType26.subclass = attributeType26Sub
# end class attributeType26Sub


class attribute_listType27Sub(supermod.attribute_listType27):
    def __init__(self, attribute=None):
        super(attribute_listType27Sub, self).__init__(attribute, )
supermod.attribute_listType27.subclass = attribute_listType27Sub
# end class attribute_listType27Sub


class attributeType28Sub(supermod.attributeType28):
    def __init__(self, type_=None, type_id=None, value_id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(attributeType28Sub, self).__init__(type_, type_id, value_id, valueOf_, mixedclass_, content_, )
supermod.attributeType28.subclass = attributeType28Sub
# end class attributeType28Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'def_area_element_inner'
        rootClass = supermod.def_area_element_inner
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:mmd-2.0="http://musicbrainz.org/ns/mmd-2.0#"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'def_area_element_inner'
        rootClass = supermod.def_area_element_inner
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'def_area_element_inner'
        rootClass = supermod.def_area_element_inner
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:mmd-2.0="http://musicbrainz.org/ns/mmd-2.0#"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'def_area_element_inner'
        rootClass = supermod.def_area_element_inner
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from mb import *\n\n')
        sys.stdout.write('import mb as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
