def lookatpeople():
  i01.setHeadSpeed(40, 40, 40)
  x = (random.randint(1, 5))
  if x == 1:
    fullspeed()
    i01_head_rothead.moveTo(100)
    sleep(2)
    trackHumans()
    sleep(10)
    stopTracking()
  if x == 2:
    fullspeed()
    i01_head_rothead.moveTo(80)
    sleep(2)
    trackHumans()
    sleep(10)
    stopTracking()
  if x == 3:
    fullspeed()
    sleep(1)
    trackHumans()
    sleep(10)
    stopTracking()
  if x == 4:
    fullspeed()
    lookrightside()
    sleep(2)
    trackHumans()
    sleep(10)
    stopTracking()
  if x == 5:
    fullspeed()
    lookleftside()
    sleep(2)
    trackHumans()
    sleep(10)
    stopTracking()
  sleep(1)
  lookinmiddle()
  sleep(3)
  i01_mouth.speak("nice to meet you all")
  #i01_mouth.speak(u"Приятно с вами познакомиться")
  i01.finishedGesture()
