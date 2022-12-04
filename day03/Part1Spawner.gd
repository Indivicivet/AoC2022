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
