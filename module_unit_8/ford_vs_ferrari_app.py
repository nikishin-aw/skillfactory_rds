import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

with tf.device('cpu:0'):
    # model
    model = load_model('1-best_model_part_9.hdf5')

# Classes
classes = {
    0: 'Lada Priora',
    1: 'Ford Focus',
    2: 'Lada 21015',
    3: 'Lada 2110',
    4: 'Lada 2107',
    5: 'Lada Niva',
    6: 'Lada Kalina',
    7: 'Lada 2109',
    8: 'Volkswagen Passat',
    9: 'Lada 21099'
}

# Head
st.title('Классификация авто по фотографии')
st.write(
    '''
    - Никакой магии.
    - Не создает зависимости.
    - Без ГМО.
    '''
)

st.write(
    '''
    Здесь можно взять картинки для загрузки: [Ссылка](https://drive.google.com/drive/folders/1dQEXiztZ0r7Q8AdexRcbU_rBkg5PwTKe?usp=sharing "Картинки машин")
    '''
)

# Load image
img_file_buffer = st.file_uploader('Загрузите картинку', type='jpg',)
if img_file_buffer is not None:
    image_loaded = Image.open(img_file_buffer)
    st.image(image_loaded, use_column_width=True)

# Predict
with tf.device('cpu:0'):
    if img_file_buffer is not None:
        # image
        img_for_model = np.array(image_loaded)
        img_for_model = img_for_model.reshape((1, img_for_model.shape[0], img_for_model.shape[1], img_for_model.shape[2]))
        
        # preparing data
        test_datagen = ImageDataGenerator(rescale=1. / 255)
        test_sub_generator = test_datagen.flow(
            img_for_model,
            batch_size=16
        )
        
        # predict
        predictions = model.predict_generator(test_sub_generator, steps=len(test_sub_generator))
        
        # output data
        max_p = np.max(predictions)
        num_calass = np.where(predictions == max_p)[1][0]
        name_model = classes[num_calass]

        # output text
        if max_p > 0.9:
            st.write(f'### Это сто пудово {name_model}! Уверен с вероятностю {round(max_p*100, 2)}%!')
        elif max_p > 0.65:
            st.write(f'### Это скорее всего {name_model}. Уверен с вероятностю {round(max_p*100, 2)}%!')
        elif max_p >0.5:
            st.write(f'### Не очень уверен, но мне кажется, что это {name_model}. Но вероятность не больше {round(max_p*100, 2)}%!')
        elif max_p > 0.3:
            st.write(f'### Меня такому не учили! Но предположу, что это {name_model}. Хотя вероятность этого всего {round(max_p*100, 2)}%!')
        else:
            st.write('### Даже предполагать не буду! На этой фотке не то, что мне нравится! )))')

# footer
st.write(
    '''
    ***
    ** Умею угадывать такие автомобили: **

    - Lada Priora
    - Ford Focus
    - Lada 21015
    - Lada 2110
    - Lada 2107
    - Lada Niva
    - Lada Kalina
    - Lada 2109
    - Volkswagen Passat
    - Lada 21099
    
    * *Беру обратно свои слова про магию!*
    '''
)