def pictureleftside():
  #i01.startedGesture()
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(109,90)
  i01.moveArm("left",90,105,24,75)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",81,65,82,60,105,113)
  sleep(1)
  i01.finishedGesture()

