extends Area2D
class_name BackpackItem


var explosion_resource = preload("res://Explosion.tscn")
var v = 50
export var right_side = false
var text setget set_text, get_text


func set_text(new_text):
	var child = get_node("RichTextLabel")
	if not child:
		print_debug("didn't get RichTextLabel")
		return
	child.text = new_text

func get_text():
	var child = get_node("RichTextLabel")
	if not child:
		print_debug("didn't get RichTextLabel")
		return
	return child.text


func _ready():
	self.connect("area_entered", self, "_area_entered")

func _process(delta):
	self.position += Vector2(v * delta * (-1 if right_side else 1), 0)

func _area_entered(other):
	if self.right_side:
		# aviod double counting
		return
	if not other.has_node("RichTextLabel"):
		return
	var child = get_node("RichTextLabel")
	var other_child = other.get_node("RichTextLabel")
	if child.text != other_child.text:
		return
	Events.emit_signal("items_collided", child.text)
	var explosion = explosion_resource.instance()
	explosion.position = position
	explosion.text = child.text
	get_node("..").add_child(explosion)
	get_node("..").move_child(explosion, 0)
	other.queue_free()
	queue_free()
