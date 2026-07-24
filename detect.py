import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Products we want to detect
PRODUCTS = {
    "bottle": "Bottle",
    "apple": "Apple",
    "banana": "Banana",
    "orange": "Orange"
}


def detect_products():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        detected_items = {}

        for result in results:

            boxes = result.boxes

            for box in boxes:

                cls = int(box.cls[0])
                confidence = float(box.conf[0])

                class_name = model.names[cls]

                if confidence < 0.50:
                    continue

                if class_name not in PRODUCTS:
                    continue

                detected_items[class_name] = detected_items.get(class_name, 0) + 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame,
                              (x1, y1),
                              (x2, y2),
                              (0, 255, 0),
                              2)

                cv2.putText(frame,
                            f"{class_name} {confidence:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 255, 0),
                            2)

        # Display detected products
        y = 30

        for product, count in detected_items.items():

            cv2.putText(frame,
                        f"{product}: {count}",
                        (20, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 0, 0),
                        2)

            y += 30

        cv2.imshow("Retail Checkout", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_products()