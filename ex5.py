name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# This line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# Extra credit
print "That's a test, %r %r. " % (name, age)

height_cm = height * 2.54
weight_kg = weight * 0.45359237

print "He is %.2f cm tall." % height_cm
print "he is %.2f kg heavy." % weight_kg
