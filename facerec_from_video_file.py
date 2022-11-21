import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
input_movie = cv2.VideoCapture("Movie.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# fourcc = cv2.VideoWriter_fourcc(*'H264')
# output_movie = cv2.VideoWriter('Characters_recognition.avi', -1, 60, (649, 272))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('Characters_recognition.avi', fourcc, 30.0, (int(input_movie.get(3)),int(input_movie.get(4))))

# output_movie = cv2.VideoWriter('Test.mp4', fourcc, 60, (640, 360))

# Load some sample pictures and learn how to recognize them.
Captain_america_image = face_recognition.load_image_file("Captain america.jpeg")
Captain_america_face_encoding = face_recognition.face_encodings(Captain_america_image)[0]

iron_man_image = face_recognition.load_image_file("iron man.jpg")
iron_man_face_encoding = face_recognition.face_encodings(iron_man_image)[0]

spider_man_image = face_recognition.load_image_file("spider man.jpg")
spider_man_face_encoding = face_recognition.face_encodings(spider_man_image)[0]

# Black_panther_image = face_recognition.load_image_file("Black Panther.jpeg")
# Black_panther_face_encoding = face_recognition.face_encodings(Black_panther_image)[0]


# Star_lord_image = face_recognition.load_image_file("Star_lord.png")
# Star_lord_face_encoding = face_recognition.face_encodings(Star_lord_image)[0]

# Thanos_image = face_recognition.load_image_file("Thanos.jpeg")
# Thanos_face_encoding = face_recognition.face_encodings(Thanos_image)[0]

Thor_image = face_recognition.load_image_file("Thor.jpeg")
Thor_face_encoding = face_recognition.face_encodings(Thor_image)[0]

Black_widow_image = face_recognition.load_image_file("Black widow.jpeg")
Black_widow_face_encoding = face_recognition.face_encodings(Black_widow_image)[0]

Bruce_image = face_recognition.load_image_file("Bruce.jpeg")
Bruce_face_encoding = face_recognition.face_encodings(Bruce_image)[0]

Proxima_image = face_recognition.load_image_file("Proxima.jpeg")
Proxima_face_encoding = face_recognition.face_encodings(Proxima_image)[0]

# Cull_Obsidian_image = face_recognition.load_image_file("Cull Obsidian.jpeg")
# Cull_Obsidian_face_encoding = face_recognition.face_encodings(Cull_Obsidian_image)[0]

# Groot_image = face_recognition.load_image_file("Groot.jpeg")
# Groot_face_encoding = face_recognition.face_encodings(Groot_image)[0]

# Rocket_image = face_recognition.load_image_file("Rocket.jpeg")
# Rocket_face_encoding = face_recognition.face_encodings(Rocket_image)[0]

known_faces = [
    Captain_america_face_encoding,
    iron_man_face_encoding,
    spider_man_face_encoding,
    # Black_panther_image,
    Thor_face_encoding,
    Black_widow_face_encoding,
    Bruce_face_encoding,
    Proxima_face_encoding
    # Cull_Obsidian_image,
    # Groot_image,
    # Rocket_image
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "Captain America"
        elif match[1]:
            name = "Iron Man"
        elif match[2]:
            name = "Spider Man"
        # elif match[3]:
        #     name = "Black Panther"
        elif match[3]:
            name = "Thor"
        elif match[4]:
            name = "Black Widow"
        elif match[5]:
            name = "Bruce"
        elif match[6]:
            name = "Proxima"
        # elif match[8]:
        #     name = "Cull Obsidian"
        # elif match[7]:
        #     name = "Groot"
        # elif match[8]:
        #     name = "Rocket"

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# All done!
input_movie.release()
cv2.destroyAllWindows()
