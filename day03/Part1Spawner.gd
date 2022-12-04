extends Node2D


func _ready():
	var f = File.new()
	f.open("res://../inputs/input_day03.txt", File.READ)
	var lines = []
	while not f.eof_reached():
		var line = f.get_line()
		if line:
			lines.append(line)
	print_debug(lines[0])
	print_debug(lines[-1])
	var backpack_item_resource = preload("res://BackpackItem.tscn")
	for jj in range(lines.size()):
		var line = lines[jj]
		for ii in range(line.length()):
			var bp_item = backpack_item_resource.instance()
			bp_item.text = line[ii]
			bp_item.position = Vector2(ii * 21, jj * 21)
			if ii >= line.length() / 2:
				bp_item.right_side = true
			add_child(bp_item)
