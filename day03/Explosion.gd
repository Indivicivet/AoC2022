extends Area2D


var text = "A"


func _ready():
	for other in get_overlapping_areas():
		var child = other.get_node("RichTextNode")
		if child and child.text == text:
			print_debug("exploded")
			other.queue_free()
