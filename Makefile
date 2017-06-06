.PHONY: clean

mbrng/models.py: mmd-schema/schema/musicbrainz_mmd-2.0.rng
	java -jar ./bin/trang.jar -I rng -O xsd mmd-schema/schema/musicbrainz_mmd-2.0.rng musicbrainz_mmd.xsd
	generateDS.py -o $@ -s mbrng/mb_mmd_subs.py --super="mb" --external-encoding="utf-8" --export="write etree" musicbrainz_mmd.xsd

clean:
	rm mbrng/models.py mbrng/mb_mmd_subs.py
