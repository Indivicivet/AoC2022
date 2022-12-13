extends KinematicBody2D


var speed = 500;


func _process(delta):
	if Input.is_action_pressed("ui_right"):
		position.x += speed * delta;
	if Input.is_action_pressed("ui_left"):
		position.x -= speed * delta;


func _physics_process(delta):
	if Input.is_action_pressed("ui_accept"):
		var result_raydown = (
			get_world_2d().direct_space_state.intersect_ray(
				global_position,
				global_position + Vector2(0, 800),
				[self]
			)
		)
		if result_raydown:
			print("hello")
			result_raydown.collider.gravity_scale = -1.0

