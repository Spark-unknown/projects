import cv2
from pyzbar import pyzbar
import webbrowser
import time

# Open the default camera
cap = cv2.VideoCapture(0)

start_time = time.time()
stored_data = ""
qr_detected = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Find and decode QR codes
    barcodes = pyzbar.decode(frame)
    
    # Loop through detected barcodes
    for barcode in barcodes:
        # Extract the data
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        
        # Display the data
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        # Open the QR code data in a web browser and store it
        if barcodeData.startswith("http") and stored_data != barcodeData:
            webbrowser.open(barcodeData)
            stored_data += barcodeData + "\n"
            with open("storedData.txt", "a") as f:
                f.write(barcodeData + "\n")
            qr_detected = True
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # Close the camera after 10 seconds if no QR code is detected
    if time.time() - start_time > 10 and not qr_detected:
        try:
            cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break
        except Exception as e:
            print(f"Error closing camera: {e}")
    
    # If QR code is detected, break the loop
    if qr_detected:
        break
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        try:
            cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break
        except Exception as e:
            print(f"Error closing camera: {e}")