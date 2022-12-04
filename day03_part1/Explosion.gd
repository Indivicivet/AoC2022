extends Area2D


var text = "A"


func _ready():
	self.connect("area_entered", self, "_area_entered")


func _area_entered(other):
	if not other.has_node("RichTextLabel"):
		return
	if other.get_node("RichTextLabel").text == text:
		other.queue_free()
