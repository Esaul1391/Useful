import cv2

capture = cv2.VideoCapture(0)  # if 0 in camera oder write path

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

prev_x, prev_y = None, None

while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)        #    face capture
    face = cascade.detectMultiScale(gray, 1.3, 5)

    # driving face
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        font = cv2.FONT_HERSHEY_SIMPLEX

        if not prev_x:
            prev_x = x
        if not prev_y:
            prev_y = y

        ansver = ''
        diff_x = abs(prev_x - x)
        diff_y = abs(prev_y - y)
        if diff_x > 35 or diff_y > 35:
            if diff_x >diff_y:
                ansver = "No"
            elif diff_x > diff_y:
                ansver = "Yes"

        cv2.putText(frame, f"Ansver: {ansver}",
                    (10, 450),
                    font,
                    2,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA
                    )


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):      # set quit from cycle if setup "q"
        break

capture.release()
cv2.destroyWindow()
