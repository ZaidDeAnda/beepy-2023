# Despliegue de YOLO en streamlit

Ahora, vamos a hacer una aplicación streamlit que al momento de subir una imagen, te pueda hacer la detección de objetos.

Primero haremos una función `draw_bounding_boxes`, que dado una imagen, genere su predicción de cajas en YOLO y dibuje sobre ellas esas cajas.
La función será un poco compleja y seguramente no haya tanto tiempo para explicar en persona esté código, pero la función es:

```python
    import streamlit as st

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
```

Básicamente, realiza la inferencia sobre la imagen, obtiene las cajas, y para cada caja dibuja un rectángulo sobre las coordenadas de la imagen. Finalmente, dibuja el nombre de la clase cerca de la caja que acaba de dibujar.

Después de eso, pedimos que en nuestra página de streamlit se suba una imagen, y que cuando se suba, la muestre en una columna a la izquierda.

```python
    img = st.sidebar.file_uploader("Sube una imagen", type=['png', 'jpg', 'jpeg'])

    if img is not None:
        img = PIL.Image.open(img)

        columns = st.columns(2)

        columns[0].image(img, caption='Imagen original', use_column_width=True)
```

Después, llamamos la función `draw_bounding_boxes` sobre esta imagen, y la graficamos. 

```python
    columns[1].pyplot(bounding_boxes(img))

    columns[1].write("Imagen dibujada")
```

## BONUS: despliegue en streamlit cloud!

Si te registras en https://streamlit.io/, puedes desplegar tu aplicación en la nube de streamlit, para que cualquier persona pueda acceder a ella!