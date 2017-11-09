# Team MakeSmart
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# Lab 7


#Warmup
def snowman():
  """creates a three circle figure looking like a snowman"""
  
  #opens a file
  pic = makePicture(pickAFile())
  
  #draws the head
  addOvalFilled(pic, 310, 80, 60,70, white)
  
  #draws the eyes
  addOvalFilled(pic, 324, 105, 5,5, green)
  addOvalFilled(pic, 351, 105, 5,5, green)
  
  #draws the nose
  addLine(pic,326,123,336,115,orange)
  addLine(pic,326,123,339,123,orange)
  
  #draws the mouth
  addArc(pic, 327, 134,20, 5, 0, -180,black)
  
  #draws the middle circle
  addOvalFilled(pic, 277, 148, 120,130, white)
  
  #draws the lower circle
  addOvalFilled(pic, 227, 268, 220,30, white)
 
  show(pic)

# problem 1
#def thanksgivingCard():
