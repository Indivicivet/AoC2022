extends Area2D

var v = 50
export var right_side = false

func _ready():
	self.connect("area_entered", self, "_area_entered")

func _process(delta):
	self.position += Vector2(v * delta * (-1 if right_side else 1), 0)

func _area_entered(other):
	print_debug(other)
