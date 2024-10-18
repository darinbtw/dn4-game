extends CharacterBody2D

enum{
	MOVE,
	ATTACK,
	ATTACK2,
	ATTACK3,
	BLOCK,
	SLIDE
}

const SPEED = 300.0
const JUMP_VELOCITY = -400.0

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

@onready var anim = $AnimatedSprite2D
@onready var animPlayer = $AnimationPlayer
var health = 100
var gold = 0
var state = MOVE

func _physics_process(delta):
	
	match state:
		MOVE:
			pass
		ATTACK:
			pass
		ATTACK2:
			pass
		ATTACK3:
			pass
		BLOCK:
			pass
		SLIDE:
			pass
	
	# Add the gravity.
	if not is_on_floor():
		velocity.y += gravity * delta

	if health <= 0:
		queue_free()
		get_tree().change_scene_to_file("res://menu.tscn")
		
	if velocity.y > 0:
		animPlayer.play("Fall")

	move_and_slide()
	
func move_state ():
	var direction = Input.get_axis("left", "right")
	if direction:
		velocity.x = direction * SPEED
		if velocity.y == 0:
			animPlayer.play("Run")
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		if velocity.y == 0:
			animPlayer.play("Idle")
			
	if direction == -1:
		anim.flip_h = true
	elif direction == 1:
		anim.flip_h = false
		
