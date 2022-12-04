extends Area2D

var v = 200
export var right_side = false
export var text = "A" setget set_text


func set_text(new_text):
	text = new_text
	var child = get_node("RichTextLabel")
	if not child:
		print_debug("didn't get RichTextLabel")
		return
	child.text = new_text


func _ready():
	self.connect("area_entered", self, "_area_entered")

func _process(delta):
	self.position += Vector2(v * delta * (-1 if right_side else 1), 0)

func _area_entered(other):
	if self.right_side:
		# aviod double counting
		return
	var child = get_node("RichTextLabel")
	var other_child = other.get_node("RichTextLabel")
	if not child or not other_child:
		print_debug("didn't get RichTextLabels")
		print_debug(child)
		print_debug(other_child)
		return
	if child.text != other_child.text:
		return
	Events.emit_signal("items_collided", child.text)
	other.queue_free()
	queue_free()
