extends Area2D


export var text_match = "A"


func _ready():
	self.connect("area_entered", self, "_area_entered")


func _area_entered(other):
	if not other is BackpackItem:
		return
	if other.text != text_match:
		return
	other.queue_free()
