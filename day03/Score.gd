extends RichTextLabel


var score = 0

func _ready():
	Events.connect("items_collided", self, "_on_items_collided")

func _on_items_collided(text):
	score += 1
	self.text = str(score)
