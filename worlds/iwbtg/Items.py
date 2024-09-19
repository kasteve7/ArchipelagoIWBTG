import typing

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World
from .Names import ItemName

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    trap: bool = False
    quantity: int = 1

class IWBTGItem(Item):
    game = "I Wanna Be the Guy"

# Item tables
event_table = {
    ItemName.mike_tyson_defeated:       ItemData(92000, ItemClassification.event),
    ItemName.mecha_birdo_defeated:      ItemData(92000, ItemClassification.event),
    ItemName.dracula_defeated:          ItemData(92000, ItemClassification.event),
    ItemName.kraidgief_defeated:        ItemData(92000, ItemClassification.event),
    ItemName.mother_brain_defeated:     ItemData(92000, ItemClassification.event),
    ItemName.bowser_defeated:           ItemData(92000, ItemClassification.event),
    ItemName.the_guy_defeated:          ItemData(92000, ItemClassification.event),
    ItemName.dev_room:                  ItemData(92001, ItemClassification.event),
}

access_item_table = {
    ItemName.spike_platform:            ItemData(92002, ItemClassification.progression),
    ItemName.link:                      ItemData(92002, ItemClassification.progression),
    ItemName.graveyard_moon:            ItemData(92003, ItemClassification.progression),
    ItemName.ryu:                       ItemData(92004, ItemClassification.progression),
    ItemName.tourian_key:               ItemData(92005, ItemClassification.progression),
}

orb_table = {
    ItemName.orb_mike_tyson:       		ItemData(92005, ItemClassification.progression),
    ItemName.orb_mecha_birdo:      		ItemData(92006, ItemClassification.progression),
    ItemName.orb_dracula:          		ItemData(92007, ItemClassification.progression),
    ItemName.orb_kraidgeif:        		ItemData(92008, ItemClassification.progression),
    ItemName.orb_mother_brain:     		ItemData(92009, ItemClassification.progression),
    ItemName.orb_bowser:           		ItemData(92010, ItemClassification.progression),
	
    ItemName.orb_piece_mike_tyson: 	ItemData(92105, ItemClassification.progression),
    ItemName.orb_piece_mecha_birdo: 	ItemData(92106, ItemClassification.progression),
    ItemName.orb_piece_dracula:     	ItemData(92107, ItemClassification.progression),
    ItemName.orb_piece_kraidgeif:   	ItemData(92108, ItemClassification.progression),
    ItemName.orb_piece_mother_brain:	ItemData(92109, ItemClassification.progression),
    ItemName.orb_piece_bowser:      	ItemData(92110, ItemClassification.progression),
}

secret_item_table = {
    ItemName.item_1:       ItemData(92011, ItemClassification.useful),
    ItemName.item_2:       ItemData(92012, ItemClassification.useful),
    ItemName.item_3:       ItemData(92013, ItemClassification.useful),
    ItemName.item_4:       ItemData(92014, ItemClassification.useful),
    ItemName.item_5:       ItemData(92015, ItemClassification.useful),
    ItemName.item_6:       ItemData(92016, ItemClassification.useful),
}

trap_table = {
    ItemName.bird_trap:      ItemData(92000, ItemClassification.trap),
    ItemName.fruit_trap:     ItemData(92000, ItemClassification.trap),
    ItemName.error_trap:     ItemData(92000, ItemClassification.trap),
    ItemName.stone_trap:     ItemData(92000, ItemClassification.trap),
    ItemName.death_trap:     ItemData(92000, ItemClassification.trap),
}

junk_table = {
    ItemName.bow:      ItemData(92000, ItemClassification.trap),
}

item_groups = {
    "Orbs": {
        ItemName.orb_mike_tyson,
        ItemName.orb_mecha_birdo,
        ItemName.orb_dracula,
		ItemName.orb_kraidgeif,
        ItemName.orb_bowser,
        ItemName.orb_mother_brain,
		
		ItemName.orb_piece_mike_tyson,
        ItemName.orb_piece_mecha_birdo,
        ItemName.orb_piece_dracula,
		ItemName.orb_piece_kraidgeif,
        ItemName.orb_piece_bowser,
        ItemName.orb_piece_mother_brain,
    },
    "Access": {
        ItemName.spike_platform,
        ItemName.link,
        ItemName.graveyard_moon,
        ItemName.ryu,
        ItemName.tourian_key,
    },
    "Secrets": {
        ItemName.item_1,
        ItemName.item_2,
        ItemName.item_3,
        ItemName.item_4,
        ItemName.item_5,
        ItemName.item_6,
    },
    "Traps": {
        ItemName.bird_trap,
        ItemName.fruit_trap,
        ItemName.error_trap,
        ItemName.stone_trap,
        ItemName.death_trap,
    },
	"Filler": {
		ItemName.char_kid,
		ItemName.char_owata,
		ItemName.char_vic,
	}
	"Junk": {
		ItemName.bow
	}
}

item_table = {
    **event_table,
    **orb_table,
    **access_item_table,
    **secret_item_table,
    **trap_table,
	**junk_table,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}