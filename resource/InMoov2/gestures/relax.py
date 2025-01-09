def relax():
  #i01.startedGesture()
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 0, 0, 20, 50)
    sleep(2)
    i01_neoPixel.setAnimation("Ironman", 0, 255, 255, 50)
  if runtime.isStarted('i01.opencv') and i01_opencv.isCapturing():
    i01.setHandSpeed("left", 43, 43, 43, 43, 43, 43)
    i01.setHandSpeed("right", 43, 43, 43, 43, 43, 43)
    i01.setArmSpeed("right", 31, 43, 23, 43)
    i01.setArmSpeed("left", 60, 23, 31, 31)
    #i01.setHeadSpeed(43, 43)
    i01.setTorsoSpeed(31, 16, 100.0)
    #i01.moveHead(79.00,100.00,122.17,64.06,0.00,90.00)
    i01.moveArm("left",5.00,84.00,25.00,12.00)
    i01.moveArm("right",5.00,82.00,25.00,12.00)
    i01.moveHand("left",92.00,33.00,37.00,71.00,66.00,25.00)
    i01.moveHand("right",81.00,66.00,82.00,60.00,23.00,160.00)
    i01.moveTorso(95.00,90.00,90.00)
  else:
    i01.setHandSpeed("left", 43, 43, 43, 43, 43, 43)
    i01.setHandSpeed("right", 43, 43, 43, 43, 43, 43)
    i01.setArmSpeed("right", 31, 43, 23, 43)
    i01.setArmSpeed("left", 60, 23, 31, 31)
    i01.setHeadSpeed(43, 43)
    i01.setTorsoSpeed(31, 16, 100.0)
    i01.moveHead(79.00,100.00,122.17,64.06,0.00,90.00)
    i01.moveArm("left",5.00,84.00,25.00,12.00)
    i01.moveArm("right",5.00,82.00,25.00,12.00)
    i01.moveHand("left",92.00,33.00,37.00,71.00,66.00,25.00)
    i01.moveHand("right",81.00,66.00,82.00,60.00,23.00,160.00)
    i01.moveTorso(95.00,90.00,90.00)
  i01.finishedGesture()