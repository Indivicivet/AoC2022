extends Area2D

var v = 50
export var right_side = false

#func _ready():
	#pass

func _process(delta):
	self.position += Vector2(v * delta * (-1 if right_side else 1), 0)
