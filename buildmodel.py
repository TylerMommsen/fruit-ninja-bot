from ultralytics import YOLO
import torch

if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if torch.cuda.is_available():
        print('using gpu')
        torch.cuda.set_device(0)

    model = YOLO('yolov5n.pt')
    model.train(data='./dataset/data.yaml', epochs=300, imgsz=640, batch=8, device='cuda')
