def releasedelicate():
  #i01.startedGesture()
  i01.setHandSpeed("left", 19, 19, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 31.0, 31.0, 31.0, 59)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(22.0, 31.0)
  i01.moveHead(20,98)
  i01.moveArm("left",30,72,64,10)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",101,74,66,58,44,180)
  i01.moveHand("right",86,51,133,162,153,180)
  i01.setHeadSpeed(100.0,100.0,100.0,100.0,100.0)
  sleep(1)
  i01.finishedGesture()

