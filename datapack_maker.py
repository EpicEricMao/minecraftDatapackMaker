import os
import json

def openfile(path):
	if not os.path.isdir(path):
		os.mkdir(path)

if not os.path.isfile('pack_modify.json'):
	new_modify = open('pack_modify.json','w')
	new_modify.write('{\n  "name":"yourPackName",\n  "format":4,\n  "description":"Data Pack Description.",\n  "data":{\n    "minecraft":{\n      "tags":{\n        "function_tick":[],\n        "//":"functions that runs every tick",\n        "function_load":[],\n        "//":"functions that runs when game reloaded"\n      }\n    },\n    "yourCustomNamespace":{\n      "make_folder":{\n        "advancements":false,\n        "functions":false,\n        "loot_tables":false,\n        "predicates":false,\n        "structures":false,\n        "recipes":false,\n        "tags":{\n          "blocks":false,\n          "entity_types":false,\n          "items":false,\n          "fluids":false,\n          "functions":false\n        }\n      },\n      "make_templates":{\n        "advancements":false,\n        "functions":false,\n        "loot_tables":false,\n        "predicates":false,\n        "recipes":false,\n        "tags":{\n          "blocks":false,\n          "entity_types":false,\n          "items":false,\n          "fluids":false,\n          "functions":false\n        }\n      }\n    }\n  }\n}')
	new_modify.close()
	exit()

with open('pack_modify.json') as reader:
	modify = json.load(reader)

pkname = modify['name']
pk_format = modify['format']
pk_description = modify['description']

openfile(pkname)

mcmeta = open(pkname + '/' + 'pack.mcmeta','w')
mcmeta.write('{\n  "pack":{\n    "pack_format":' + str(pk_format) + ',\n    "description":"' + pk_description + '"\n  }\n}')

openfile(pkname + '/data')
openfile(pkname + '/data/minecraft')
openfile(pkname + '/data/minecraft/tags')
openfile(pkname + '/data/minecraft/tags/functions')
func_tick = open(pkname + '/data/minecraft/tags/functions/tick.json','w')
tmp = ''
for i in modify['data']['minecraft']['tags']['function_tick']:
	tmp += '    "' + i + '"'
	if modify['data']['minecraft']['tags']['function_tick'].index(i) != len(modify['data']['minecraft']['tags']['function_tick'])-1:
		tmp += ','
	tmp += '\n'
func_tick.write('{\n  "values":[\n' + tmp + '  ]\n}')
func_load = open(pkname + '/data/minecraft/tags/functions/load.json','w')
tmp = ''
for i in modify['data']['minecraft']['tags']['function_load']:
	tmp += '    "' + i + '"'
	if modify['data']['minecraft']['tags']['function_load'].index(i) != len(modify['data']['minecraft']['tags']['function_load'])-1:
		tmp += ','
	tmp += '\n'
func_load.write('{\n  "values":[\n' + tmp + '  ]\n}')

contentl = ['advancements','functions','loot_tables','predicates','structures','recipes','tags']
tagl = ['blocks','entity_types','items','fluids','functions']
template_type = {'advancements':'.json','functions':'.mcfunction','loot_tables':'.json','predicates':'.json','recipes':'.json'}
template_content = {'advancements':'{\n  "display":{\n    "icon":{\n      "item":"minecraft:stone",\n      "nbt":"{CustomModelData:1b}"\n    },\n    "title":"[{\"text\":\"An example advancement.\"}]",\n    "frame":"task",\n    "description":"Description of the advancement.",\n    "show_toast":false,\n    "announce_to_chat":false,\n    "hidden":true\n  },\n  "criteria":{\n    "creteriaName":{\n      "trigger":"minecraft:impossible"\n    }\n  },\n  "requirements":[\n    "creteriaName"\n  ],\n  "rewards":{\n    "recipes":[\n      "minecraft:recipe_name"\n    ],\n    "loot":[\n      "minecraft:loot_name"\n    ],\n    "experience":5,\n    "function":"foo:bar"\n  }\n}','functions':'say hi','loot_tables':'{\n  "type":"generic",\n  "pools":[\n    {\n      "conditions":[\n        {"condition":"conditionName"}\n      ],\n      "rolls":{\n        "min":0,\n        "max":3\n      },\n      "bonus_rolls":{\n        "min":0,\n        "max":3\n      },\n      "entries":[\n        {\n          "conditions":[\n            {"condition":"conditionName"}\n          ],\n          "type":"item",\n          "name":"minecraft:item_id",\n          "weight":1,\n          "quality":2\n        }\n      ]\n    }\n  ]\n}','predicates':'{\n  "condition":"random_chance",\n  "chance":0.5\n}','recipes':'{\n  "type":"minecraft:crafting_shaped",\n  "pattern":[\n    "#T#",\n    "DND",\n    "EOE"\n  ],\n  "key":{\n    "#":{"item": "minecraft:diamond"},\n    "T":{"item": "minecraft:totem_of_undying"},\n    "D":{"item": "minecraft:dragon_breath"},\n    "N":{"item": "minecraft:nether_star"},\n    "E":{"item": "minecraft:emerald"},\n    "O":{"item": "minecraft:obsidian"}\n  },\n  "result":{\n    "item":"minecraft:potato",\n    "count": 1\n  }\n}'}

for i in modify['data']:
	if i == 'minecraft':
		continue
	else:
		openfile(pkname + '/data/' + i)
		for j in contentl:
			if (j in modify['data'][i]['make_folder']) and (modify['data'][i]['make_folder'][j] == True):
				openfile(pkname + '/data/' + i + '/' + j)
				if (j in modify['data'][i]['make_templates']) and (modify['data'][i]['make_templates'][j] == True):
					template = open(pkname + '/data/' + i + '/' + j + '/template' + template_type[j],'w')
					template.write(template_content[j])
			if j == 'tags':
				for k in tagl:
					if (k in modify['data'][i]['make_folder']['tags']) and (modify['data'][i]['make_folder']['tags'][k] == True):
						openfile(pkname + '/data/' + i + '/' + j)
						openfile(pkname + '/data/' + i + '/' + j + '/' + k)
						if (k in modify['data'][i]['make_templates']['tags']) and (modify['data'][i]['make_templates']['tags'][k] == True):
							template = open(pkname + '/data/' + i + '/' + j + '/' + k + '/template.json','w')
							template.write('{\n  "values":[\n    "foo:bar1",\n    "foo:bar2"\n  ]\n}')