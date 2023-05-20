import streamlit as st
import PIL
import matplotlib.pyplot as plt

from ultralytics import YOLO

def bounding_boxes(img):
    model = YOLO("yolov8n.pt")

    model_output = model(img)[0]

    results = model_output.boxes.boxes.cpu().numpy()

    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.imshow(img)

    # Plot boxes
    for result in results:
        # Draw square
        ax.add_patch(plt.Rectangle((result[0], result[1]),
            result[2] - result[0],
            result[3] - result[1],
            fill=False,
            edgecolor='red',
            linewidth=2))

        # Get name
        name = model_output.names[int(result[5])]

        # Draw label
        ax.text(result[0], result[1] - 2,
            s=str(name) + ' ' + str(round(result[4], 2)),
            color='white',
            verticalalignment='top',
            bbox={'color': 'red', 'pad': 0})

    #Remove axes
    ax.axis('off')

    return fig

img = st.sidebar.file_uploader("Sube una imagen", type=['png', 'jpg', 'jpeg'])

if img is not None:
    img = PIL.Image.open(img)

    columns = st.columns(2)

    columns[0].image(img, caption='Imagen original', use_column_width=True)

    columns[1].pyplot(bounding_boxes(img))

    columns[1].write("Imagen dibujada")