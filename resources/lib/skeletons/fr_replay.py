# -*- coding: utf-8 -*-
# Copyright: (c) 2016, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals

from codequick import Script, utils

# The following dictionaries describe
# the addon's tree architecture.
# * Key: item id
# * Value: item infos
#     - route (folder)/resolver (playable URL): Callback function to run once this item is selected
#     - thumb: Item thumb path relative to "media" folder
#     - fanart: Item fanart path relative to "media" folder

root = "replay"

menu = {
    "mytf1": {
        "route": "/resources/lib/channels/fr/mytf1:mytf1_root",
        "label": "MYTF1",
        "thumb": "channels/fr/mytf1.png",
        "fanart": "channels/fr/mytf1_fanart.jpg",
        "enabled": True,
        "order": 1,
    },
    "francetv": {
        "route": "/resources/lib/channels/fr/francetv:francetv_root",
        "label": "france.tv",
        "thumb": "channels/fr/francetv.png",
        "fanart": "channels/fr/francetv_fanart.jpg",
        "enabled": True,
        "order": 2,
    },
    "mycanal": {
        "route": "/resources/lib/channels/fr/mycanal:mycanal_root",
        "label": "myCANAL",
        "thumb": "channels/fr/mycanal.png",
        "fanart": "channels/fr/mycanal_fanart.jpg",
        "enabled": True,
        "order": 4,
    },
    "6play": {
        "route": "/resources/lib/channels/fr/6play:sixplay_root",
        "label": "6play",
        "thumb": "channels/fr/6play.png",
        "fanart": "channels/fr/6play_fanart.jpg",
        "enabled": True,
        "order": 6,
    },
    "nrjplay": {
        "route": "/resources/lib/channels/fr/nrj:nrjplay_root",
        "label": "NRJ Play",
        "thumb": "channels/fr/nrjplay.png",
        "fanart": "channels/fr/nrjplay_fanart.jpg",
        "enabled": True,
        "order": 11,
    },
    "rmcbfmplay": {
        "route": "/resources/lib/channels/fr/rmcbfmplay:rmcbfmplay_root",
        "label": "RMC BFM Play",
        "thumb": "channels/fr/rmcbfmplay.png",
        "fanart": "channels/fr/rmcbfmplay_fanart.jpg",
        "enabled": True,
        "order": 13,
    },
    "cnews": {
        "route": "/resources/lib/channels/fr/cnews:list_categories",
        "label": "CNews",
        "thumb": "channels/fr/cnews.png",
        "fanart": "channels/fr/cnews_fanart.jpg",
        "enabled": True,
        "order": 14,
    },
    "lci": {
        "route": "/resources/lib/channels/fr/lci:lci_root",
        "label": "LCI",
        "thumb": "channels/fr/lci.png",
        "fanart": "channels/fr/lci_fanart.jpg",
        "enabled": True,
        "order": 16,
    },
    "lequipe": {
        "route": "/resources/lib/channels/fr/lequipe:list_programs",
        "label": "L'Équipe",
        "thumb": "channels/fr/lequipe.png",
        "fanart": "channels/fr/lequipe_fanart.jpg",
        "enabled": True,
        "order": 19,
    },
    "la_1ere": {
        "route": "/resources/lib/channels/fr/la_1ere:list_programs",
        "label": "La 1ère ("
        + utils.ensure_unicode(Script.setting["la_1ere.language"])
        + ")",
        "thumb": "channels/fr/la1ere.png",
        "fanart": "channels/fr/la1ere_fanart.jpg",
        "enabled": False,
        "order": 23,
    },
    "franceinfo": {
        "route": "/resources/lib/channels/fr/franceinfo:list_categories",
        "label": "France Info",
        "thumb": "channels/fr/franceinfo.png",
        "fanart": "channels/fr/franceinfo_fanart.jpg",
        "enabled": True,
        "order": 24,
    },
    "lcp": {
        "route": "/resources/lib/channels/fr/lcp:list_categories",
        "label": "LCP Assemblée Nationale",
        "thumb": "channels/fr/lcp.png",
        "fanart": "channels/fr/lcp_fanart.jpg",
        "enabled": True,
        "order": 31,
    },
    "publicsenat": {
        "route": "/resources/lib/channels/fr/publicsenat:list_categories",
        "label": "Public Sénat",
        "thumb": "channels/fr/publicsenat.png",
        "fanart": "channels/fr/publicsenat_fanart.jpg",
        "enabled": True,
        "order": 39,
    },
    "france3regions": {
        "route": "/resources/lib/channels/fr/france3regions:list_programs",
        "label": "France 3 Régions ("
        + utils.ensure_unicode(Script.setting["france3regions.language"])
        + ")",
        "thumb": "channels/fr/france3regions.png",
        "fanart": "channels/fr/france3regions_fanart.jpg",
        "enabled": False,
        "order": 40,
    },
    "francetvsport": {
        "route": "/resources/lib/channels/fr/francetvsport:list_categories",
        "label": "France TV Sport (francetv)",
        "thumb": "channels/fr/francetvsport.png",
        "fanart": "channels/fr/francetvsport_fanart.jpg",
        "enabled": True,
        "order": 41,
    },
    "histoire": {
        "route": "/resources/lib/channels/fr/tf1thematiques:list_categories",
        "label": "Histoire",
        "thumb": "channels/fr/histoire.png",
        "fanart": "channels/fr/histoire_fanart.jpg",
        "enabled": True,
        "order": 42,
    },
    "tvbreizh": {
        "route": "/resources/lib/channels/fr/tf1thematiques:list_categories",
        "label": "TV Breizh",
        "thumb": "channels/fr/tvbreizh.png",
        "fanart": "channels/fr/tvbreizh_fanart.jpg",
        "enabled": True,
        "order": 43,
    },
    "ushuaiatv": {
        "route": "/resources/lib/channels/fr/tf1thematiques:list_categories",
        "label": "Ushuaïa TV",
        "thumb": "channels/fr/ushuaiatv.png",
        "fanart": "channels/fr/ushuaiatv_fanart.jpg",
        "enabled": True,
        "order": 44,
    },
    "gameone": {
        "route": "/resources/lib/channels/fr/gameone:list_programs",
        "label": "Game One",
        "thumb": "channels/fr/gameone.png",
        "fanart": "channels/fr/gameone_fanart.jpg",
        "enabled": True,
        "order": 53,
    },
    "lumni": {
        "route": "/resources/lib/channels/fr/lumni:list_categories",
        "label": "Lumni (francetv)",
        "thumb": "channels/fr/lumni.png",
        "fanart": "channels/fr/lumni_fanart.jpg",
        "enabled": True,
        "order": 54,
    },
    "gong": {
        "route": "/resources/lib/channels/fr/gong:list_categories",
        "label": "Gong",
        "thumb": "channels/fr/gong.png",
        "fanart": "channels/fr/gong_fanart.jpg",
        "enabled": True,
        "order": 55,
    },
    "kto": {
        "route": "/resources/lib/channels/fr/kto:list_categories",
        "label": "KTO",
        "thumb": "channels/fr/kto.png",
        "fanart": "channels/fr/kto_fanart.jpg",
        "enabled": True,
        "order": 64,
    },
    "antennereunion": {
        "route": "/resources/lib/channels/fr/antennereunion:list_categories",
        "label": "Antenne Réunion",
        "thumb": "channels/fr/antennereunion.png",
        "fanart": "channels/fr/antennereunion_fanart.jpg",
        "enabled": True,
        "order": 65,
    },
    "ouatchtv": {
        "route": "/resources/lib/channels/fr/ouatchtv:list_programs",
        "label": "Ouatch TV",
        "thumb": "channels/fr/ouatchtv.png",
        "fanart": "channels/fr/ouatchtv_fanart.jpg",
        "enabled": False,
        "order": 67,
    },
    "lachainemeteo": {
        "route": "/resources/lib/channels/fr/lachainemeteo:list_programs",
        "label": "La Chaîne Météo",
        "thumb": "channels/fr/lachainemeteo.png",
        "fanart": "channels/fr/lachainemeteo_fanart.jpg",
        "enabled": True,
        "order": 70,
    },
    "j_one": {
        "route": "/resources/lib/channels/fr/j_one:list_videos",
        "label": "J-One",
        "thumb": "channels/fr/jone.png",
        "fanart": "channels/fr/jone_fanart.jpg",
        "enabled": True,
        "order": 71,
    },
    "via93": {
        "route": "/resources/lib/channels/fr/via:list_categories",
        "label": "vià93",
        "thumb": "channels/fr/via93.png",
        "fanart": "channels/fr/via93_fanart.jpg",
        "enabled": True,
        "order": 74,
    },
    "jack": {
        "route": "/resources/lib/channels/fr/jack:list_programs",
        "label": "Jack (mycanal)",
        "thumb": "channels/fr/jack.png",
        "fanart": "channels/fr/jack_fanart.jpg",
        "enabled": True,
        "order": 75,
    },
    "caledonia": {
        "route": "/resources/lib/channels/fr/caledonia:list_programs",
        "label": "Caledonia",
        "thumb": "channels/fr/caledonia.png",
        "fanart": "channels/fr/caledonia_fanart.jpg",
        "enabled": True,
        "order": 76,
    },
    "tebeo": {
        "route": "/resources/lib/channels/fr/tebeo:list_categories",
        "label": "Tébéo",
        "thumb": "channels/fr/tebeo.png",
        "fanart": "channels/fr/tebeo_fanart.jpg",
        "enabled": True,
        "order": 77,
    },
    "tl7": {
        "route": "/resources/lib/channels/fr/tl7:list_programs",
        "label": "Télévision Loire 7",
        "thumb": "channels/fr/tl7.png",
        "fanart": "channels/fr/tl7_fanart.jpg",
        "enabled": True,
        "order": 82,
    },
    "mblivetv": {
        "route": "/resources/lib/channels/fr/mblivetv:list_videos",
        "label": "Mont Blanc Live TV",
        "thumb": "channels/fr/mblivetv.png",
        "fanart": "channels/fr/mblivetv_fanart.jpg",
        "enabled": True,
        "order": 84,
    },
    "tv8montblanc": {
        "route": "/resources/lib/channels/fr/tv8montblanc:list_videos",
        "label": "8 Mont-Blanc",
        "thumb": "channels/fr/tv8montblanc.png",
        "fanart": "channels/fr/tv8montblanc_fanart.jpg",
        "enabled": True,
        "order": 85,
    },
    "luxetv": {
        "route": "/resources/lib/channels/fr/luxetv:list_categories",
        "label": "Luxe.TV",
        "thumb": "channels/fr/luxetv.png",
        "fanart": "channels/fr/luxetv_fanart.jpg",
        "enabled": True,
        "order": 86,
    },
    "alsace20": {
        "route": "/resources/lib/channels/fr/alsace20:list_categories",
        "label": "Alsace 20",
        "thumb": "channels/fr/alsace20.png",
        "fanart": "channels/fr/alsace20_fanart.jpg",
        "enabled": True,
        "order": 87,
    },
    "tvpifr": {
        "route": "/resources/lib/channels/fr/tvpifr:list_categories",
        "label": "TVPI télévision d'ici",
        "thumb": "channels/fr/tvpifr.png",
        "fanart": "channels/fr/tvpifr_fanart.jpg",
        "enabled": True,
        "order": 89,
    },
    "paramountchannel_fr": {
        "route": "/resources/lib/channels/fr/paramountchannel_fr:list_programs",
        "label": "Paramount Channel (FR)",
        "thumb": "channels/fr/paramountchannel_fr.png",
        "fanart": "channels/fr/paramountchannel_fr_fanart.jpg",
        "enabled": True,
        "order": 93,
    },
    "tebesud": {
        "route": "/resources/lib/channels/fr/tebeo:list_categories",
        "label": "TébéSud",
        "thumb": "channels/fr/tebesud.png",
        "fanart": "channels/fr/tebesud_fanart.jpg",
        "enabled": True,
        "order": 103,
    },
    "telegrenoble": {
        "route": "/resources/lib/channels/fr/telegrenoble:list_categories",
        "label": "TéléGrenoble",
        "thumb": "channels/fr/telegrenoble.png",
        "fanart": "channels/fr/telegrenoble_fanart.jpg",
        "enabled": True,
        "order": 105,
    },
    'albitv': {
        'route': '/resources/lib/channels/fr/albitv:list_videos_emissions',
        'label': 'Albi TV',
        'thumb': 'channels/fr/albitv.png',
        'fanart': 'channels/fr/albitv_fanart.jpg',
        'enabled': True,
        'order': 106
    },
    'dicitv': {
        'route': '/resources/lib/channels/fr/dicitv:list_videos',
        'label': 'DiCi TV',
        'thumb': 'channels/fr/dicitv.png',
        'fanart': 'channels/fr/dicitv_fanart.jpg',
        'enabled': True,
        'order': 107
    },
    "equidia": {
        "route": "/resources/lib/channels/fr/equidia:list_categories",
        "label": "Equidia",
        "thumb": "channels/fr/equidia.png",
        "fanart": "channels/fr/equidia_fanart.jpg",
        "enabled": True,
        "order": 122,
    },
    "bsmart": {
        "route": "/resources/lib/channels/fr/bsmart:list_categories",
        "label": "B Smart",
        "thumb": "channels/fr/bsmart.png",
        "fanart": "channels/fr/bsmart_fanart.jpg",
        "enabled": True,
        "order": 123,
    },
}
