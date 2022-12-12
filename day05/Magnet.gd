extends KinematicBody2D


var speed = 500;


func _process(delta):
	if Input.is_action_pressed("ui_right"):
		position.x += speed * delta;
	if Input.is_action_pressed("ui_left"):
		position.x -= speed * delta;
