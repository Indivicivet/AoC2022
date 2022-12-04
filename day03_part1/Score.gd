extends RichTextLabel


var score = 0

func _ready():
	Events.connect("items_collided", self, "_on_items_collided")
	self.text = "Score: " + str(score)

func _on_items_collided(text):
	score += (
		ord(text) - 97 + 1  # a
		if ord(text) >= 97
		else ord(text) - 65 + 27  # A
	)
	self.text = "Score: " + str(score)
