extends Node2D

var speed = 200  # Скорость движения
var jump_force = 500  # Сила прыжка
var vel = Vector2()  # Вектор скорости

func _physics_process(delta):
	vel = Vector2()  # Сбрасываем скорость

	if Input.is_action_pressed("player_left"):
		vel.x -= speed  # Влево
	if Input.is_action_pressed("player_right"):
		vel.x += speed  # Вправо

	# Обновляем позицию игрока
	position += vel * delta  # Изменяем позицию в зависимости от скорости
