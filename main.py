import picamera	
camera = picamera.PiCamera()
camera.resolution = (2592, 1944)
camera.capture('Test-001.jpg')
