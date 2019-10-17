import face_recognition
import cv2
import numpy as np
from datetime import datetime
import time

                            #####################
                    # Recognise faces from images folder
                            #####################

# Load a first sample picture and learn how to recognize it.
karim_image = face_recognition.load_image_file("images/karim.jpg")
karim_face_encoding = face_recognition.face_encodings(karim_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    karim_face_encoding
]

known_face_names = [
    "Karim Mezhoud"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

                            #####################
                # run webcam  and Start a loop to detect faces
                            #####################

# Get a reference to webcam #0 (the default one)
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
                                #####################
                        #  recognise and compare faces
                              #####################

        # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        count = 0
        for face_encoding in face_encodings:
            count += 1
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]
            
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index] > 0.4 :
                name = known_face_names[best_match_index]
            else:
                crop = None
                print(face_locations)
                for (top, right, bottom, left) in face_locations:
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                
                # datetime object containing current date and time
                now = datetime.now()
                # dd/mm/YY H:M:S
                dt_string = now.strftime("%Y_%m_%d_%H_%M_%S_")    
                # Save the unknown  face into the unknown folder
                cv2.imwrite("unknown/"+ str(dt_string) + str(count) + ".jpg", frame[top:bottom, left:right])
 
            face_names.append(name)
            # Delays for 2 seconds . take one face at a time
            #time.sleep(2)  
    process_this_frame = not process_this_frame
    
                                        #####################
                                       # Tag and label faces
                                       #####################
        
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        best_distance = round(face_distances[best_match_index],2)
        cv2.putText(frame, str(name +" " +  str(best_distance)) , (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

        
    #     # Open file or create if not exists
    #     f = open("records/list.txt", "a+")
    #     # read lines and count
    #     f1 = f.readlines()
    #     
    #     if name == "Unknown":
    #         if len(f1) == 0:
    #             print(name)
    #             f.write("\n" + str(name))
    #             # Close the file
    #             f.flush()
    #             f.close()
    #             if count == 1:
    #                 break
    #             
    # # Save the captured image into the datasets folder
    # cv2.imwrite("records/" + str(name) + ".jpg", frame)
