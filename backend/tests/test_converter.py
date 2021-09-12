# -*- coding: utf-8 -*-
from mtpylon.types import long

from converter import (
    int64_to_long,
    long_to_int64,
    int2048_to_bytes,
    bytes_to_int2048
)

int_value = 39272391711858965859357247302539762225426965279027970582290284308595419394440285107459644417689477975526491410702667331388612046325239050546381571076589610240184943649450640764843570382634789795798030161524760864681913649643294797279466713528958148253767882088916696237782675170554127852978502596754588603604906171707238981314634472178436591652807349394799592427854430886778549606624728693877761242534091081663213292809167858909353541578873982495744164333205450555919731331357122016906507375046184992487211826115132878290338641724156808394673000604380946237299649938561447024614059239128205485006487611353680633800  # noqa

bytes_value = (
    b'\x00O\xa4\x12\r6F\xe1\xca\xdc~!\xfc\xc9\xc4a\x11\xff\x84gfY\x08\xa5'
    b'k\x18\xbd8\xbe\xe6\x0e\xe1\xcc\xcc.\xffi\xdd\xa5\xe68\xbe+\x06'
    b'\xe8\x13\xe6\xd9\x83!B\xa0T\xd2/@]\x9dAoy\x16\x81@\xd3s\xb0H\xf5Y$\xb8'
    b'6\xec[\xe2\xab\x92\xe2\x96$\xed\xf6{\xd5\xd7c\xf8\xa1\\:\xedX~z\xc7'
    b'\x0f\x8f\xe0\xd7\x8d\xe4\\K\x9e\xa5\xb8\x1a\x1e\t\x8e\xb0d\xdc\x96\t'
    b'\xfa7\xca3\xf7\x03\xb4\x84a\xae\xd3C'
    b'\xaa\xbc\x14\x98\xddM\x1c\xbb\xf3\xcaLV'
    b'\xcc\x8c}\xc3\x15\xe2Q\xe2\x83\x12\xed%\x8ct2g)\x11\x82Q\xf9\x15?z'
    b'\xc9\xd5+\xd4\x7f\xdfpr\x96?c0\xf0k\xb7.,\xc7D\xaf\x91\xdf3\x02'
    b'\x80\x0e\x80\xc2<%\xa4\x02\xb9{\xfcR'
    b'\x92X\x9b\x1ch\x8b\xd1\xfd\xe0\xe9\x99}'
    b'\x99\x96\xa3.\xbd9\xba%\x817\xb1#'
    b'\xfav/\xd0uH\xc4O\xd1\xb92\x17x\xf6\xec4'
    b'd\xae9@,\x04E\xbd\x02\xfa\x82#\xb3\x0c\xdf\xc8'
)


def test_int64_to_long():
    assert int64_to_long(16462053750161430071) == long(-1984690323548121545)


def test_long_to_int64():
    assert long_to_int64(long(-1984690323548121545)) == 16462053750161430071


def test_int2048_to_bytes():
    assert int2048_to_bytes(int_value) == bytes_value


def test_bytes_to_int2048():
    assert bytes_to_int2048(bytes_value) == int_value
