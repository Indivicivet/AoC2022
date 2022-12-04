extends Area2D


var text = "A"


func _ready():
	self.connect("area_entered", self, "_area_entered")


func _area_entered(other):
	var child = other.get_node("RichTextLabel")
	if child and child.text == text:
		other.queue_free()
