def picturerightside():
  #i01.startedGesture()
  i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 43.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 43.0, 43.0, 43.0, 43.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(109,90)
  i01.moveArm("left",5,94,28,15)
  i01.moveArm("right",90,115,23,68)
  i01.moveHand("left",42,58,87,55,71,35)
  i01.moveHand("right",10,112,95,91,125,45)
  sleep(1)
  i01.finishedGesture()

