def shrug():
  ## i2Head
  i01_head_forheadLeft.moveTo(0.0)
  i01_head_forheadRight.moveTo(0.0)
  i01_head_upperLip.moveTo(113.0)
  i01_head_cheekLeft.moveTo(82.0)
  i01_head_cheekRight.moveTo(180.0)
  i01_head_eyebrowLeft.moveTo(76.0)
  i01_head_eyebrowRight.moveTo(29.0)
  i01_head_eyelidRightLower.moveTo(23.0)
  i01_head_eyelidRightUpper.moveTo(100.0)
  i01_head_eyelidLeftLower.moveTo(72.0)
  i01_head_eyelidLeftUpper.moveTo(137.0)
  i01_head_eyeRightLR.moveTo(84.0)
  i01_head_eyeRightUD.moveTo(90.0)
  i01_head_eyeLeftLR.moveTo(88.0)
  i01_head_eyeLeftUD.moveTo(84.0)
  ##body
  i01.setHandSpeed("left", 19, 19, 19, 19, 19, 19)
  i01.setHandSpeed("right", 19, 36, 19, 19, 19, 19)
  i01.setArmSpeed("left", 60, 60, 60, 60)
  i01.setArmSpeed("right", 60, 60, 60, 60)
  i01.setHeadSpeed(22.0, 22.0)
  i01.moveHead(80,90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  sleep(1)
  i01.finishedGesture()
  neutral()
  relax()